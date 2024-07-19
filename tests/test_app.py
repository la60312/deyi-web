import unittest
from demo import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_home(self):
        # sends HTTP GET request to the application on the specified path
        result = self.app.get('/')

        # assert the response data
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, b'Hello, World!')

if __name__ == "__main__":
    unittest.main()
