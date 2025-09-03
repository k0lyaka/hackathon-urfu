from urfu.domain.dto.exam_score import ExamScoreDTO
from urfu.domain.entities.exam_score import ExamScoreEntity


def exam_score_entity_to_dto(entity: ExamScoreEntity) -> ExamScoreDTO:
    return ExamScoreDTO(
        id=entity.id.value,
        subject=entity.subject,
        score=entity.score,
        year=entity.year,
    )
