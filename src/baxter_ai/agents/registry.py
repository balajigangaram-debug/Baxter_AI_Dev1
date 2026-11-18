"""Agent registry with explicit names and no dynamic code loading."""

from baxter_ai.agents.implementations import (
    AnalyticsInsightAgent,
    AutonomousSlaAgent,
    DebtProfilerAgent,
    IncidentCorrelatorAgent,
    KnowledgeValidationAgent,
    MIMAssistanceAgent,
    TicketTriagingAgent,
)


class AgentRegistry:
    def __init__(self) -> None:
        self._agents = {}

    def register(self, agent) -> None:
        if agent.name in self._agents:
            raise ValueError(f"Agent already registered: {agent.name}")
        self._agents[agent.name] = agent

    def get(self, name: str):
        try:
            return self._agents[name]
        except KeyError as exc:
            raise KeyError(f"Unknown agent: {name}") from exc

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._agents))


def build_default_registry() -> AgentRegistry:
    registry = AgentRegistry()
    for agent in (DebtProfilerAgent(), TicketTriagingAgent(), IncidentCorrelatorAgent(),
                  AnalyticsInsightAgent(), MIMAssistanceAgent(), AutonomousSlaAgent(),
                  KnowledgeValidationAgent()):
        registry.register(agent)
    return registry
