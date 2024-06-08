from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Region(_message.Message):
    __slots__ = ["country_id", "flag_url", "id", "local_name", "name"]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    FLAG_URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    country_id: str
    flag_url: str
    id: str
    local_name: str
    name: str
    def __init__(self, id: _Optional[str] = ..., country_id: _Optional[str] = ..., name: _Optional[str] = ..., local_name: _Optional[str] = ..., flag_url: _Optional[str] = ...) -> None: ...
