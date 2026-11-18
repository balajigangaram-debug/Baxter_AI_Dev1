# Agent catalog

All seven agents have deterministic, independently callable starter classes under `src/baxter_ai/agents/implementations.py`. They emit recommendations; no class calls enterprise services or performs external writes.

| Agent | Inputs / outputs | Approval boundary |
|---|---|---|
| Debt profiler | Incidents → debt category counts, prioritized backlog, cadence | Validate classifications and backlog with service owners |
| Ticket triaging | Ticket description/category and candidate history → CI/group/confidence | Human acceptance or override |
| Incident correlator | Candidate incidents → related list and parent suggestion | Human approves links/merges |
| Analytics & insight | Ticket snapshot → aged/orphan counts and triage suggestions | Review before bulk changes |
| MIM assistance | Incident ID/timeline → summary, handoff, communications and RCA drafts | Human validates all drafts and recipients |
| Autonomous SLA | SLA-risk tickets → risk list and recommended action | Escalation/reassignment/swarming require approval |
| Knowledge validation | Article and resolved incidents → review metadata and update draft | Knowledge owner approves publication |

