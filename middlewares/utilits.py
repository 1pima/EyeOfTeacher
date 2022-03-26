from flask import abort
from functools import wraps

from flask import request, g
from marshmallow import ValidationError
import marshmallow as ma


def parse_params(schema: ma.Schema = None):

    def decorator(fn):

        @wraps(fn)
        def wrapper(*args, **kwargs):
            if request.method == 'GET':
                return fn(*args, **kwargs)
            elif request.form:
                data = request.form
            else:
                return abort(403)

            if schema:
                try:
                    g.rq = schema.load(data)
                except ValidationError:
                    return abort(403)

            return fn(*args, **kwargs)

        return wrapper
    return decorator
