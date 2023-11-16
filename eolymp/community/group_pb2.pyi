from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Group(_message.Message):
    __slots__ = ["description", "id", "name", "tier_id"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIER_ID_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    name: str
    tier_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., tier_id: _Optional[str] = ...) -> None: ...
