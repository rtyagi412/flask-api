import unittest
from app import app

class FlaskApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_data(self):
        response = self.app.get('/data')
        self.assertEqual(response.status_code, 200)  # Check for success status code
        data = response.get_json()
        self.assertIn('name', data)  # Check if 'name' key exists in response
        self.assertEqual(data['name'], 'Flask API example')

    def test_invalid_route(self):
        response = self.app.get('/invalid-route')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()