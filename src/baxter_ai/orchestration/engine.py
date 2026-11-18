"""Small deterministic orchestration core; LangGraph can wrap this registry."""

from baxter_ai.agents.registry import AgentRegistry
from baxter_ai.models import AgentRequest, AgentResult


class Orchestrator:
    def __init__(self, registry: AgentRegistry) -> None:
        self.registry = registry

    def invoke(self, agent_name: str, request: AgentRequest) -> AgentResult:
        return self.registry.get(agent_name).run(request)

    def route(self, request: AgentRequest) -> str:
        kind = request.payload.get("workflow", "ticket_triaging")
        routes = {"incident": "ticket_triaging", "service_request": "ticket_triaging",
                  "major_incident": "mim_assistance", "sla": "autonomous_sla",
                  "knowledge": "knowledge_validation", "backlog": "analytics_insight"}
        return routes.get(str(kind), "ticket_triaging")
