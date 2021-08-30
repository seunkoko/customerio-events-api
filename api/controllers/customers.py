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
        pass
