import streamlit as st
import boto3

# Create Bedrock client
client = boto3.client("bedrock-agent-runtime", region_name="us-east-1")

st.title("Enterprise Knowledge Base Q&A")

query = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if query:
        try:
            response = client.retrieve_and_generate(
                input={"text": query},
                retrieveAndGenerateConfiguration={
                    "type": "KNOWLEDGE_BASE",
                    "knowledgeBaseConfiguration": {
                        "knowledgeBaseId": "XQV3TIZWLH",
                        "modelArn": "amazon.nova-micro-v1:0"
                    }
                }
            )

            answer = response['output']['text']
            st.success(answer)

        except Exception as e:
            st.error(f"Error: {e}")