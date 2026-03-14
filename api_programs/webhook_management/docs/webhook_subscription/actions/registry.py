"""Action registry seed for webhook_subscription."""

from __future__ import annotations


DOC_ID = "webhook_subscription"
ALLOWED_ACTIONS = ['create', 'verify', 'activate', 'disable', 'rotate_secret', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'verified', 'active', 'disabled'], 'transitions_to': None}, 'verify': {'allowed_in_states': ['draft', 'verified', 'active', 'disabled'], 'transitions_to': None}, 'activate': {'allowed_in_states': ['draft'], 'transitions_to': 'active'}, 'disable': {'allowed_in_states': ['draft', 'verified', 'active', 'disabled'], 'transitions_to': None}, 'rotate_secret': {'allowed_in_states': ['draft', 'verified', 'active', 'disabled'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'verified', 'active', 'disabled'], 'transitions_to': 'archived'}}

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
