"""Action handler seed for partner_api_key:revoke."""

from __future__ import annotations


DOC_ID = "partner_api_key"
ACTION_ID = "revoke"
ACTION_RULE = {'allowed_in_states': ['requested', 'issued', 'active', 'suspended', 'revoked'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['api_program_record', 'api_access_case', 'sandbox_account'], 'borrowed_fields': ['program scope', 'access policy from api_program_record'], 'inferred_roles': ['compliance officer', 'case owner']}, 'actors': ['compliance officer', 'case owner'], 'action_actors': {'create': ['compliance officer'], 'issue': ['case owner'], 'activate': ['case owner'], 'archive': ['case owner']}}

def handle_revoke(payload: dict, context: dict | None = None) -> dict:
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
