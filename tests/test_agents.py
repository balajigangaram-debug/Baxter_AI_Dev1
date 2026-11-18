from baxter_ai.agents.registry import build_default_registry
from baxter_ai.models import AgentRequest


def test_all_seven_agents_are_registered_and_callable():
    registry = build_default_registry()
    assert len(registry.names()) == 7
    for name in registry.names():
        result = registry.get(name).run(AgentRequest(f"req-{name}", {}))
        assert result.agent == name
        assert result.status in {"completed", "needs_approval"}


def test_ticket_triage_recommends_group_from_mock_text():
    agent = build_default_registry().get("ticket_triaging")
    result = agent.run(AgentRequest("r1", {"description": "Email is down"}))
    assert result.output["assignment_group"] == "Messaging Support"


def test_kill_switch_blocks_agent():
    from baxter_ai.agents.implementations import TicketTriagingAgent
    from baxter_ai.governance import GovernancePolicy

    result = TicketTriagingAgent(GovernancePolicy(kill_switch=True)).run(AgentRequest("r", {}))
    assert result.status == "blocked"
