"""Doc runtime hooks for api_program_record."""

class DocRuntime:
    doc_key = "api_program_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'activate', 'retire', 'archive']
