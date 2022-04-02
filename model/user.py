import uuid
from datetime import datetime, timezone

from fastapi import HTTPException, status
from sqlalchemy import Column, String, DateTime, select, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from model.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), unique=True, default=uuid.uuid4, autoincrement=True)
    username = Column(String(20), primary_key=True, nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    create_on = Column(DateTime, default=func.now(), nullable=True)

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
