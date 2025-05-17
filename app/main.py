import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

from app.db.session import db_helper
from app.core.config import settings
from app.api import router as api_router
from app.lib.http_client import HTTPClient
from app.core.exceptions import DatabaseError

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http_client = HTTPClient(
        base_url=settings.digi.base_url,
        headers=settings.digi.headers,
        timeout=settings.digi.timeout,
        delay=settings.digi.delay,
        retries=settings.digi.retries,
    )
    yield
    await db_helper.dispose()
    await app.state.http_client.close()


app = FastAPI(
    version="1.0",
    docs_url="/docs",
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)

app.include_router(
    api_router,
)

@app.exception_handler(DatabaseError)
async def handle_database_error(request: Request, exc: DatabaseError):
    return ORJSONResponse(status_code=500, content={"detail": str(exc)})


if __name__ == "__main__":

    uvicorn.run(
        app="main:app", host=settings.run.host, port=settings.run.port, reload=True
    )
