"""Optional Neo4j driver factory. Credentials are read from environment by deployment code."""


def connect(uri: str, username: str, password: str):
    try:
        from neo4j import GraphDatabase
    except ImportError as exc:
        raise RuntimeError("Install the graph extra: uv sync --extra graph") from exc
    return GraphDatabase.driver(uri, auth=(username, password))
