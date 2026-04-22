## Enterprise Knowledge Base Q&A System (RAG with Amazon Bedrock)
This project implements a Retrieval-Augmented Generation (RAG) system using Amazon Bedrock Knowledge Bases to enable semantic search over internal documents and generate accurate, context-aware responses.

#  Key Features
- Semantic search using vector embeddings
- LLM-based response generation
- Streamlit-based user interface
- Integration with AWS Bedrock Knowledge Base
- Supports natural language queries

#  Architecture
1. Documents stored in Amazon S3
2. Bedrock Knowledge Base creates embeddings
3. Query processed via semantic retrieval
4. LLM generates grounded response

##  Tech Stack
- Python
- Streamlit
- AWS Bedrock
- AWS S3
- boto3

##  How to Run

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m streamlit run app.py
