"""Doc runtime hooks for sandbox_account."""

class DocRuntime:
    doc_key = "sandbox_account"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'provision', 'activate', 'suspend', 'expire', 'archive']
