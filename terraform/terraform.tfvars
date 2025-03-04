project_id              = "tonal-feat-448014-b0"
rag_bucket_name         = "mass-rag-gcp-bucket" #different bucket than the one used for terraform state
location                = "europe-west1"
firestore_database_name = "rag-firestore-db"

enable_iap = false

image = "europe-west1-docker.pkg.dev/tonal-feat-448014-b0/rag-api/gen-ai"

# If enable_iap = true
# Set to "internal-and-cloud-load-balancing"
# Else, set to "all"
service_annotations = {
  "run.googleapis.com/ingress" = "all"
}

env_vars = [
  {
    name  = "DEPLOYED_INDEX_ID"
    value = "ragdeployedindex"
  }

]