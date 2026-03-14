"""Action registry seed for partner_api_key."""

from __future__ import annotations


DOC_ID = "partner_api_key"
ALLOWED_ACTIONS = ['create', 'issue', 'activate', 'rotate', 'suspend', 'revoke', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['requested', 'issued', 'active', 'suspended', 'revoked'], 'transitions_to': None}, 'issue': {'allowed_in_states': ['requested', 'issued', 'active', 'suspended', 'revoked'], 'transitions_to': 'issued'}, 'activate': {'allowed_in_states': ['requested'], 'transitions_to': 'active'}, 'rotate': {'allowed_in_states': ['requested', 'issued', 'active', 'suspended', 'revoked'], 'transitions_to': None}, 'suspend': {'allowed_in_states': ['requested', 'issued', 'active', 'suspended', 'revoked'], 'transitions_to': None}, 'revoke': {'allowed_in_states': ['requested', 'issued', 'active', 'suspended', 'revoked'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['requested', 'issued', 'active', 'suspended', 'revoked'], 'transitions_to': 'archived'}}

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
