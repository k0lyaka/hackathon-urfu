from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from urfu.application.contracts.exam_scores.add_exam_scores import AddExamScoresRequest
from urfu.application.contracts.users.get import GetUserRequest
from urfu.application.contracts.users.update_interests import UpdateInterestsRequest
from urfu.application.usecases.exam_scores.add_exam_scores import AddExamScores
from urfu.application.usecases.users.get import GetUser
from urfu.application.usecases.users.update_interests import UpdateInterests
from urfu.domain.dto.user import UserDTO

router = APIRouter(prefix="/profile", tags=["Profile"], route_class=DishkaRoute)


@router.get("")
async def get_profile(interactor: FromDishka[GetUser]) -> UserDTO:
    return await interactor(GetUserRequest())


@router.post("/exams")
async def add_exams_scores(
    req: AddExamScoresRequest, interactor: FromDishka[AddExamScores]
) -> UserDTO:
    return await interactor(req)


@router.post("/interests")
async def update_interests(
    req: UpdateInterestsRequest, interactor: FromDishka[UpdateInterests]
) -> UserDTO:
    return await interactor(req)
