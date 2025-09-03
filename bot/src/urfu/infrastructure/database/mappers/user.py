from urfu.domain.dto.user import UserDTO
from urfu.domain.entities.user import UserEntity
from urfu.infrastructure.database.mappers.exam_score import exam_score_entity_to_dto


def user_entity_to_dto(entity: UserEntity) -> UserDTO:
    return UserDTO(
        id=entity.id.value,
        telegram_id=entity.telegram_id.value,
        username=entity.username,
        interest_tags=entity.interest_tags,
        full_interest_text=entity.full_interest_text,
        exam_scores=[exam_score_entity_to_dto(score) for score in entity.exam_scores],
    )
