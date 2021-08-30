import os
import time

from flask import g, request
from flask_restful import Resource

from ..helper import (
    response_message, validate_request, get_data_summary,
    write_to_file
)


class UnitCustomerResource(Resource):
    """ Unit Customer Resource
    GET /customers/customer_id - Gets a customer's summary
    PATCH /customers/customer_id - Update customer's attribute summary
    DELETE /customers/customer_id - Delete customer's summary
    """

    @get_data_summary()
    def get(self, customer_id):
        """Get unit customer data"""

        # check if customer exists
        if customer_id not in list(g.customers.keys()):
            # returns error message if customer does not exist
            return {
                "message": "Customer ID does not exist"
            }, 400

        # returns customer
        return {
            "customer": g.customers[customer_id]
        }, 200

    @validate_request()
    @get_data_summary()
    def patch(self, customer_id):
        """Update customer attribute"""

        _data = request.get_json() # request body

        # check if customer exists
        if customer_id not in list(g.customers.keys()):
            return {
                "message": "Customer ID does not exist"
            }, 400

        # get customer summary
        current_customer_details = g.customers[customer_id]

        # check that immutable fields are not updated
        immutable_fields = {'email', 'id', 'created_at'}
        if set(_data['customer']['attributes'].keys()) & immutable_fields:
            return {
                "message": "Customer email, id or created_at fields cannot be updated."
            }, 400

        # prepare updated customer data
        updated_customer = {
            **current_customer_details,
            'attributes': {
                **current_customer_details['attributes'],
                **_data['customer']['attributes']
            },
            'last_updated': round(time.time())
        }

        # update customer data
        g.customers[customer_id] = updated_customer

        # update file
        write_to_file(g.customers)

        # return success message
        return {
            "customer": updated_customer
        }

    @get_data_summary()
    def delete(self, customer_id):
        """Delete unit customer data"""

        # check if customer exists
        if customer_id not in list(g.customers.keys()):
            return {
                "message": "Customer ID does not exist"
            }, 400

        # delete customer
        del g.customers[customer_id]

        # update file
        write_to_file(g.customers)

        # return success message
        return {
            "message": "Customer info deleted successfully"
        }, 201
