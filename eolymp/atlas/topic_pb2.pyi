from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Topic(_message.Message):
    __slots__ = ("id", "name", "summary", "keywords", "description", "locale", "locales", "variants")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[Topic.Extra]
        VARIANTS: _ClassVar[Topic.Extra]
        DESCRIPTION_VALUE: _ClassVar[Topic.Extra]
        DESCRIPTION_RENDER: _ClassVar[Topic.Extra]
    UNKNOWN_EXTRA: Topic.Extra
    VARIANTS: Topic.Extra
    DESCRIPTION_VALUE: Topic.Extra
    DESCRIPTION_RENDER: Topic.Extra
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
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    LOCALES_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    summary: str
    keywords: _containers.RepeatedScalarFieldContainer[str]
    description: _content_pb2.Content
    locale: str
    locales: _containers.RepeatedScalarFieldContainer[str]
    variants: _containers.RepeatedCompositeFieldContainer[Topic.Variant]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., summary: _Optional[str] = ..., keywords: _Optional[_Iterable[str]] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., locale: _Optional[str] = ..., locales: _Optional[_Iterable[str]] = ..., variants: _Optional[_Iterable[_Union[Topic.Variant, _Mapping]]] = ...) -> None: ...
