from dishka import AsyncContainer, make_async_container

from urfu.infrastructure.ioc.providers.adapters import (
    AiProvider,
    BotProvider,
    SQLAlchemyProvider,
)
from urfu.infrastructure.ioc.providers.gateways import GatewaysProvider
from urfu.infrastructure.ioc.providers.security import SecurityProvider
from urfu.infrastructure.ioc.providers.settings import SettingsProvider
from urfu.infrastructure.ioc.providers.usecases import UseCasesProvider


def get_container() -> AsyncContainer:
    return make_async_container(
        SettingsProvider(),
        SQLAlchemyProvider(),
        UseCasesProvider(),
        GatewaysProvider(),
        SecurityProvider(),
        BotProvider(),
        AiProvider(),
    )
