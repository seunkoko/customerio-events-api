import os
import json

from functools import wraps
from flask import g


def get_data_summary():
    """ This method gets data summary and makes it available globally.
    """

    def real_get_data_summary(f):
        @wraps(f)
        def decorated(*args,**kwargs):
            try:
                # filename used based on app environment
                file_name = "tests/default_test_data/summary.data" if \
                os.getenv('FLASK_CONFIG') == "testing" else "data/summary.data"

                file_to_read = open(file_name, "r") # read file
                g.customers = json.loads(file_to_read.read()) # make data summary available globally
            except:
                # in case of any exceptions, customer is an empty dict
                g.customers = {} 

            return f(*args, **kwargs)

        return decorated

    return real_get_data_summary
