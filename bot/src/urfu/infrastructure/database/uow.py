from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from urfu.application.common.uow import UnitOfWork


@dataclass
class UnitOfWorkImpl(UnitOfWork):
    session: AsyncSession

    async def commit(self) -> None:
        await self.session.commit()

    async def flush(self) -> None:
        await self.session.flush()

    async def rollback(self) -> None:
        await self.session.rollback()
