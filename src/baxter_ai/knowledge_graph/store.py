"""In-memory graph adapter for local execution and tests."""

from baxter_ai.knowledge_graph.schema import validate_node


class MemoryGraph:
    def __init__(self) -> None:
        self.nodes: dict[tuple[str, str], dict[str, object]] = {}
        self.edges: set[tuple[str, str, str, str, str]] = set()

    def upsert_node(self, node: dict[str, object]) -> None:
        validate_node(node)
        key = (str(node["label"]), str(node["id"]))
        self.nodes[key] = dict(node)

    def add_edge(self, source: tuple[str, str], relationship: str, target: tuple[str, str]) -> None:
        self.edges.add((*source, relationship, *target))
