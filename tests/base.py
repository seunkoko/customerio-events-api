import os
import json

from flask_testing import TestCase
from server import create_flask_app
from data_processing import file_summary


class BaseTestCase(TestCase):
    """ Testing Setup """

    def create_app(self):
        """ Create app instance for testing """
        self.app = create_flask_app('testing')
        
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.client = self.app.test_client()

        return self.app

    def tearDown(self):
        """ Write empty data from file """
        fileToWrite = open("tests/default_test_data/summary.data", "w")
        fileToWrite.write("")
        fileToWrite.close()
        
    def create_default_data(self):
        """ Create default data """
        file_summary("tests/default_test_data/mock_event.data", True)
        
        file_to_read = open("tests/default_test_data/summary.data", "r")
        self.customers = json.loads(file_to_read.read())
        file_to_read.close()
