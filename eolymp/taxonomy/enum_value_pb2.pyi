from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Value(_message.Message):
    __slots__ = ["abbr", "id", "image", "keywords", "name", "summary"]
    class Translation(_message.Message):
        __slots__ = ["abbr", "keywords", "locale", "name", "summary"]
        ABBR_FIELD_NUMBER: _ClassVar[int]
        KEYWORDS_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        abbr: str
        keywords: _containers.RepeatedScalarFieldContainer[str]
        locale: str
        name: str
        summary: str
        def __init__(self, locale: _Optional[str] = ..., name: _Optional[str] = ..., abbr: _Optional[str] = ..., summary: _Optional[str] = ..., keywords: _Optional[_Iterable[str]] = ...) -> None: ...
    ABBR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    abbr: str
    id: str
    image: str
    keywords: _containers.RepeatedScalarFieldContainer[str]
    name: str
    summary: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., summary: _Optional[str] = ..., abbr: _Optional[str] = ..., image: _Optional[str] = ..., keywords: _Optional[_Iterable[str]] = ...) -> None: ...
