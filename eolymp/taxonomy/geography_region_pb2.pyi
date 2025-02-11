from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Region(_message.Message):
    __slots__ = ("id", "country_id", "name", "local_name", "flag_url")
    ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCAL_NAME_FIELD_NUMBER: _ClassVar[int]
    FLAG_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    country_id: str
    name: str
    local_name: str
    flag_url: str
    def __init__(self, id: _Optional[str] = ..., country_id: _Optional[str] = ..., name: _Optional[str] = ..., local_name: _Optional[str] = ..., flag_url: _Optional[str] = ...) -> None: ...
