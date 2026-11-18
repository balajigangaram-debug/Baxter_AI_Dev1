"""Model gateway port; Bedrock adapter is intentionally optional and credential-free."""

from typing import Protocol


class ModelGateway(Protocol):
    def generate(self, prompt: str) -> str: ...


class MockModelGateway:
    def generate(self, prompt: str) -> str:
        return "Mock response. Configure an approved AWS Bedrock model before production use."
