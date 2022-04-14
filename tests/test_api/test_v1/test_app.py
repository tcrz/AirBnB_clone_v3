from unittest import TestCase
from api.v1.app import app


class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_statusroute(self):
        """tests the status route returns JSON-formatted
        response correctly"""
        response = self.app.get('/api/v1/status')
        assert b'{\n  "status": "OK"\n}\n' in response.data

    def test_404error(self):
        """tests the handing of 404 error returns JSON-formatted
        status code response"""
        response = self.app.get('/api/v1/nop')
        self.assertEqual(b'{\n  "error": "Not found"\n}\n', response.data)
