from unittest import TestCase
from api.v1.app import app


class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_statusroute(self):
        response = self.app.get('/api/v1/status')
        assert b'{\n  "status": "OK"\n}\n' in response.data
