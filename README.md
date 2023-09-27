# AOAI_VectorDB_CognitiveSearch
> Quick demo: Azure OpenAI integration with Vector Database and Cognitive Search

## Deployment steps:

### Infrastructure

- Create a deployment of ChatGPT 3.5
- Create a deployment of embedding ada 002
- Create a Cognitive Search service with at least basic tier
- Optional: create a search index, if you don't the 'demo' index will be created

### Code

- Install depedancies 
```bash
pip install azure-identity --upgrade 
pip install openai --upgrade 
pip install langchain --upgrade 
pip install azure-search-documents --pre --upgrade
```

- Create a .env file as follow:

```bash
OPENAI_API_BASE=https://NAMEOFYOUROPENAI.openai.azure.com/ 
OPENAI_API_KEY=KEY OPENAI_API_VERSION=2023-07-01-preview 
OPENAI_API_DEPLOYMENT_NAME=NAME OF YOUR CHATGPT 3.5 DEPLOYMENT 
OPENAI_API_EMBEDDING_NAME=NAME OF YOUR EMBEDDING DEPLOYMENT 
AZURE_COGNITIVE_SEARCH_SERVICE_NAME=https://NAMEOFYOURDB.search.windows.net 
AZURE_COGNITIVE_SEARCH_API_KEY=KEY 
AZURE_COGNITIVE_SEARCH_INDEX_NAME=demo
```

## Tools: 
- Azure OpenAI 
- Azure Cognitive Search 
- Langchain 
- Streamlit

## Start the app: 
streamlit run .\app.py

## Questions:
- what is Azure OpenAI Service?
- Which regions does the service support?

All the data is coming from this repo: https://github.com/microsoft/azure-openai-in-a-day-workshop/tree/main/data/qna

## Story

There is a cool capability in Azure Cognitive Search called Vector Search.
This is something that can really help us when you want to chat with your own data using Azure OpenAI like chatGPT 4.
The goal here is to bring the source data to query against it and show in the prompt the source data.
One of the problem we are facing is the token limit so we need to only show in the prompt the data that is relevant to the question.
So how can we retrieve the relevant data to feed it to the prompt ? Should I use Azure Cognitive search with semantic search or use a vector search ?
If you don't remember what is a vector search: Basically calculate the distance between your source embedding and the prompt embedding
If you don't remember what is a semantic search: Deep learning search machine model that Bing leverage

Today you don't need anymore to create your own vector search because everything is embedded in Azure Cognitive Search, it can do both semantic search and vector search. 
One if the issue we are going to face is, Azure Cognitive Search does not generate vector embeddings for your content but we can leverage Azure OpenAI to do it for us.

Here are a couple of use cases this architecture can cover from [Documentation](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)

>Vector search for text. Encode text using embedding models such as OpenAI embeddings or open source models such as SBERT, and retrieve documents with queries that are also encoded as vectors.
>
>Vector search across different data types (multi-modal). Encode images, text, audio, and video, or even a mix of them (for example, with models like CLIP) and do a similarity search across them.
>
>Multi-lingual search. Use a multi-lingual embeddings model to represent your document in multiple languages in a single vector space to find documents regardless of the language they are in.
>
>Hybrid search. Vector search is implemented at the field level, which means you can build queries that include both vector fields and searchable text fields. The queries execute in parallel and the results are merged into a single response. Optionally, add semantic search (preview) for even more accuracy with L2 reranking using the same language models that power Bing.
>
>Filtered vector search. A query request can include a vector query and a filter expression. Filters apply to text and numeric fields, and are useful for including or excluding search documents based on filter criteria. Although a vector field isn't filterable itself, you can set up a filterable text or numeric field. The search engine processes the filter after the vector query executes, trimming search results from query response.
>
>Vector database. Use Cognitive Search as a vector store to serve as long-term memory or an external knowledge base for Large Language Models (LLMs), or other applications. For example, you can use Azure Cognitive Search as a vector index in an Azure Machine Learning prompt flow for Retrieval Augmented Generation (RAG) applications.