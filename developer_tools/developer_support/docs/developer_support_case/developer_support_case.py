"""Doc runtime hooks for developer_support_case."""

class DocRuntime:
    doc_key = "developer_support_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'investigate', 'resolve', 'escalate', 'close', 'archive']
