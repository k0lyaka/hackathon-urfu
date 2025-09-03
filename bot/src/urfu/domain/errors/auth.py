from urfu.application.errors import AppError


class UnauthorizedError(AppError):
    status_code = 403
    message = "Unauthorized"
