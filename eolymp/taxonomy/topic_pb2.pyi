from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Topic(_message.Message):
    __slots__ = ["id", "keywords", "name", "summary"]
    class Translation(_message.Message):
        __slots__ = ["keywords", "locale", "name", "summary"]
        KEYWORDS_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        keywords: _containers.RepeatedScalarFieldContainer[str]
        locale: str
        name: str
        summary: str
        def __init__(self, locale: _Optional[str] = ..., name: _Optional[str] = ..., summary: _Optional[str] = ..., keywords: _Optional[_Iterable[str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    id: str
    keywords: _containers.RepeatedScalarFieldContainer[str]
    name: str
    summary: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., summary: _Optional[str] = ..., keywords: _Optional[_Iterable[str]] = ...) -> None: ...
