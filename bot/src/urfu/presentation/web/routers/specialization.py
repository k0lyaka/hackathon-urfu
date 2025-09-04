from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Body

from urfu.application.contracts.specializations.create import (
    CreateSpecializationRequest,
)
from urfu.application.contracts.specializations.get_raiting import (
    GetSpecializationsRequest,
)
from urfu.application.contracts.specializations.insert_tag import InsertTagsRequest
from urfu.application.usecases.specializations.create import CreateSpecialization
from urfu.application.usecases.specializations.get_raiting import GetSpecializations
from urfu.application.usecases.specializations.insert_tag import InsertTags
from urfu.domain.dto.specialization import Specialization

router = APIRouter(
    prefix="/specialization", tags=["Specialization"], route_class=DishkaRoute
)


@router.post("")
async def create_specialization(
    req: CreateSpecializationRequest, interactor: FromDishka[CreateSpecialization]
) -> Specialization:
    return await interactor(req)


@router.get("")
async def get_specializations(
    interactor: FromDishka[GetSpecializations],
) -> list[Specialization]:
    return await interactor(GetSpecializationsRequest())


@router.post("/{specialization_id}/tags")
async def insert_tags(
    specialization_id: int,
    tags: Annotated[list[str], Body()],
    interactor: FromDishka[InsertTags],
) -> Specialization:
    return await interactor(
        InsertTagsRequest(
            specialization_id=specialization_id,
            tags=tags,
        )
    )
