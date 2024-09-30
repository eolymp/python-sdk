from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Class(_message.Message):
    __slots__ = ["assign_all", "group_id", "id", "inactive", "name"]
    ASSIGN_ALL_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    assign_all: bool
    group_id: str
    id: str
    inactive: bool
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., group_id: _Optional[str] = ..., inactive: bool = ..., assign_all: bool = ...) -> None: ...
