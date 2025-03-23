# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import api.proto.fake_personal_pb2 as fake__personal__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in fake_personal_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FakePersonalServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Generate = channel.unary_unary(
                '/fake_personal.FakePersonalService/Generate',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=fake__personal__pb2.FakePersonal.FromString,
                _registered_method=True)
        self.StreamGenerate = channel.unary_stream(
                '/fake_personal.FakePersonalService/StreamGenerate',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=fake__personal__pb2.FakePersonal.FromString,
                _registered_method=True)


class FakePersonalServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Generate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamGenerate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FakePersonalServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Generate': grpc.unary_unary_rpc_method_handler(
                    servicer.Generate,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=fake__personal__pb2.FakePersonal.SerializeToString,
            ),
            'StreamGenerate': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamGenerate,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=fake__personal__pb2.FakePersonal.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fake_personal.FakePersonalService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('fake_personal.FakePersonalService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FakePersonalService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Generate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/fake_personal.FakePersonalService/Generate',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            fake__personal__pb2.FakePersonal.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StreamGenerate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/fake_personal.FakePersonalService/StreamGenerate',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            fake__personal__pb2.FakePersonal.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
