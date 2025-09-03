from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from urfu.application.contracts.specializations.create import (
    CreateSpecializationRequest,
)
from urfu.application.usecases.specializations.create import CreateSpecialization
from urfu.domain.dto.specialization import Specialization

router = APIRouter(
    prefix="/specialization", tags=["Specialization"], route_class=DishkaRoute
)


@router.post("")
async def create_specialization(
    req: CreateSpecializationRequest, interactor: FromDishka[CreateSpecialization]
) -> Specialization:
    return await interactor(req)
