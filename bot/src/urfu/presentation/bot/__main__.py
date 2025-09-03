import asyncio

from aiogram import Bot
from aiogram.types import BotCommand

from urfu.infrastructure.ioc import get_container
from urfu.infrastructure.settings import AppSettings


async def setup_commands(bot: Bot) -> None:
    await bot.set_my_commands([BotCommand(command="start", description="Главное меню")])


async def main() -> None:
    container = get_container()

    bot = await container.get(Bot)
    settings = await container.get(AppSettings)

    url = settings.bot.url.unicode_string()

    await setup_commands(bot)

    await bot.set_webhook(
        url=f"{url}hooks/telegram",
        secret_token=settings.bot.secret.get_secret_value(),
    )


if __name__ == "__main__":
    asyncio.run(main())
