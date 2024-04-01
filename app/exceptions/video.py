from app.exceptions.base import JSONHTTPException


class ForbiddenMethod(JSONHTTPException):
    code = 403
    description = "Forbidden method"
