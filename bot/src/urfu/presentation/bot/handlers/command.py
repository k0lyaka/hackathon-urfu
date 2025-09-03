from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from urfu.domain.entities.user import UserEntity
from urfu.presentation.bot.keyboards.menu import menu_keyboard

router = Router(name=__name__)


@router.message(CommandStart())
async def start_handler(message: Message, user: UserEntity) -> None:
    bot_info = await message.bot.me()

    await message.answer(
        "Привет!",
        reply_markup=menu_keyboard(
            user.is_profile_created,
            bot_info.username,
        ),
    )
