# Technology stack

| Technology | Intended role | Starter status |
|---|---|---|
| Python | Agent and service logic | Implemented, Python 3.12 |
| AWS Bedrock | Model gateway | Mock port only; AWS setup/model approval required |
| LangGraph | Stateful orchestration | Dependency declared; adapter not yet wired |
| Neo4j / Bloom | Graph and exploration | Schema/mock store; Neo4j driver factory; Bloom deployment required |
| ServiceNow MCP | ITSM/CMDB | Port and mock only |
| Jira / GitHub | Approved metadata sources | Integration requirements only |
| PySpark / Pandas | Larger-scale transformations and analytics | Dependencies declared; pipeline not wired |
| Ragas | RAG evaluation | Dependency declared; datasets/runners not wired |
| Grafana / FinOps | Operations and cost visibility | Design requirement only |
| Docker | Local container runtime | App and Neo4j compose configuration |
