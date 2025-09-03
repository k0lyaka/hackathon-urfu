from urfu.infrastructure.errors.gateways import ModelNotFoundError


class ExamScoreNotFoundError(ModelNotFoundError):
    message = "Exam score not found"
