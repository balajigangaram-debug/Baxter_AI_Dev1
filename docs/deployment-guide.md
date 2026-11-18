# Deployment guide

## Local

Use `uv sync --extra dev`, copy `.env.example` to `.env`, then `uv run python -m baxter_ai`. The local demonstration needs no enterprise credentials.

## Docker development

Run `docker compose up --build` after creating `.env`. Neo4j data persists in a named volume. Do not expose this development configuration to an untrusted network.

## Enterprise deployment prerequisites

Private container registry/runtime, approved AWS account and Bedrock model access, secret manager, ServiceNow MCP/API endpoint and scopes, Neo4j cluster and Bloom access, approved Jira/GitHub scopes if needed, network allowlists, IAM roles, durable approval provider, logging/SIEM and Grafana integration, backup/restore and operational support. None are provisioned by this repository.
