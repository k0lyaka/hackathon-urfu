from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from urfu.application.contracts.exam_scores.add_exam_scores import AddExamScoresRequest
from urfu.application.usecases.exam_scores.add_exam_scores import AddExamScores
from urfu.domain.entities.user import UserEntity

router = APIRouter(prefix="/profile", tags=["Profile"], route_class=DishkaRoute)


@router.post("/exams")
async def add_exams_scores(
    req: AddExamScoresRequest, interactor: FromDishka[AddExamScores]
) -> UserEntity:
    return await interactor(req)
