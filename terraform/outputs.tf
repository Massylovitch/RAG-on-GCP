output "index_endpoint_id" {
  value       = google_vertex_ai_index_endpoint.index_endpoint.name
  description = "Vertex AI endpoint ID"
}

output "index_id" {
  value       = google_vertex_ai_index.index.name
  description = "Vertex AI index ID"
}