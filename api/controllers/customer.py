import os
import time

from flask import g, request
from flask_restful import Resource

from ..helper import (
    response_message, validate_request, get_data_summary,
    write_to_file
)


class UnitCustomerResource(Resource):
    """Unit Customer Resource
    GET /customers/customer_id - Gets a customer's summary
    PATCH /customers/customer_id - Update customer's attribute summary
    DELETE /customers/customer_id - Delete customer's summary
    """

    @get_data_summary()
    def get(self, customer_id):
        pass