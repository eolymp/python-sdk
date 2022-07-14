from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
SERVICE_FIELD_NUMBER: _ClassVar[int]
service: _descriptor.FieldDescriptor

class Service(_message.Message):
    __slots__ = ["internal", "space"]
    INTERNAL_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    internal: bool
    space: bool
    def __init__(self, space: bool = ..., internal: bool = ...) -> None: ...
