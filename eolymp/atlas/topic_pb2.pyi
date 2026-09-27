from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Topic(_message.Message):
    __slots__ = ("id", "name", "summary", "keywords", "variants")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[Topic.Extra]
        VARIANTS: _ClassVar[Topic.Extra]
    UNKNOWN_EXTRA: Topic.Extra
    VARIANTS: Topic.Extra
    class Variant(_message.Message):
        __slots__ = ("locale", "name", "summary", "keywords")
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        KEYWORDS_FIELD_NUMBER: _ClassVar[int]
        locale: str
        name: str
        summary: str
        keywords: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, locale: _Optional[str] = ..., name: _Optional[str] = ..., summary: _Optional[str] = ..., keywords: _Optional[_Iterable[str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    summary: str
    keywords: _containers.RepeatedScalarFieldContainer[str]
    variants: _containers.RepeatedCompositeFieldContainer[Topic.Variant]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., summary: _Optional[str] = ..., keywords: _Optional[_Iterable[str]] = ..., variants: _Optional[_Iterable[_Union[Topic.Variant, _Mapping]]] = ...) -> None: ...
