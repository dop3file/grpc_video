import asyncio
from typing import AsyncGenerator

import grpc
from google.protobuf.empty_pb2 import Empty
import faker
from loguru import logger

from fake_personal.proto.fake_personal_pb2 import FakePersonal
from fake_personal.proto.fake_personal_pb2_grpc import (
    FakePersonalServiceServicer,
    add_FakePersonalServiceServicer_to_server,
)

from fake_personal.config import config


class FakePersonalService(FakePersonalServiceServicer):
    def __init__(self):
        self._faker = faker.Faker()

    async def Generate(
        self, request: Empty, context: grpc.aio.ServicerContext
    ) -> FakePersonal:
        return FakePersonal(
            name=self._faker.name(),
            address=self._faker.address(),
            city=self._faker.city(),
        )

    async def StreamGenerate(
        self, request: Empty, context: grpc.aio.ServicerContext
    ) -> AsyncGenerator[FakePersonal, None]:
        logger.debug("Stream generate")
        while not context.done():
            yield FakePersonal(
                name=self._faker.name(),
                address=self._faker.address(),
                city=self._faker.city(),
            )
            await asyncio.sleep(1)


async def start_server() -> None:
    logger.info("Start grpc server")
    server = grpc.aio.server()
    add_FakePersonalServiceServicer_to_server(FakePersonalService(), server)
    server.add_insecure_port(config.FAKE_PERSONAL_GRPC_ADDRESS)
    await server.start()
    await server.wait_for_termination()
