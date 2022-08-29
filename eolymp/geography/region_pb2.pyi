from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Region(_message.Message):
    __slots__ = ["country", "flag", "id", "name"]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    country: str
    flag: str
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., country: _Optional[str] = ..., name: _Optional[str] = ..., flag: _Optional[str] = ...) -> None: ...
