import json
import pytest

from tests.base import BaseTestCase


class DataProcessingTestCase(BaseTestCase):
    """ Test Data processing function """

    def setUp(self):
        self.create_default_data() # process default data

    def test_duplicated_events(self):
        """ Test duplicated events are skipped
        """
        self.assertEqual(self.customers['1']['events']['programgoldenrod'], 1)

    def test_user_event_summary(self):
        """ Test user event summary data
        """
        self.assertEqual(len(self.customers['1']['events']), 2)
        self.assertTrue(self.customers['1']['events']['programgoldenrod'])
        self.assertTrue(self.customers['1']['events']['parsebrown'])
        self.assertEqual(self.customers['1']['events']['programgoldenrod'], 1)
        self.assertEqual(self.customers['1']['events']['parsebrown'], 1)

    def test_user_attribute_summary(self):
        """ Test user event attribute data
        """
        self.assertEqual(self.customers['3']['last_updated'], 1660980000)
        self.assertEqual(self.customers['3']['attributes']['last_name'], 'Owonikoko')
        self.assertTrue(self.customers['3']['attributes']['city'])
        self.assertTrue(self.customers['3']['attributes']['cadillackacey'])

    def test_user_count(self):
        """ Test users data is complete
        """
        self.assertEqual(len(self.customers), 5)
