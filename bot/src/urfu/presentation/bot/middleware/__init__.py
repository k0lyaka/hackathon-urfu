from aiogram import Dispatcher

from urfu.presentation.bot.middleware.user import UserMiddleware


def setup_middlewares(dp: Dispatcher) -> None:
    user = UserMiddleware()

    dp.message.middleware(user)
    dp.callback_query.middleware(user)
