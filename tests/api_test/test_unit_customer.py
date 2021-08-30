import json
import pytest

from tests.base import BaseTestCase


class GetCustomersTestCase(BaseTestCase):
    """ Get Unit Customer Route """

    def setUp(self):
        self.create_default_data() # process default data

    def test_get_customer_does_not_exist(self):
        """ Test get unit customer
        GET /customer/customer_id
        """
        response = self.client.get('customers/200000000',
            content_type='application/json'
        )
        response_data = json.loads(response.data)

        self.assertEqual(response_data['message'], 'Customer ID does not exist')
        self.assert400(response)

    def test_get_customer_exist(self):
        """ Test get unit customer exist
        GET /customers/customer_id
        """
        response = self.client.get('customers/1',
            content_type='application/json'
        )
        response_data = json.loads(response.data)

        self.assertTrue(response_data['customer'])
        self.assertEqual(response_data['customer']['id'], '1')
        self.assert200(response)