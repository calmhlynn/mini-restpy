from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy import Column, String, DateTime, select
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from model.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    create_on = Column(DateTime, nullable=False)

    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email

    @classmethod
    async def find(cls, db_session: AsyncSession, username: str):
        stmt = select(cls).where(cls.username == username)
        result = await db_session.execute(stmt)
        instance = result.scalars().first()
        if instance is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={"Not Found": f"There is no record for requested: {username=}"}
            )
        else:
            return instance
