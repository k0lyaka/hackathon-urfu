from dataclasses import dataclass

from urfu.application.common.interactor import Interactor
from urfu.application.common.uow import UnitOfWork
from urfu.application.gateways.specialization_score import SpecializationScoreWriter
from urfu.domain.dto.specialization import CreateSpecializationScoreDTO
from urfu.domain.entities.specialization_score import SpecializationScoreEntity


@dataclass
class CreateSpecializationScoresBatch(
    Interactor[list[CreateSpecializationScoreDTO], list[SpecializationScoreEntity]]
):
    specialization_score_writer: SpecializationScoreWriter

    uow: UnitOfWork

    async def __call__(
        self, data: list[CreateSpecializationScoreDTO]
    ) -> list[SpecializationScoreEntity]:
        async with self.uow:
            results = [
                await self.specialization_score_writer.save(item) for item in data
            ]

            await self.uow.commit()

        return results
