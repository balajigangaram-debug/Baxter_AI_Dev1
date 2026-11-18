import pytest

from baxter_ai.agents.registry import build_default_registry
from baxter_ai.integrations.servicenow import MockServiceNow
from baxter_ai.knowledge_graph.ingestion import hydrate_cmdb
from baxter_ai.knowledge_graph.store import MemoryGraph
from baxter_ai.models import AgentRequest
from baxter_ai.orchestration.engine import Orchestrator


def test_mock_cmdb_hydration():
    graph = MemoryGraph()
    assert hydrate_cmdb(MockServiceNow(), graph) == 1
    assert ("ConfigurationItem", "demo-ci-1") in graph.nodes


def test_graph_rejects_free_text_fields():
    with pytest.raises(ValueError):
        MemoryGraph().upsert_node({"label": "Server", "id": "1", "description": "sensitive"})


def test_orchestrator_routes_major_incident():
    orchestrator = Orchestrator(build_default_registry())
    request = AgentRequest("r", {"workflow": "major_incident"})
    assert orchestrator.route(request) == "mim_assistance"
