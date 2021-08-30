from flask_restful import Api

# import controllers
from ..controllers import (
    CustomersResource, UnitCustomerResource
)

api = Api()

# add routes
api.add_resource(CustomersResource, '/customers', '/customers/')
api.add_resource(UnitCustomerResource, '/customers/<customer_id>', '/customers/<customer_id>/')
