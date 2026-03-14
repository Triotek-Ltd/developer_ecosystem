"""Doc runtime hooks for sdk_package."""

class DocRuntime:
    doc_key = "sdk_package"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'deprecate', 'archive']
