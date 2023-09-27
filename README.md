# AOAI_VectorDB_CognitiveSearch
> Quick demo: Azure OpenAI integration with Vector Database and Cognitive Search

## Deployment steps:

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

## Tools: Azure Open AI Azure Cognitive Search Langchain Streamlit

- Questions:
what is Azure OpenAI Service?
Which regions does the service support?

All the data is coming from this repo: https://github.com/microsoft/azure-openai-in-a-day-workshop/tree/main/data/qna

## Story
