import functools
from functools import wraps
from http import HTTPStatus

from sqlalchemy.exc import OperationalError, IntegrityError, ProgrammingError, NoInspectionAvailable
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Namespace, marshal

from api.src.constants import StatusAPI
from api.src.marshalls import marshall_api_response


def role_required(role):
    def decorator(fn):
        @wraps(fn)
        @jwt_required()
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user['role'] != role:
                return  marshal(
                    StatusAPI.FORBIDEN,
                    marshall_api_response
                ), int(HTTPStatus.FORBIDDEN)
            return fn(*args, **kwargs)
        return wrapper
    return decorator


def exceptions(namespace: Namespace):
    """Exception to OperationalError on database"""
    def decorator(function: callable):
        @functools.wraps(function)
        def type_exceptions(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except (OperationalError, IntegrityError, ProgrammingError, NoInspectionAvailable,
                    AttributeError, KeyError, ValueError) as _error:
                namespace.logger.critical(_error)
                response, code = marshal(
                    StatusAPI.INTERNAL_SERVER_ERROR_API,
                    marshall_api_response
                ), int(HTTPStatus.INTERNAL_SERVER_ERROR)
            return response, code

        return type_exceptions
    return decorator
