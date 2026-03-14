"""Doc runtime hooks for partner_api_key."""

class DocRuntime:
    doc_key = "partner_api_key"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'issue', 'activate', 'rotate', 'suspend', 'revoke', 'archive']
