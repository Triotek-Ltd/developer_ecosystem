"""Doc runtime hooks for webhook_subscription."""

class DocRuntime:
    doc_key = "webhook_subscription"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'verify', 'activate', 'disable', 'rotate_secret', 'archive']
