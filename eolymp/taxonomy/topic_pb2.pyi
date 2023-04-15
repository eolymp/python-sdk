from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Topic(_message.Message):
    __slots__ = ["descriptors", "id"]
    class Descriptor(_message.Message):
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
    DESCRIPTORS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    descriptors: _containers.RepeatedCompositeFieldContainer[Topic.Descriptor]
    id: str
    def __init__(self, id: _Optional[str] = ..., descriptors: _Optional[_Iterable[_Union[Topic.Descriptor, _Mapping]]] = ...) -> None: ...
