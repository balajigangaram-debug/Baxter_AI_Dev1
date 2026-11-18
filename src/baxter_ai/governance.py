"""Small policy primitives; production authorization belongs to enterprise IAM."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GovernancePolicy:
    kill_switch: bool = False
    approvals_required: bool = True
    allowed_roles: tuple[str, ...] = ("operator", "approver", "admin")

    def authorize(self, role: str) -> bool:
        return not self.kill_switch and role in self.allowed_roles

    def needs_approval(self, action_risk: str) -> bool:
        return self.approvals_required or action_risk in {"high", "critical"}
