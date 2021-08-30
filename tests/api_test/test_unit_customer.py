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


class UpdateCustomersTestCase(BaseTestCase):
    """ Update Unit Customer Route """

    def setUp(self):
        self.create_default_data() # process default data

    def test_update_customer_does_not_exist(self):
        """ Test update unit customer
        PATCH /customer/customer_id
        """
        customer = {
            "customer": {
                "attributes": {
                    "ip": "127.0.0.1",
                    "first_name": "real",
                    "last_name": "customer"
                }
            }
        }

        response = self.client.patch('customers/200000000',
            data=json.dumps(customer),
            content_type='application/json'
        )
        response_data = json.loads(response.data)

        self.assertEqual(response_data['message'], 'Customer ID does not exist')
        self.assert400(response)

    def test_update_customer_immutable_field(self):
        """ Test update unit customer fields that should not change
        PATCH /customer/customer_id
        """
        customer = {
            "customer": {
                "attributes": {
                    "ip": "127.0.0.1",
                    "first_name": "real",
                    "last_name": "customer",
                    "email": "customer@email.com"
                }
            }
        }

        response = self.client.patch('customers/1',
            data=json.dumps(customer),
            content_type='application/json'
        )
        response_data = json.loads(response.data)

        self.assertEqual(response_data['message'], 'Customer email, id or created_at fields cannot be updated.')
        self.assert400(response)

    def test_update_customer_success(self):
        """ Test update unit customer fields that should not change
        PATCH /customer/customer_id
        """
        customer = {
            "customer": {
                "attributes": {
                    "first_name": "real",
                    "last_name": "customer"
                }
            }
        }

        response = self.client.patch('customers/5',
            data=json.dumps(customer),
            content_type='application/json'
        )
        response_data = json.loads(response.data)

        self.assertEqual(response_data['customer']['id'], '5')
        self.assertEqual(response_data['customer']['attributes']['first_name'], 'real')
        self.assertEqual(response_data['customer']['attributes']['last_name'], 'customer')
        self.assertEqual(response_data['customer']['attributes']['ip'], '210.36.180.177')
        self.assertNotEqual(response_data['customer']['last_updated'], self.customers['5']['last_updated'])
        self.assert200(response)


