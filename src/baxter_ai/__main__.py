"""Run a local demonstration without enterprise credentials."""

from baxter_ai.agents.registry import build_default_registry
from baxter_ai.models import AgentRequest


def main() -> None:
    registry = build_default_registry()
    result = registry.get("ticket_triaging").run(
        AgentRequest("demo-1", {"description": "Email service unavailable", "category": "incident"})
    )
    print(result.to_dict())


if __name__ == "__main__":
    main()
