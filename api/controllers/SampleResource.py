import os

from flask import g, request
from flask_restful import Resource

from ..helper import response_message


class SampleResource(Resource):

    def get(self):
        return response_message(
            'success',
            200,
            'Successfully hit this endpoint'
        )

    def post(self):
        data = request.get_json()

        return response_message(
            'success',
            200,
            'Successfully hit this endpoint',
            {}
        )
