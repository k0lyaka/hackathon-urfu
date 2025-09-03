from typing import Any

from aiogram.utils.keyboard import InlineKeyboardBuilder


def menu_keyboard(profile_created: bool, bot_username: str) -> Any:
    builder = InlineKeyboardBuilder()

    builder.button(
        text="Заполнить анкету" if not profile_created else "Просмотреть направления",
        url=f"https://t.me/{bot_username}/app",
    )

    return builder.as_markup()
