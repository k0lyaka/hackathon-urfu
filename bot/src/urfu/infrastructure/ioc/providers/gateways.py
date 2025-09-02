from dishka import AnyOf, Provider, Scope, provide

from urfu.application.common.uow import UnitOfWork
from urfu.application.gateways.exam_score import ExamScoreReader, ExamScoreWriter
from urfu.application.gateways.user import UserReader, UserUpdater, UserWriter
from urfu.infrastructure.database.gateways.exam_score import ExamScoreGateway
from urfu.infrastructure.database.gateways.user import UserGateway
from urfu.infrastructure.database.uow import UnitOfWorkImpl


class GatewaysProvider(Provider):
    scope = Scope.REQUEST

    user_gateway = provide(
        UserGateway,
        provides=AnyOf[
            UserReader,
            UserWriter,
            UserUpdater,
        ],
    )

    exam_score_gateway = provide(
        ExamScoreGateway,
        provides=AnyOf[
            ExamScoreReader,
            ExamScoreWriter,
        ],
    )

    # other
    uow = provide(UnitOfWorkImpl, provides=UnitOfWork)
