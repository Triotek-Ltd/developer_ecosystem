"""Doc runtime hooks for api_access_case."""

class DocRuntime:
    doc_key = "api_access_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'review', 'approve', 'reject', 'suspend', 'close', 'archive']
