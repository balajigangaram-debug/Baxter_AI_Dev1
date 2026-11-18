# Governance and security

- Start in Assist mode; humans make operational decisions.
- Require review for external communication, merge, publication, reassignment, escalation, and any other sensitive write.
- Keep the kill switch available and test its behavior.
- Use enterprise IAM/RBAC and least-privilege service identities; the local role check is not IAM.
- Store secrets in an approved manager; `.env` is local-only and ignored by Git.
- Validate and minimize inputs/outputs; keep graph data metadata-only with no employee nodes or PII.
- Audit request IDs, agent names, status, and decision metadata; avoid recording source text or secrets.
- Evaluate models and workflows on approved de-identified datasets before pilots and autonomy.
- Define retention, incident response, change control, model risk tiers, and human override monitoring with governance owners.

These patterns are not a compliance certification or a substitute for Baxter/TCS policies.
