from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Team(_message.Message):
    __slots__ = ["name", "staffed"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STAFFED_FIELD_NUMBER: _ClassVar[int]
    name: str
    staffed: bool
    def __init__(self, name: _Optional[str] = ..., staffed: bool = ...) -> None: ...
