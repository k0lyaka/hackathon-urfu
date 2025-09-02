from urfu.infrastructure.errors.gateways import ModelNotFoundError


class UserNotFoundError(ModelNotFoundError):
    message = "User not found"
