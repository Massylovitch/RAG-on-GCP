import collections
from typing import List
from langchain.schema import Document


def list_top_k_sources(source_documents, k=3):
    if not source_documents:
        print("""
            No documents were found in Firestore
            Vector Search requested some documents IDs but no one is in Firestore
            The Vector Search should be updated when new contents are added in GCS and Firestore.
            Have a look at `gcloud ai index update` command
        """)
        return ""

    sources = [
        f'[{source_document.metadata["title"]}]({source_document.metadata["source"]})'
        for source_document in source_documents
    ]

    if sources:
        k = min(k, len(sources))
        distinct_sources = list(zip(*collections.Counter(sources).most_common()))[0][:k]
        distinct_sources_str = "  \n- ".join(distinct_sources)
        return f"Source(s):  \n- {distinct_sources_str}"


def get_top_k_urls(source_documents, k=3):
    if not source_documents:
        print("""
            No urls sources retrieved for your question
            It is related to the not found Firestore document
        """)
        return list()

    urls = [source_document.metadata["source"] for source_document in source_documents]
    k = min(k, len(urls))
    distinct_urls = list(zip(*collections.Counter(urls).most_common()))[0][:k]
    return distinct_urls