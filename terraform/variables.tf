variable "project_id" {
  description = "The project ID to deploy to"
  type        = string
}

variable "rag_bucket_name" {
  description = "RAG GCS bucket"
  type        = string
}

variable "location" {
  description = "Ressources service deployment location"
  type        = string
  default     = "europe-west1"
}

variable "image" {
  description = "GCR hosted image URL to deploy"
  type        = string
}

variable "service_annotations" {
  type        = map(string)
  description = "Annotations to the service. Acceptable values all, internal, internal-and-cloud-load-balancing"
  default = {
    "run.googleapis.com/ingress" = "all"
  }
}

variable "template_annotations" {
  type        = map(string)
  description = "Annotations to the container metadata including VPC Connector and SQL."
  default = {
    "run.googleapis.com/client-name"   = "terraform"
    "generated-by"                     = "terraform"
    "autoscaling.knative.dev/maxScale" = 2
    "autoscaling.knative.dev/minScale" = 1
  }
}

variable "container_concurrency" {
  type        = number
  description = "Concurrent request limits to the service"
  default     = null
}

variable "timeout_seconds" {
  type        = number
  description = "Timeout for each request"
  default     = 120
}

variable "container_command" {
  type        = list(string)
  description = "Leave blank to use the ENTRYPOINT command defined in the container image, include these only if image entrypoint should be overwritten"
  default     = []
}

variable "run_service_account_id" {
  type        = string
  description = "Service Account ID"
  default     = "rag-api-sa"
}

variable "members" {
  type        = list(string)
  description = "Users/SAs to be given invoker access to the service"
  default     = []
}

variable "oauth_client_display_name" {
  type        = string
  description = "Display name given to the OAuth client."
  default     = "rag-api"
}

variable "oauth_brand_name" {
  type        = string
  description = "Identifier of the brand to which this client is attached to. The format is projects/{project_number}/brands/{brand_id}/identityAwareProxyClients/{client_id}."
  default     = null
}

variable "enable_iap" {
  type        = bool
  description = "If True it will create OAuth2 client_id/secret and enable IAP on the loadbalancer"
  default     = false
}

variable "iap_http_accessor" {
  type        = list(string)
  description = "IAP members allowed to access (asign roles/iap.httpsResourceAccessor)"
  default     = ["allAuthenticatedUsers"]
}

variable "firestore_region" {
  type        = string
  description = "The region to create the Firestore database in. See https://cloud.google.com/firestore/docs/locations?"
  default     = "europe-west1"
}

variable "firestore_database_name" {
  type        = string
  description = "Identifier of the brand to which this client is attached to. The format is projects/{project_number}/brands/{brand_id}/identityAwareProxyClients/{client_id}."
  default     = "rag-firestore-db"
}

variable "env_vars" {
  type = list(object({
    value = string
    name  = string
  }))
  description = "Cloud RUN Environment variables (cleartext)"
  default     = []
}


# Cloud functions variables

variable "cloud_functions_name" {
  type    = string
  default = "rag-update-active-pages"
}

variable "cloud_functions_topic_name" {
  type    = string
  default = "rag-trigger-update-active-pages"
}

variable "cloud_functions_scheduler_name" {
  type    = string
  default = "rag-invoke-update-pages-function"
}

variable "scheduler" {
  type    = string
  default = "0 0 * * *" # every day at OO:00 https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules
}

variable "functions_service_account_name" {
  type    = string
  default = "rag-functions-sa"
}

variable "cloudfunctions_sa_roles" {
  type        = list(string)
  description = "Roles to apply to cloud functions sa"
  default = [
    "roles/storage.objectUser",
    "roles/iam.serviceAccountUser",
    "roles/datastore.user",
    "roles/secretmanager.secretAccessor",
    "roles/aiplatform.admin",
    "roles/cloudfunctions.serviceAgent"
  ]
}

variable "functions_main_file" {
  type    = string
  default = "load_data.py"
}

variable "functions_output_zip_path" {
  type    = string
  default = "/tmp/rag_functions.zip"
}

variable "funtions_source_dir" {
  type    = string
  default = "../src/upload_data"
}