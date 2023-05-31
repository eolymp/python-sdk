from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Locale(_message.Message):
    __slots__ = ["code", "completeness"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    COMPLETENESS_FIELD_NUMBER: _ClassVar[int]
    code: str
    completeness: float
    def __init__(self, code: _Optional[str] = ..., completeness: _Optional[float] = ...) -> None: ...
