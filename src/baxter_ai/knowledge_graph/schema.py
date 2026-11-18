"""Allowlisted graph labels and relationships; deliberately excludes people and PII."""

NODE_LABELS = ("ConfigurationItem", "Application", "Infrastructure", "Server", "Environment",
               "Epic", "Feature", "UserGroup", "AccessGroup")
RELATIONSHIPS = ("DEPENDS_ON", "RUNS_IN", "SUPPORTS", "OWNED_BY", "BELONGS_TO", "RELATED_TO")

CONSTRAINTS = """
CREATE CONSTRAINT ci_id IF NOT EXISTS FOR (n:ConfigurationItem) REQUIRE n.id IS UNIQUE;
CREATE CONSTRAINT app_id IF NOT EXISTS FOR (n:Application) REQUIRE n.id IS UNIQUE;
"""


def validate_node(node: dict[str, object]) -> None:
    if node.get("label") not in NODE_LABELS:
        raise ValueError("Node label is not allowlisted")
    forbidden = {"name", "email", "employee_id", "phone", "description", "ticket_text"}
    if forbidden.intersection(node):
        raise ValueError("PII or free-text fields are not accepted in graph metadata")
    if not node.get("id"):
        raise ValueError("Node requires a stable source identifier")
