from fastapi import FastAPI

from database.DB_create import engine
from logger.utils import get_logger
from api.user import router as user_router
from model.base import Base

logger = get_logger(__name__)

app = FastAPI(title="nfp fullstack backend API", version="0.1")

app.include_router(user_router)


async def start_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")
    await start_db()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
