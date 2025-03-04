import os
from ast import literal_eval
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv(), override=True)

# GCP
PROJECT_ID = os.environ['PROJECT_ID']
REGION = os.environ['REGION']


# Firestore
FIRESTORE_DATABASE_NAME = os.environ['FIRESTORE_DATABASE_NAME']
FIRESTORE_COLLECTION_NAME = "gdrive_docs"

# Vertex Search
INDEX_ENDPOINT_ID = os.environ["INDEX_ENDPOINT_ID"]
DEPLOYED_INDEX_ID = os.environ["DEPLOYED_INDEX_ID"]