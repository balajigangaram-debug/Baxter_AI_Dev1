"""Shared typed request and response contracts."""

from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(slots=True)
class AgentRequest:
    request_id: str
    payload: dict[str, Any]
    actor: str = "local-demo"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class AgentResult:
    request_id: str
    agent: str
    status: str
    output: dict[str, Any]
    confidence: float = 0.0
    requires_approval: bool = False
    created_at: str = field(default_factory=lambda: datetime.now(UTC).isoformat())

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
