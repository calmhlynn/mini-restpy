import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings
from logger.utils import get_logger

logger = get_logger(__name__)
load_dotenv()


class Settings(BaseSettings):
    """
    .env에 저장한 DATABASE의 정보를 검증한다.

    :argument BaseSettings
    BaseSettings는 Pydantic에서 Setting 인스턴스를 만들 때 데이터를 검증합니다.

    :param pg_user: str = postgresql 유저 이름
    :param pg_pass: str = postgresql 패스워드
    :param pg_database: str = postgresql DB 이름
    :param asyncpg_url : AnyUrl = asyncpg URL

    :return instance of Settings
    """

    pg_user: str = os.environ.get("POSTGRES_USER")
    pg_pass: str = os.environ.get("POSTGRES_PW")
    pg_host: str = os.environ.get("POSTGRES_HOST")
    pg_DB: str = os.environ.get("POSTGRES_DB")

    print(f"pg_user: {pg_user}, pg_pass:{pg_pass}, pg_host: {pg_host}, pg_db: {pg_DB}")

    asyncpg_url: str = f"postgresql+asyncpg://{pg_user}:{pg_pass}@{pg_host}:5432/{pg_DB}"


@lru_cache  # 함수의 리턴결과를 캐시해주는 데코레이터이다.
def get_settings():
    logger.info("Loading config settings from the environment...")
    return Settings()
