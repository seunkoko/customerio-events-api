import json
import pytest

from tests.base import BaseTestCase


class GetCustomersTestCase(BaseTestCase):
    """ Test Data processing function """

    def setUp(self):
        self.create_default_data() # process default data

    def test_get_all_customers(self):
        """ Test get customers
        GET /customers
        """
        response = self.client.get('customers',
            content_type='application/json'
        )
        response_data = json.loads(response.data)

        self.assertTrue(response_data['customers'])
        self.assertTrue(response_data['meta'])
        self.assertEqual(
            response_data['meta']['total'],
            len(self.customers)
        )
        self.assert200(response)

    def test_get_all_customers_pagination(self):
        """ Test get customers pagination
        GET /customers?page=2&per_page=2
        """
        response = self.client.get('customers?page=2&per_page=2',
            content_type='application/json'
        )
        response_data = json.loads(response.data)

        self.assertTrue(response_data['customers'])
        self.assertTrue(response_data['meta'])
        self.assertEqual(
            len(response_data['customers']),
            2
        )
        self.assertEqual(
            response_data['meta']['total'],
            len(self.customers)
        )
        self.assertEqual(
            response_data['meta']['page'],
            2
        )
        self.assert200(response)
