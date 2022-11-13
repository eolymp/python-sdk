from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Agreement(_message.Message):
    __slots__ = ["description", "id", "required", "summary"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    required: bool
    summary: str
    def __init__(self, id: _Optional[str] = ..., required: bool = ..., summary: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
