"""Action handler seed for sandbox_usage_record:review."""

from __future__ import annotations


DOC_ID = "sandbox_usage_record"
ACTION_ID = "review"
ACTION_RULE = {'allowed_in_states': ['active'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['sandbox_account', 'developer_test_run'], 'borrowed_field_context': ['account tier', 'scope from sandbox_account'], 'inferred_roles': ['Finance Officer']}, 'actors': ['Finance Officer'], 'action_actors': {'record': ['Finance Officer'], 'review': ['Finance Officer'], 'archive': ['Finance Officer']}}

def handle_review(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
