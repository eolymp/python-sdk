from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.auth import claims_pb2 as _claims_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HandleSecurityEventInput(_message.Message):
    __slots__ = ["security_event"]
    SECURITY_EVENT_FIELD_NUMBER: _ClassVar[int]
    security_event: str
    def __init__(self, security_event: _Optional[str] = ...) -> None: ...

class HandleSecurityEventOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
