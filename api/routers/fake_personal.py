import asyncio
from typing import AsyncGenerator

from fastapi import APIRouter
from loguru import logger
from starlette.requests import Request
from fastapi.responses import StreamingResponse

from api.schemas import FakePersonalSchema
from api.resources import Resources

from google.protobuf.empty_pb2 import Empty
from sse_starlette.sse import EventSourceResponse


router = APIRouter()


@router.get("/")
async def generate_fake_personal() -> FakePersonalSchema:
    fake_personal = await Resources.fake_personal_stub.Generate(Empty())
    return FakePersonalSchema(
        name=fake_personal.name, address=fake_personal.address, city=fake_personal.city
    )


@router.get("/stream")
async def stream_generate_fake_personal(request: Request) -> StreamingResponse:
    async def stream() -> AsyncGenerator[FakePersonalSchema, None]:
        async for fake_person in Resources.fake_personal_stub.StreamGenerate(Empty()):
            if await request.is_disconnected():
                break
            fake_person_schema = FakePersonalSchema(
                name=fake_person.name,
                address=fake_person.address,
                city=fake_person.city
            )
            yield f"data: {fake_person_schema.model_dump_json()}\n\n"
            await asyncio.sleep(1)

    return StreamingResponse(
        stream(),
        media_type="text/event-stream"
    )


