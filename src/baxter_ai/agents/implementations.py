"""Seven deterministic mock-first agent starters."""

from collections import Counter
from typing import Any

from baxter_ai.agents.base import BaseAgent
from baxter_ai.models import AgentRequest


class DebtProfilerAgent(BaseAgent):
    name = "debt_profiler"

    def execute(self, request: AgentRequest) -> dict[str, Any]:
        incidents = request.payload.get("incidents", [])
        counts = Counter(str(item.get("debt_type", "Knowledge")) for item in incidents if isinstance(item, dict))
        return {"classified": dict(counts), "backlog": sorted(counts, key=counts.get, reverse=True),
                "cadence": request.payload.get("cadence", "weekly"), "confidence": 0.5}


class TicketTriagingAgent(BaseAgent):
    name = "ticket_triaging"

    def execute(self, request: AgentRequest) -> dict[str, Any]:
        text = str(request.payload.get("description", "")).lower()
        candidates = request.payload.get("similar_closed_tickets", [])
        category = str(request.payload.get("category", "service_request"))
        group = "Messaging Support" if any(word in text for word in ("email", "mail", "outlook")) else "Service Desk"
        return {"configuration_item": request.payload.get("configuration_item", "unresolved"),
                "assignment_group": group, "category": category, "similar_ticket_count": len(candidates),
                "confidence": 0.62 if text else 0.2, "human_override_supported": True}


class IncidentCorrelatorAgent(BaseAgent):
    name = "incident_correlator"

    def execute(self, request: AgentRequest) -> dict[str, Any]:
        matches = request.payload.get("candidate_incidents", [])
        return {"related_incidents": matches, "proposed_parent": matches[0] if matches else None,
                "merge_requires_approval": True, "confidence": 0.4 if matches else 0.0}


class AnalyticsInsightAgent(BaseAgent):
    name = "analytics_insight"

    def execute(self, request: AgentRequest) -> dict[str, Any]:
        tickets = request.payload.get("tickets", [])
        aged = [t for t in tickets if isinstance(t, dict) and t.get("aged")]
        orphaned = [t for t in tickets if isinstance(t, dict) and not t.get("assignment_group")]
        return {"ticket_count": len(tickets), "aged_count": len(aged), "orphaned_count": len(orphaned),
                "bulk_triage_recommendations": [t.get("id") for t in orphaned], "confidence": 0.8}


class MIMAssistanceAgent(BaseAgent):
    name = "mim_assistance"

    def execute(self, request: AgentRequest) -> dict[str, Any]:
        incident = request.payload.get("incident_id", "unspecified")
        updates = request.payload.get("timeline", [])
        return {"incident_id": incident, "summary": f"Major incident {incident}: {len(updates)} timeline updates recorded.",
                "handoff": "Review current impact, mitigations, owners, and next update time.",
                "stakeholder_draft": "Draft only; validate audience and facts before sending.",
                "rca_draft": "Root cause analysis pending human review.", "timeline": updates,
                "requires_approval": True, "confidence": 0.3}


class AutonomousSlaAgent(BaseAgent):
    name = "autonomous_sla"

    def execute(self, request: AgentRequest) -> dict[str, Any]:
        tickets = request.payload.get("tickets", [])
        at_risk = [t.get("id") for t in tickets if isinstance(t, dict) and t.get("sla_risk")]
        return {"at_risk_ticket_ids": at_risk, "recommended_action": "escalate_or_swarm" if at_risk else "monitor",
                "requires_approval": True, "confidence": 0.5}


class KnowledgeValidationAgent(BaseAgent):
    name = "knowledge_validation"

    def execute(self, request: AgentRequest) -> dict[str, Any]:
        article = request.payload.get("article", {})
        resolved = request.payload.get("resolved_incidents", [])
        return {"article_id": article.get("id") if isinstance(article, dict) else None,
                "resolved_incident_count": len(resolved), "stale_or_conflicting": [],
                "draft_update": "Compare validated resolution steps with approved article content.",
                "publication_requires_owner_approval": True, "confidence": 0.25}
