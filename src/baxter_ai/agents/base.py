"""Agent protocol and shared execution checks."""

from abc import ABC, abstractmethod

from baxter_ai.audit import record
from baxter_ai.governance import GovernancePolicy
from baxter_ai.models import AgentRequest, AgentResult


class BaseAgent(ABC):
    name = "base"

    def __init__(self, policy: GovernancePolicy | None = None) -> None:
        self.policy = policy or GovernancePolicy()

    def run(self, request: AgentRequest) -> AgentResult:
        if self.policy.kill_switch:
            return AgentResult(request.request_id, self.name, "blocked", {"reason": "kill_switch"})
        output = self.execute(request)
        requires_approval = bool(output.pop("requires_approval", False)) or self.policy.approvals_required
        result = AgentResult(
            request.request_id,
            self.name,
            "needs_approval" if requires_approval else "completed",
            output,
            float(output.get("confidence", 0.0)),
            requires_approval,
        )
        record("agent.completed", request_id=request.request_id, agent=self.name, status=result.status)
        return result

    @abstractmethod
    def execute(self, request: AgentRequest) -> dict[str, object]:
        """Return a bounded recommendation, never perform a real external mutation."""
