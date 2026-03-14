"""Doc runtime hooks for developer_documentation_release."""

class DocRuntime:
    doc_key = "developer_documentation_release"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'publish', 'supersede', 'archive']
