from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Figure(_message.Message):
    __slots__ = ("name", "url", "alt", "pages")
    NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ALT_FIELD_NUMBER: _ClassVar[int]
    PAGES_FIELD_NUMBER: _ClassVar[int]
    name: str
    url: str
    alt: str
    pages: int
    def __init__(self, name: _Optional[str] = ..., url: _Optional[str] = ..., alt: _Optional[str] = ..., pages: _Optional[int] = ...) -> None: ...
