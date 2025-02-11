from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ("country", "state", "postal_code", "city", "line1", "line2")
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    LINE1_FIELD_NUMBER: _ClassVar[int]
    LINE2_FIELD_NUMBER: _ClassVar[int]
    country: str
    state: str
    postal_code: str
    city: str
    line1: str
    line2: str
    def __init__(self, country: _Optional[str] = ..., state: _Optional[str] = ..., postal_code: _Optional[str] = ..., city: _Optional[str] = ..., line1: _Optional[str] = ..., line2: _Optional[str] = ...) -> None: ...
