from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Quota(_message.Message):
    __slots__ = ["unlimited", "value"]
    UNLIMITED_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    unlimited: bool
    value: int
    def __init__(self, value: _Optional[int] = ..., unlimited: bool = ...) -> None: ...
