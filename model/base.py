from typing import Any

from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declared_attr


@as_declarative()
class Base:
    id: Any

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    async def save(self, db_session: AsyncSession):
        try:
            db_session.add(self)
            return await db_session.commit()

        except SQLAlchemyError as sql_err:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(sql_err))

    async def delete(self, db_session: AsyncSession):
        try:
            await db_session.delete(self)
            await db_session.commit()
            return True

        except SQLAlchemyError as sql_err:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=repr(sql_err))

    async def update(self, db_session: AsyncSession, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

        await self.save(db_session)
