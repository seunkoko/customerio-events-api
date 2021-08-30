import os
import json

from flask import request
from functools import wraps

def validate_request():
    """ This method validates the Request payload.
    Args
        expected_args(tuple): where i = 0 is type and i > 0 is argument to be
                            validated
    Returns
      f(*args, **kwargs)
    """

    def real_validate_request(f):
        @wraps(f)
        def decorated(*args,**kwargs):
            if not request.json:
                return {"status": "fail",
                        "data": {"message": "Request must be a valid JSON"}
                       }, 400

            return f(*args, **kwargs)

        return decorated

    return real_validate_request

def write_to_file(new_data):
    """Write updated data to file
    """
    # filename used based on app environment
    file_name = "tests/default_test_data/summary.data" if \
    os.getenv('FLASK_CONFIG') == "testing" else "data/summary.data"

    file_to_write = open(file_name, "w")
    file_to_write.write(json.dumps(new_data))
    file_to_write.close()

