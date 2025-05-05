import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.db.session import db_helper
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


app = FastAPI(
    version="1.0",
    docs_url="/docs",
    lifespan=lifespan
)

if __name__ == '__main__':

    uvicorn.run(
        app='main:app',
        host=settings.run.host,
        port=settings.run.port,
        reload=True
    )