from dishka import AsyncContainer, make_async_container

from urfu.infrastructure.ioc.providers.adapters import BotProvider, SQLAlchemyProvider
from urfu.infrastructure.ioc.providers.gateways import GatewaysProvider
from urfu.infrastructure.ioc.providers.settings import SettingsProvider


def get_container() -> AsyncContainer:
    return make_async_container(
        SettingsProvider(),
        SQLAlchemyProvider(),
        GatewaysProvider(),
        BotProvider(),
    )
