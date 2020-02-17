import unittest
from app import app


class test_home(unittest.TestCase):

    def test_get(self):
        app = app.test_client()
        response = app.get('/')
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
