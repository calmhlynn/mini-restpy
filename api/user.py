from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.DB_create import get_db
from model.user import User
from schema.user import UserResponse, UserSchema

router = APIRouter(prefix="/v1/user")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(payload: UserSchema, db_session: AsyncSession = Depends(get_db)):
    user = User(**payload.dict())
    await user.save(db_session)
    return user


@router.get("/", response_model=UserResponse)
async def find_user(username: str, db_session: AsyncSession = Depends(get_db)):
    return await User.find(db_session, username)


@router.delete("/")
async def delete_user(username: str, db_session: AsyncSession = Depends(get_db)):
    user = await User.find(db_session, username)
    return await user.delete(user, db_session)
