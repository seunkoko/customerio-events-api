import os
import time

from flask import g, request
from flask_restful import Resource

from ..helper import (
    response_message, get_data_summary,
    validate_request, write_to_file
)


class CustomersResource(Resource):
    """Customers Resource
    GET /customers - Gets all customers
    POST /customers - Creates a new customer
    """

    @get_data_summary()
    def get(self):
        """Get all customer data summary"""

        page = request.args.get('page', 1, type=int) # active page, pagination
        per_page = request.args.get('per_page', 10, type=int) # data per page, pagination

        # get all customers
        all_customers = list(g.customers.values())

        # paginate data
        paginated_data = [
            all_customers[i:i+per_page] for i in range(0, len(all_customers), per_page)
        ]

        # return all customer with pagination meta-data
        return {
            "customers": paginated_data[page-1],
            "meta": {
                "page": page,
                "per_page": per_page,
                "total": len(all_customers)
            }
        }, 200

    @validate_request()
    @get_data_summary()
    def post(self):
        """Create new customer data"""

        # get customer data from request body
        _data = request.get_json()

        # check that customer does not exist
        if 'customer' in _data and 'id' in _data['customer'] and \
        str(_data['customer']['id']) in list(g.customers.keys()):
            return {
                "message": "Customer ID already exists"
            }, 400

        # create new customer data
        new_customer = {
            **_data['customer'],
            'events': {},
            'last_updated': round(time.time())
        }

        # add new customer data
        g.customers[_data['customer']['id']] = new_customer

        # update file
        write_to_file(g.customers)

        # return new customer
        return {
            "customer": new_customer
        }, 201
