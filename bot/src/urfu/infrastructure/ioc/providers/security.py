from dishka import Provider, Scope, from_context, provide
from fastapi import Request

from urfu.application.common.security.id_provider import IdProvider
from urfu.application.common.security.token_processor import TokenProcessor
from urfu.domain.entities.user import UserEntity
from urfu.infrastructure.security.id_provider import UserIdProvider
from urfu.infrastructure.security.init_data_processor import InitDataProcessor


class SecurityProvider(Provider):
    scope = Scope.REQUEST

    request = from_context(Request)

    id_provider = provide(UserIdProvider, provides=IdProvider[UserEntity])
    init_data_processor = provide(
        InitDataProcessor, provides=TokenProcessor, scope=Scope.APP
    )
