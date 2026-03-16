"""Action handler seed for api_program_record:update."""

from __future__ import annotations


DOC_ID = "api_program_record"
ACTION_ID = "update"
ACTION_RULE = {'allowed_in_states': ['draft', 'active', 'retired'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'define, review, activate, and retire API programs with the right access and partner-governance controls', 'actors': ['API owner', 'security reviewer', 'partner admin'], 'start_condition': 'a partner requests or uses API-program access', 'ordered_steps': ['Create or update the API program.', 'Review the access and governance posture.', 'Activate or retire the program.'], 'primary_actions': ['create', 'update', 'review', 'activate', 'retire'], 'action_actors': {'create': ['API owner'], 'update': ['API owner'], 'review': ['security reviewer'], 'activate': ['API owner', 'security reviewer'], 'retire': ['API owner'], 'archive': ['API owner']}, 'primary_transitions': ['api_program_record: draft -> active -> retired'], 'downstream_effects': ['drives access review, key issuance readiness, and partner integration onboarding']}

def handle_update(payload: dict, context: dict | None = None) -> dict:
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
