from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ["city", "country", "lines", "post_code", "region"]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    POST_CODE_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    city: str
    country: str
    lines: _containers.RepeatedScalarFieldContainer[str]
    post_code: str
    region: str
    def __init__(self, country: _Optional[str] = ..., post_code: _Optional[str] = ..., region: _Optional[str] = ..., city: _Optional[str] = ..., lines: _Optional[_Iterable[str]] = ...) -> None: ...
