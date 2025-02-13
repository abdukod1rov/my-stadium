from typing import (
    List,
    TypeVar,
    Type,
    Generic, Any, Sequence
)

from sqlalchemy import delete, func, Row, RowMapping, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm.strategy_options import Load
from app.infrastructure.database.models import Base

Model = TypeVar("Model", Base, Base)


class BaseDAO(Generic[Model]):
    def __init__(
            self,
            model: Type[Model],
            session: AsyncSession,
    ):
        self.model = model
        self.session = session

    async def _get_all(
            self, skip: int = 0, limit: int = 20
    ):
        result = await self.session.execute(select(self.model).offset(skip).limit(limit)
                                            .order_by(text('id')))
        return result.scalars().all()

    async def get_by_id(
            self,
            id_: int,
            options: list[Load] = None,
    ) -> Model:
        query = select(self.model).where(self.model.id == id_)
        if options:
            query = query.options(*options)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    def _save(
            self,
            obj: Model,
    ):
        self.session.add(obj)

    async def delete_all(
            self,
    ):
        await self.session.execute(delete(self.model))

    async def _delete(
            self,
            obj: Model,
    ):
        await self.session.delete(obj)
        await self.session.commit()

    async def count(
            self,
    ):
        result = await self.session.execute(select(func.count(self.model.id)))
        return result.scalar_one()

    async def commit(
            self,
    ):
        await self.session.commit()

    async def _flush(self, *objects):
        await self.session.flush(objects)


