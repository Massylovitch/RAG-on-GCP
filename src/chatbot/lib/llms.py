from langchain_google_vertexai import ChatVertexAI
from config import REGION


def get_llm(callbacks=None, streaming=False, max_output_tokens=512, temperature=0.1):
    llm = ChatVertexAI(
        model="chat-bison",
        location=REGION,
        temperature=temperature,
        streaming=streaming,
        callbacks=callbacks,
        max_output_tokens=max_output_tokens
    )
    return llm