import json
import pytest

from tests.base import BaseTestCase


class GetCustomersTestCase(BaseTestCase):
    """ Get Customers Route """

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


class CreateCustomersTestCase(BaseTestCase):
    """ Create Customer Route """

    def setUp(self):
        self.create_default_data() # process default data

    def test_customer_already_exists(self):
        """ Test create customer fail
        POST /customers
        """
        customer = {
            "customer": {
                "id": 1,
                "attributes": {
                    "created_at": "1560964022",
                    "email": "example@customer.io",
                    "first_name": "example"
                }
            }
        }

        response = self.client.post('customers',
            data=json.dumps(customer),
            content_type='application/json'
        )
        response_data = json.loads(response.data)

        self.assertEqual(response_data['message'], 'Customer ID already exists')
        self.assert400(response)

    def test_create_customer(self):
        """ Test create customer success
        POST /customers
        """
        customer = {
            "customer": {
                "id": 12345,
                "attributes": {
                    "created_at": "1560964022",
                    "email": "example@customer.io",
                    "first_name": "example"
                }
            }
        }

        response = self.client.post('customers',
            data=json.dumps(customer),
            content_type='application/json'
        )
        response_data = json.loads(response.data)

        self.assertTrue(response_data['customer'])
        self.assertEqual(response_data['customer']['id'], 12345)
        self.assertEqual(response_data['customer']['attributes']['created_at'], '1560964022')
        self.assertEqual(response_data['customer']['attributes']['email'], 'example@customer.io')
        self.assertEqual(response_data['customer']['attributes']['first_name'], 'example')
        self.assertTrue(response_data['customer']['last_updated'])
        self.assertEqual(response.status_code, 201)
