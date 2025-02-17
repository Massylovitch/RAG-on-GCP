from .embeddings import get_embedding_model
from langchain.chains import RetrievalQA

from llms import get_llm
from prompt import get_prompt
from firestore import get_retriever
from embeddings import get_embedding_model


def get_chain(filters, streaming, streaming_handler):

    if streaming and not streaming_handler:
        raise ValueError("streaming_handler must be provided when streaming is True")
    
    embeddings = get_embedding_model()
    retriever = get_retriever(embeddings=embeddings, filters=filters)
    llm = get_llm(
        streaming=streaming,
        callbacks=streaming_handler
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": get_prompt()},
        return_source_documents=True,
    )

    return qa