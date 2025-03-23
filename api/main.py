import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.resources import Resources
from api.routers.fake_personal import router as fake_personal_router
import uvicorn
from api.config import config


@asynccontextmanager
async def lifespan(app: FastAPI):
    Resources.setup()
    yield


def app_factory():
    app = FastAPI(
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(fake_personal_router, prefix="/fake_personal")

    return app


app = app_factory()
uvicorn.run(app, host="localhost", port=8000)