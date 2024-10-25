import unittest
import json
from flask import Flask
from your_flask_app import application  # Replace with your actual Flask app module

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = application
        self.app.testing = True
        self.client = self.app.test_client()

    def test_fake_news(self):
        fake_news = [
            "The moon landing was staged by NASA.",
            "Aliens have been living among us for years."
        ]
        for news in fake_news:
            response = self.client.post('/predict', json={'text': news})
            self.assertEqual(response.status_code, 200)
            self.assertIn('prediction', response.get_json())

    def test_real_news(self):
        real_news = [
            "The president signed a new bill into law.",
            "Scientists discover a new species of frog in the Amazon."
        ]
        for news in real_news:
            response = self.client.post('/predict', json={'text': news})
            self.assertEqual(response.status_code, 200)
            self.assertIn('prediction', response.get_json())

if __name__ == '__main__':
    unittest.main()