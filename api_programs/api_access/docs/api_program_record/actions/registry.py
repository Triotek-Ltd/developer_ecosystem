"""Action registry seed for api_program_record."""

from __future__ import annotations


DOC_ID = "api_program_record"
ALLOWED_ACTIONS = ['create', 'update', 'review', 'activate', 'retire', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['draft', 'active', 'retired'], 'transitions_to': None}, 'update': {'allowed_in_states': ['draft', 'active', 'retired'], 'transitions_to': None}, 'review': {'allowed_in_states': ['draft', 'active', 'retired'], 'transitions_to': None}, 'activate': {'allowed_in_states': ['draft'], 'transitions_to': 'active'}, 'retire': {'allowed_in_states': ['draft', 'active', 'retired'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['draft', 'active', 'retired'], 'transitions_to': 'archived'}}

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
