from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Class(_message.Message):
    __slots__ = ["group_id", "id", "module_count"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MODULE_COUNT_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    id: str
    module_count: int
    def __init__(self, id: _Optional[str] = ..., group_id: _Optional[str] = ..., module_count: _Optional[int] = ...) -> None: ...
