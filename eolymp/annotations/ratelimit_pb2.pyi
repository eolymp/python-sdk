from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
RATELIMIT_FIELD_NUMBER: _ClassVar[int]
ratelimit: _descriptor.FieldDescriptor

class RateLimit(_message.Message):
    __slots__ = ("limit", "burst")
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    BURST_FIELD_NUMBER: _ClassVar[int]
    limit: float
    burst: int
    def __init__(self, limit: _Optional[float] = ..., burst: _Optional[int] = ...) -> None: ...
