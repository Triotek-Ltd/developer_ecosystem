"""Action handler seed for sandbox_account:activate."""

from __future__ import annotations


DOC_ID = "sandbox_account"
ACTION_ID = "activate"
ACTION_RULE = {'allowed_in_states': ['requested'], 'transitions_to': 'active'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['sandbox_usage_record', 'developer_test_run', 'developer_support_case', 'partner_api_key'], 'borrowed_fields': ['developer/program access context from partner_api_key or developer account records'], 'inferred_roles': ['case owner']}, 'actors': ['case owner'], 'action_actors': {'create': ['case owner'], 'activate': ['case owner'], 'archive': ['case owner']}}

def handle_activate(payload: dict, context: dict | None = None) -> dict:
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
