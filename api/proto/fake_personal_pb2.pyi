from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FakePersonal(_message.Message):
    __slots__ = ("name", "address", "city")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    address: str
    city: str
    def __init__(self, name: _Optional[str] = ..., address: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...
