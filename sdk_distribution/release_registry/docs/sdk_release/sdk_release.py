"""Doc runtime hooks for sdk_release."""

class DocRuntime:
    doc_key = "sdk_release"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'approve', 'publish', 'supersede', 'archive']
