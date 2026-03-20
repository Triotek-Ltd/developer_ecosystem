"""Action handler seed for api_program_record:retire."""

from __future__ import annotations

from typing import Any, cast


DOC_ID = "api_program_record"
ACTION_ID = "retire"
ACTION_RULE: dict[str, Any] = {'allowed_in_states': ['draft', 'active', 'retired'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'business_objective': 'define, review, activate, and retire API programs with the right access and partner-governance controls', 'actors': ['API owner', 'security reviewer', 'partner admin'], 'start_condition': 'a partner requests or uses API-program access', 'ordered_steps': ['Create or update the API program.', 'Review the access and governance posture.', 'Activate or retire the program.'], 'primary_actions': ['create', 'update', 'review', 'activate', 'retire'], 'action_actors': {'create': ['API owner'], 'update': ['API owner'], 'review': ['security reviewer'], 'activate': ['API owner', 'security reviewer'], 'retire': ['API owner'], 'archive': ['API owner']}, 'primary_transitions': ['api_program_record: draft -> active -> retired'], 'downstream_effects': ['drives access review, key issuance readiness, and partner integration onboarding']}

ACTION_CONTRACT: dict[str, Any] = {'rule': {'allowed_in_states': ['draft', 'active', 'retired'], 'transitions_to': None}, 'requires_action_comment': False, 'requires_reason_for_change': False, 'requires_evidence': False, 'is_disposition_action': False, 'creates_submission_snapshot': False, 'creates_official_copy': False, 'requires_signature': False}

def handle_retire(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = cast(str | None, ACTION_RULE.get("transitions_to"))
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "action_contract": ACTION_CONTRACT,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
