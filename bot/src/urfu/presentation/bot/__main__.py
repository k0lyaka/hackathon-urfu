import asyncio

from aiogram import Bot

from urfu.infrastructure.ioc import get_container
from urfu.infrastructure.settings import AppSettings


async def main() -> None:
    container = get_container()

    bot = await container.get(Bot)
    settings = await container.get(AppSettings)

    url = settings.bot.url.unicode_string()

    await bot.set_webhook(
        url=f"{url}hooks/telegram",
        secret_token=settings.bot.secret.get_secret_value(),
    )


if __name__ == "__main__":
    asyncio.run(main())
