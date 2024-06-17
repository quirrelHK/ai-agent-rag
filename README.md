# AI-Agent-RAG

A RAG react agent. This agent integrates Retrieval-Augmented Generation (RAG) capabilities with ReAct (Reasoning and Acting) architecture, providing query handling and data retrieval from diverse sources like CSV files and PDFs. The agent leverages the `mixtral-8x7b-32768` model from GROQ for efficient inference.

## How to setup
### Clone this repo
```console
https://github.com/quirrelHK/ai-agent-rag.git

cd ai-agent-rag
```

### Add a .env file with environment variables
```
HUGGINGFACE_API_TOKEN=<your-huggingface-api-token>
GROQ_API_KEY=<your-GROQ-api-key>
```

### Create and activate a virtual environment
```console
python -m venv base

base\Scripts\activate.bat
```

### Install the requirements
```console
pip install -r requirements.txt
```

### Run the tool
```bash
python main.py
```