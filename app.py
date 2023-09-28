import os
import openai
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import AzureSearch
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import TextLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
import streamlit as st

# Load environment variables
load_dotenv()

# Configure OpenAI API
openai.api_type = "azure"
openai.api_base = os.getenv('OPENAI_API_BASE')
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_version = os.getenv('OPENAI_API_VERSION')

# Initialize gpt-35-turbo and our embedding model
llm = AzureChatOpenAI(deployment_name=os.getenv('OPENAI_API_DEPLOYMENT_NAME'))
embeddings = OpenAIEmbeddings(deployment_id=os.getenv('OPENAI_API_EMBEDDING_NAME'), chunk_size=1)

# Connect to Azure Cognitive Search
acs = AzureSearch(azure_search_endpoint=os.getenv('AZURE_COGNITIVE_SEARCH_SERVICE_NAME'),
                 azure_search_key=os.getenv('AZURE_COGNITIVE_SEARCH_API_KEY'),
                 index_name=os.getenv('AZURE_COGNITIVE_SEARCH_INDEX_NAME'),
                 embedding_function=embeddings.embed_query)

# Load data from disk
loader = DirectoryLoader('data/qna/', glob="*.txt", loader_cls=TextLoader, loader_kwargs={'autodetect_encoding': True})
documents = loader.load()

# Chunk documents into smaller pieces
# 1000 for the chunk size is the default value
# Chunk overlap is set to 0 to avoid duplicate chunks but you can change that value to increase context
text_splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Add documents to Azure Search with their embeddings
acs.add_documents(documents=docs)

# Building prompt
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template("""Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:""")

# Using Langchain to create a conversation with chatGPT based on the data retrieved from Azure Cognitive Search
qa = ConversationalRetrievalChain.from_llm(llm=llm,
                                           retriever=acs.as_retriever(),
                                           condense_question_prompt=CONDENSE_QUESTION_PROMPT,
                                           return_source_documents=True,
                                           verbose=False)


# Create a nice title for our webUI
st.title('🦜🔗 GPT Bring your own docs')

#Create text input box
prompt = st.text_input('Enter prompt here:')

# Create a session state to store the chat history for the follow up questions
chat_history = []
if 'history' not in st.session_state:
    st.session_state.history = []

if prompt:    
    chat_history = st.session_state.history
    result = qa({"question": prompt, "chat_history": chat_history})
    st.write("Question:", prompt)
    st.write("Answer:", result["answer"])
    st.session_state.history.append((prompt, result["answer"]))
