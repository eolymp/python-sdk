from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AppearanceConfig(_message.Message):
    __slots__ = ["description", "logo_url", "title"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    description: str
    logo_url: str
    title: str
    def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., logo_url: _Optional[str] = ...) -> None: ...
