from flask import Flask, Response,  url_for
import random
from unittest.mock import patch
from flask_testing import TestCase
import requests_mock
from application import *



from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_animal0(self):
        with patch('requests.get') as g:
            g.return_value.text = 'Dog'
            #assert get_animal()=='Dog'
            response = self.client.get(url_for('get_noise'))
            self.assertIn(b'Bark', response.data)


    def test_animal1(self):
        with patch('requests.get') as g:
            g.return_value.text = 'Cat'
            #assert get_animal()=='Dog'
            response = self.client.get(url_for('get_noise'))
            self.assertIn(b'Meow', response.data)
    def test_animal2(self):
        with patch('requests.get') as g:
            g.return_value.text = 'Horse'
            #assert get_animal()=='Dog'
            response = self.client.get(url_for('get_noise'))
            self.assertIn(b'Neigh', response.data)
