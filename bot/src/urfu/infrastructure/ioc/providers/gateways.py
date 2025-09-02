from dishka import AnyOf, Provider, Scope, provide

from urfu.application.common.uow import UnitOfWork
from urfu.application.gateways.user import UserReader, UserUpdater, UserWriter
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

    # other
    uow = provide(UnitOfWorkImpl, provides=UnitOfWork)
