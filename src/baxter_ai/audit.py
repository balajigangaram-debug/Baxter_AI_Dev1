"""Structured, metadata-only audit events."""

import json
import logging
from typing import Any

logger = logging.getLogger("baxter_ai.audit")


def record(event: str, **fields: Any) -> None:
    # Callers must not pass ticket descriptions, credentials, PII, or source records.
    logger.info(json.dumps({"event": event, **fields}, default=str, sort_keys=True))
