"""Action registry seed for api_access_case."""

from __future__ import annotations


DOC_ID = "api_access_case"
ALLOWED_ACTIONS = ['create', 'assign', 'review', 'approve', 'reject', 'suspend', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['opened', 'in_review', 'approved', 'rejected', 'suspended'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['opened', 'in_review', 'approved', 'rejected', 'suspended'], 'transitions_to': 'in_review'}, 'review': {'allowed_in_states': ['opened', 'in_review', 'approved', 'rejected', 'suspended'], 'transitions_to': 'in_review'}, 'approve': {'allowed_in_states': ['opened', 'in_review', 'approved', 'rejected', 'suspended'], 'transitions_to': 'approved'}, 'reject': {'allowed_in_states': ['opened', 'in_review', 'approved', 'rejected', 'suspended'], 'transitions_to': 'rejected'}, 'suspend': {'allowed_in_states': ['opened', 'in_review', 'approved', 'rejected', 'suspended'], 'transitions_to': None}, 'close': {'allowed_in_states': ['opened', 'in_review', 'approved', 'rejected', 'suspended'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['opened', 'in_review', 'approved', 'rejected', 'suspended'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
