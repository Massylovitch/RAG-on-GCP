project_id              = "tonal-feat-448014-b0"
rag_bucket_name         = "mass-rag-gcp-bucket" #different bucket than the one used for terraform state
location                = "europe-west1"
firestore_database_name = "rag-firestore-db"

enable_iap = false
enable_lb  = false


image = "europe-west1-docker.pkg.dev/tonal-feat-448014-b0/rag-api/gen-ai"

# If enable_iap = true and enable_lb = true
# Set to "internal-and-cloud-load-balancing"
# Else, set to "all"
service_annotations = {
  "run.googleapis.com/ingress" = "all"
}

# If enable_iap = true and enable_lb = true
# Update the domain name
lb_domain = "11-222-333-444.sslip.io"


env_vars = [
  {
    name  = "DEPLOYED_INDEX_ID"
    value = "ragdeployedindex"
  }

]

env_secrets = [
  {
    env_name       = "CONFLUENCE_PRIVATE_API_KEY"
    secret_name    = "CONFLUENCE_PRIVATE_API_KEY"
    secret_version = "latest"
  },
  {
    env_name       = "CONFLUENCE_URL"
    secret_name    = "CONFLUENCE_URL"
    secret_version = "latest"
  },
  {
    env_name       = "CONFLUENCE_EMAIL_ADRESS"
    secret_name    = "CONFLUENCE_EMAIL_ADRESS"
    secret_version = "latest"
  },
  {
    env_name       = "CONFLUENCE_SPACE_NAMES"
    secret_name    = "CONFLUENCE_SPACE_NAMES"
    secret_version = "latest"
  }
]