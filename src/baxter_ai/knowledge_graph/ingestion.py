"""CMDB hydration that persists identifiers and approved metadata only."""

from baxter_ai.integrations.servicenow import ServiceNowPort
from baxter_ai.knowledge_graph.store import MemoryGraph


def hydrate_cmdb(source: ServiceNowPort, graph: MemoryGraph) -> int:
    count = 0
    for row in source.get_cmdb_items():
        node = {"label": str(row.get("class", "ConfigurationItem")), "id": row["sys_id"]}
        if row.get("environment"):
            node["environment"] = row["environment"]
        graph.upsert_node(node)
        count += 1
    return count
