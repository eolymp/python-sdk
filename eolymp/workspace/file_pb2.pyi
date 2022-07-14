from eolymp.annotations import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class File(_message.Message):
    __slots__ = ["content", "ern", "name"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ERN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    content: bytes
    ern: str
    name: str
    def __init__(self, ern: _Optional[str] = ..., name: _Optional[str] = ..., content: _Optional[bytes] = ...) -> None: ...
