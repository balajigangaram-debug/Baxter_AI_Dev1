"""In-memory approval gate for demonstrations; production requires durable IAM-backed workflow."""

class ApprovalQueue:
    def __init__(self) -> None:
        self._pending: dict[str, str] = {}

    def submit(self, action_id: str, summary: str) -> None:
        if action_id in self._pending:
            raise ValueError("Action is already pending")
        self._pending[action_id] = summary

    def decide(self, action_id: str, approved: bool) -> bool:
        if action_id not in self._pending:
            raise KeyError(action_id)
        del self._pending[action_id]
        return approved
