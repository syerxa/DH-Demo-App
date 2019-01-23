from flask import Flask
from flask_testing import TestCase
from app import create_app, db

class MyTest(TestCase):

    def create_app(self):
        return create_app()
    
    def test_get_all_lists(self):
        response = self.client.get('/lists')
        self.assert200(response)