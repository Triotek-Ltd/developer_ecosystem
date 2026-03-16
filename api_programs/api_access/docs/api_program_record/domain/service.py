"""Business-domain service seed for Api Program Record."""

from __future__ import annotations


ARCHETYPE_PROFILE = {'workflow_profile': {'mode': 'configuration_control', 'case_management': False}, 'reporting_profile': {'supports_snapshots': False, 'supports_outputs': False}, 'integration_profile': {'external_sync_enabled': True}, 'lifecycle_states': ['draft', 'active', 'retired', 'archived'], 'is_transactional': False}

CONTRACT = {'title_field': 'title', 'status_field': 'workflow_state', 'reference_field': 'reference_no', 'required_fields': ['title', 'workflow_state'], 'field_purposes': {'workflow_state': 'lifecycle_state', 'related_partner_api_key': 'relation_collection', 'related_webhook_subscription': 'relation_collection', 'related_api_access_case': 'relation_collection', 'related_developer_documentation_release': 'relation_collection'}, 'search_fields': ['title', 'reference_no', 'description', 'program_code', 'program_name', 'audience_type'], 'list_columns': ['title', 'reference_no', 'workflow_state', 'modified'], 'initial_state': 'draft', 'lifecycle_states': ['draft', 'active', 'retired', 'archived'], 'terminal_states': ['archived'], 'action_targets': {'create': None, 'update': None, 'review': None, 'activate': 'active', 'retire': None, 'archive': 'archived'}}

WORKFLOW_HINTS = {'business_objective': 'define, review, activate, and retire API programs with the right access and partner-governance controls', 'actors': ['API owner', 'security reviewer', 'partner admin'], 'start_condition': 'a partner requests or uses API-program access', 'ordered_steps': ['Create or update the API program.', 'Review the access and governance posture.', 'Activate or retire the program.'], 'primary_actions': ['create', 'update', 'review', 'activate', 'retire'], 'action_actors': {'create': ['API owner'], 'update': ['API owner'], 'review': ['security reviewer'], 'activate': ['API owner', 'security reviewer'], 'retire': ['API owner'], 'archive': ['API owner']}, 'primary_transitions': ['api_program_record: draft -> active -> retired'], 'downstream_effects': ['drives access review, key issuance readiness, and partner integration onboarding']}

SIDE_EFFECT_HINTS = {'downstream_effects': ['drives access review, key issuance readiness, and partner integration onboarding'], 'related_docs': ['partner_api_key', 'webhook_subscription', 'api_access_case', 'developer_documentation_release'], 'action_targets': {'create': None, 'update': None, 'review': None, 'activate': 'active', 'retire': None, 'archive': 'archived'}, 'action_side_effects_file': 'side_effects.json'}

class DomainService:
    doc_id = "api_program_record"
    archetype = "configuration"
    doc_kind = "configuration"

    def required_fields(self) -> list[str]:
        return CONTRACT.get("required_fields", [])

    def state_field(self) -> str | None:
        return CONTRACT.get("status_field")

    def default_state(self) -> str | None:
        return CONTRACT.get("initial_state")

    def list_columns(self) -> list[str]:
        return CONTRACT.get("list_columns", [])

    def validate_invariants(self, payload: dict, *, partial: bool = False) -> dict:
        if partial:
            required_scope = [field for field in self.required_fields() if field in payload]
        else:
            required_scope = self.required_fields()
        missing_fields = [field for field in required_scope if not payload.get(field)]
        if missing_fields:
            raise ValueError(f"Missing required business fields: {', '.join(missing_fields)}")
        state_field = self.state_field()
        allowed_states = set(CONTRACT.get("lifecycle_states", []))
        if state_field and payload.get(state_field) and allowed_states and payload[state_field] not in allowed_states:
            raise ValueError(f"Invalid state '{payload[state_field]}' for {state_field}")
        return payload

    def prepare_create_payload(self, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        state_field = self.state_field()
        if state_field and not payload.get(state_field) and self.default_state():
            payload[state_field] = self.default_state()
        title_field = CONTRACT.get("title_field")
        reference_field = CONTRACT.get("reference_field")
        if title_field and not payload.get(title_field) and reference_field and payload.get(reference_field):
            payload[title_field] = str(payload[reference_field])
        payload = self.validate_invariants(payload)
        return payload

    def after_create(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def prepare_update_payload(self, instance, payload: dict, context: dict | None = None) -> dict:
        payload = dict(payload)
        payload = self.validate_invariants(payload, partial=True)
        return payload

    def after_update(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        return serialized_data

    def after_action(
        self,
        instance,
        action_id: str,
        payload: dict,
        action_result: dict,
        context: dict | None = None,
    ) -> dict:
        return {
            "updates": {},
            "side_effects": [],
        }

    def shape_retrieve_data(self, instance, serialized_data: dict, context: dict | None = None) -> dict:
        serialized_data.setdefault("_business_capabilities", self.business_capabilities())
        return serialized_data

    def workflow_objective(self) -> str | None:
        return WORKFLOW_HINTS.get("business_objective")

    def side_effect_hints(self) -> dict:
        return SIDE_EFFECT_HINTS

    def business_capabilities(self) -> dict:
        return {
            **ARCHETYPE_PROFILE,
            "required_fields": self.required_fields(),
            "state_field": self.state_field(),
            "default_state": self.default_state(),
        }
