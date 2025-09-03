from urfu.application.errors import AppError


class UnauthenticatedError(AppError):
    status_code = 401
    message = "Unauthenticated"


class UnauthorizedError(AppError):
    status_code = 403
    message = "Unauthorized"
