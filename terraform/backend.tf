terraform {
  backend "gcs" {
    bucket = "tfstate_bucket_rag_on_gcp"
    prefix = "terraform/tf-rag-infra"
  }
}