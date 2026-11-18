# Contributing

Keep agents independently testable and integrations behind ports. Use typed contracts, deterministic mock examples, and metadata-only fixtures. Do not commit customer records, PII, credentials, or proprietary source documents. Document assumptions and obtain domain-owner review for workflow behavior and ontology changes.

Run `uv sync --extra dev`, `uv run pytest`, and `uv run ruff check .` before proposing changes. Production adapters require security, platform, and governance review.
