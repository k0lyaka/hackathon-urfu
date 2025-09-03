from urfu.application.errors import AppError


class ModelNotFoundError(AppError):
    message = "Not found"
    status_code = 404
