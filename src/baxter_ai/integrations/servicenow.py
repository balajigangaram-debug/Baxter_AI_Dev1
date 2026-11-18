"""ServiceNow integration port. Replace the mock with an approved MCP/API client."""

from typing import Protocol


class ServiceNowPort(Protocol):
    def get_cmdb_items(self) -> list[dict[str, object]]: ...

    def get_closed_tickets(self, limit: int = 100) -> list[dict[str, object]]: ...


class MockServiceNow:
    def get_cmdb_items(self) -> list[dict[str, object]]:
        return [{"sys_id": "demo-ci-1", "class": "ConfigurationItem", "environment": "test",
                 "support_group_id": "group-1"}]

    def get_closed_tickets(self, limit: int = 100) -> list[dict[str, object]]:
        return [{"sys_id": "demo-ticket-1", "category": "incident", "assignment_group_id": "group-1"}][:limit]
