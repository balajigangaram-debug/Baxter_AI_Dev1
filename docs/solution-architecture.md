# Solution architecture

The starter separates agent logic, orchestration, governance, adapters, and graph context. The local runtime uses deterministic mocks. Production path: approved source adapters → metadata validation/transformation → Neo4j graph → agent context retrieval → Bedrock/model gateway → recommendations → human approval → ITSM action. Treat this as a target pattern pending confirmation against the source PDF and enterprise architecture.

The graph stores stable identifiers and approved operational metadata only. No PII, employee nodes, ticket descriptions, or free text should be hydrated. Validate every source contract and enforce privacy controls at ingestion and storage boundaries.
