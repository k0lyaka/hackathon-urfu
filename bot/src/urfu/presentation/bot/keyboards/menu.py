from typing import Any

from aiogram.utils.keyboard import InlineKeyboardBuilder


def menu_keyboard(profile_created: bool, bot_username: str) -> Any:
    builder = InlineKeyboardBuilder()

    if not profile_created:
        builder.button(
            text="Заполнить анкету",
            url=f"https://t.me/{bot_username}/registration",
        )
    else:
        builder.button(
            text="Посмотреть направления",
            url=f"https://t.me/{bot_username}/specs",
        )

    return builder.as_markup()
