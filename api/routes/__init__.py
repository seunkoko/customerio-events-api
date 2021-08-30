from flask_restful import Api

# import controllers
from ..controllers import (
    CustomersResource
)

api = Api()

# add routes
api.add_resource(CustomersResource, '/customers', '/customers/')
