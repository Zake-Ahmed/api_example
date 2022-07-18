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
        with patch('random.randint') as g:
            g.return_value = 0
            #assert get_animal()=='Dog'
            response = self.client.get(url_for('get_animal'))
            self.assertIn(b'Dog', response.data)


    def test_animal1(self):
        with patch('random.randint') as g:
            g.return_value = 1

            response = self.client.get(url_for('get_animal'))
            self.assertIn(b'Cat', response.data)
    def test_animal2(self):
        with patch('random.randint') as g:
            g.return_value = 2

            response = self.client.get(url_for('get_animal'))
            self.assertIn(b'Horse', response.data)
