from langchain_google_vertexai import VertexAIEmbeddings


def get_embedding_model():
    embeddings = VertexAIEmbeddings(model_name="text-embedding-004")
    return embeddings
