from dataclasses import dataclass

from sqlalchemy import insert, select, update
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from urfu.application.gateways.specialization import (
    SpecializationReader,
    SpecializationUpdater,
    SpecializationWriter,
)
from urfu.domain.dto.specialization import (
    CreateSpecializationDTO,
    UpdateSpecializationDTO,
)
from urfu.domain.entities.specialization import SpecializationEntity
from urfu.domain.entities.user import UserEntity
from urfu.domain.enums.subject import SubjectEnum
from urfu.domain.value_objects.specialization import SpecializationId
from urfu.infrastructure.database.models.specialization import SpecializationModel
from urfu.infrastructure.errors.gateways.specialization import (
    SpecializationNotFoundError,
)

OPTIONS = [joinedload(SpecializationModel.scores)]
CURRENT_YEAR = 2025


@dataclass
class SpecializationGateway(
    SpecializationReader, SpecializationWriter, SpecializationUpdater
):
    session: AsyncSession

    async def with_id(
        self, specialization_id: SpecializationId
    ) -> SpecializationEntity:
        stmt = (
            select(SpecializationModel)
            .where(SpecializationModel.id == specialization_id.value)
            .options(*OPTIONS)
        )

        try:
            result = (await self.session.scalars(stmt)).unique().one()
        except NoResultFound as err:
            raise SpecializationNotFoundError from err

        return result.to_entity()

    async def get_all_tags(self) -> set[str]:
        stmt = select(SpecializationModel.tags)

        tags = (await self.session.scalars(stmt)).all()
        result = set()

        for tag in tags:
            result.update(tag)

        return result

    async def save(self, dto: CreateSpecializationDTO) -> SpecializationEntity:
        stmt = (
            insert(SpecializationModel)
            .values(**dto.model_dump())
            .returning(SpecializationModel.id)
        )
        result = (await self.session.execute(stmt)).scalar_one()
        return await self.with_id(SpecializationId(result))

    async def update(self, dto: UpdateSpecializationDTO) -> SpecializationEntity:
        stmt = (
            update(SpecializationModel)
            .where(SpecializationModel.id == dto.id.value)
            .values(**dto.model_dump(exclude={"id"}, exclude_unset=True))
        )

        await self.session.execute(stmt)

        return await self.with_id(dto.id)

    async def get_all_with_scores(self) -> list[SpecializationEntity]:
        stmt = select(SpecializationModel).options(*OPTIONS)
        results = (await self.session.scalars(stmt)).unique().all()
        return [result.to_entity() for result in results]

    async def get_suitable_for_user(
        self, user: UserEntity
    ) -> list[SpecializationEntity]:
        all_specializations = await self.get_all_with_scores()

        user_scores = {score.subject: score.score for score in user.exam_scores}

        if (
            SubjectEnum.RUSSIAN not in user_scores
            or SubjectEnum.MATH not in user_scores
        ):
            return []

        russian_score = user_scores[SubjectEnum.RUSSIAN]
        math_score = user_scores[SubjectEnum.MATH]

        additional_subjects = {
            k: v
            for k, v in user_scores.items()
            if k not in [SubjectEnum.RUSSIAN, SubjectEnum.MATH]
        }

        best_additional_score = 0
        if additional_subjects:
            best_additional_score = max(additional_subjects.values())

        total_user_score = russian_score + math_score + best_additional_score

        suitable_specializations = []

        user_tags = user.interest_tags or []
        positive_tags = {
            t.strip().lower() for t in user_tags if not t.strip().startswith("-")
        }
        negative_tags = {
            t.strip()[1:].lower()
            for t in user_tags
            if t.strip().startswith("-") and len(t.strip()) > 1
        }

        for specialization in all_specializations:
            latest_scores = [
                score for score in specialization.scores if score.year == CURRENT_YEAR
            ]

            if not latest_scores:
                continue

            min_score = latest_scores[0].minimal_score

            if total_user_score >= min_score:
                suitable_specializations.append(specialization)

        def sort_key(spec: SpecializationEntity) -> tuple[int, int]:
            spec_tag_set = {t.strip().lower() for t in spec.tags}

            matching_positive = len(positive_tags & spec_tag_set)
            matching_negative = len(negative_tags & spec_tag_set)

            # anti-tags subtract attractiveness
            matching_tags = matching_positive - matching_negative

            return (-matching_tags, -total_user_score)

        suitable_specializations.sort(key=sort_key)

        return suitable_specializations
