import unittest
from app import app
from flask import json


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_endpoint(self):
        with open("Input.json", "r") as file:
            input_data = json.load(file)

        with open("Output.json", "r") as file:
            output_data = json.load(file)

        response = self.app.post("/reformat", json=input_data)
        response_data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data, output_data)


if __name__ == '__main__':
    unittest.main()
