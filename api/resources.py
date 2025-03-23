from api.proto.fake_personal_pb2_grpc import FakePersonalServiceStub
from grpc.aio import insecure_channel
from api.config import config


class Resources:
    @classmethod
    def setup(cls):
        fake_personal_channel = insecure_channel(config.FAKE_PERSONAL_GRPC_ADDRESS)
        cls.fake_personal_stub = FakePersonalServiceStub(fake_personal_channel)
