import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.db.session import db_helper
from app.core.config import settings
from app.core.clients import APIClients
from app.api import router as api_router
from app.core.exceptions import DatabaseError, NotFoundError


@asynccontextmanager
async def lifespan(app: FastAPI):
    clients = APIClients()
    await clients.init_digi_client()
    await clients.init_wgamers_client()
    app.state.clients = clients
    yield
    await db_helper.dispose()
    await app.state.clients.close_all()


app = FastAPI(
    version="1.0",
    docs_url="/docs",
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    api_router,
)


@app.exception_handler(DatabaseError)
async def handle_database_error(request: Request, exc: DatabaseError):
    return ORJSONResponse(status_code=500, content={"detail": str(exc)})


@app.exception_handler(NotFoundError)
async def handle_not_found_error(request: Request, exc: NotFoundError):
    return ORJSONResponse(status_code=404, content={"detail": str(exc)})


if __name__ == "__main__":

    uvicorn.run(
        app="main:app", host=settings.run.host, port=settings.run.port, reload=True
    )
