"""Doc runtime hooks for sandbox_usage_record."""

class DocRuntime:
    doc_key = "sandbox_usage_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['record', 'review', 'archive']
