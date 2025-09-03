from collections.abc import AsyncIterable

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dishka import AsyncContainer, Provider, Scope, provide
from dishka.integrations.aiogram import setup_dishka
from sqlalchemy import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from urfu.infrastructure.adapters.openai.client import AiAdapter
from urfu.infrastructure.settings import AppSettings
from urfu.presentation.bot.handlers import setup_handlers
from urfu.presentation.bot.middleware import setup_middlewares


class SQLAlchemyProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_engine(self, settings: AppSettings) -> AsyncEngine:
        return create_async_engine(
            url=settings.database.build_connection_uri(),
            poolclass=AsyncAdaptedQueuePool,
            pool_size=30,
            max_overflow=20,
        )

    @provide(scope=Scope.APP)
    def provide_sessionmaker(
        self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            bind=engine, expire_on_commit=False, class_=AsyncSession
        )

    @provide(scope=Scope.REQUEST)
    async def provide_session(
        self, sessionmaker: async_sessionmaker[AsyncSession]
    ) -> AsyncIterable[AsyncSession]:
        async with sessionmaker() as session:
            yield session


class AiProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_ai_adapter(self, settings: AppSettings) -> AiAdapter:
        return AiAdapter(
            settings.ai.token.get_secret_value(),
            settings.ai.base_url.unicode_string(),
        )


class BotProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_bot(self, settings: AppSettings) -> Bot:
        return Bot(
            token=settings.bot.token.get_secret_value(),
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML, link_preview_is_disabled=True
            ),
        )

    @provide(scope=Scope.APP)
    def provide_dp(self, container: AsyncContainer) -> Dispatcher:
        # TODO: add redis storage

        dp = Dispatcher()

        setup_dishka(container, dp, auto_inject=True)
        setup_middlewares(dp)
        setup_handlers(dp)

        return dp
