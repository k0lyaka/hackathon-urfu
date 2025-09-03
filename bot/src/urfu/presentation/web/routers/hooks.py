from aiogram import Bot, Dispatcher
from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Depends

from urfu.presentation.web.dependencies.telegram import validate_telegram_hook

router = APIRouter(prefix="/hooks", include_in_schema=False, route_class=DishkaRoute)


@router.post("/telegram", dependencies=[Depends(validate_telegram_hook)])
async def telegram_webhook(
    update: dict, bot: FromDishka[Bot], dp: FromDishka[Dispatcher]
) -> dict[str, str]:
    await dp.feed_raw_update(bot, update)

    return {"status": "ok"}
