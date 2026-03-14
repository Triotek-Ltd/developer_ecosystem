"""Doc runtime hooks for developer_test_run."""

class DocRuntime:
    doc_key = "developer_test_run"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'queue', 'start', 'pass', 'fail', 'archive']
