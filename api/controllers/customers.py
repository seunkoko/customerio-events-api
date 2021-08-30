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
