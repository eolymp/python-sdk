from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Attachment(_message.Message):
    __slots__ = ["id", "link", "name", "problem_id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    link: str
    name: str
    problem_id: str
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., name: _Optional[str] = ..., link: _Optional[str] = ...) -> None: ...
