from urfu.infrastructure.errors.gateways import ModelNotFoundError


class SpecializationNotFoundError(ModelNotFoundError):
    message = "Specialization not found"


class SpecializationScoreNotFoundError(ModelNotFoundError):
    message = "Specialization score not found"
