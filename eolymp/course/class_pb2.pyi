from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Class(_message.Message):
    __slots__ = ("id", "group_id", "module_count")
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    group_id: str
    module_count: int
    def __init__(self, id: _Optional[str] = ..., group_id: _Optional[str] = ..., module_count: _Optional[int] = ...) -> None: ...
