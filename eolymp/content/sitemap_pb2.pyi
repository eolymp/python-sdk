import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SitemapEntry(_message.Message):
    __slots__ = ("type", "resource_link", "title", "languages", "image_link", "attributes", "created_at", "updated_at")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TYPE: _ClassVar[SitemapEntry.Type]
        PROBLEM: _ClassVar[SitemapEntry.Type]
        PROBLEM_EDITORIAL: _ClassVar[SitemapEntry.Type]
        CONTEST: _ClassVar[SitemapEntry.Type]
        CONTEST_PAGE: _ClassVar[SitemapEntry.Type]
        CONTEST_SCOREBOARD: _ClassVar[SitemapEntry.Type]
        SCOREBOARD: _ClassVar[SitemapEntry.Type]
        COURSE: _ClassVar[SitemapEntry.Type]
        COURSE_MODULE: _ClassVar[SitemapEntry.Type]
        COURSE_MATERIAL: _ClassVar[SitemapEntry.Type]
        POST: _ClassVar[SitemapEntry.Type]
        PAGE: _ClassVar[SitemapEntry.Type]
        MEMBER: _ClassVar[SitemapEntry.Type]
        PRODUCT: _ClassVar[SitemapEntry.Type]
    UNKNOWN_TYPE: SitemapEntry.Type
    PROBLEM: SitemapEntry.Type
    PROBLEM_EDITORIAL: SitemapEntry.Type
    CONTEST: SitemapEntry.Type
    CONTEST_PAGE: SitemapEntry.Type
    CONTEST_SCOREBOARD: SitemapEntry.Type
    SCOREBOARD: SitemapEntry.Type
    COURSE: SitemapEntry.Type
    COURSE_MODULE: SitemapEntry.Type
    COURSE_MATERIAL: SitemapEntry.Type
    POST: SitemapEntry.Type
    PAGE: SitemapEntry.Type
    MEMBER: SitemapEntry.Type
    PRODUCT: SitemapEntry.Type
    class AttributesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LINK_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    IMAGE_LINK_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    type: SitemapEntry.Type
    resource_link: str
    title: str
    languages: _containers.RepeatedScalarFieldContainer[str]
    image_link: str
    attributes: _containers.ScalarMap[str, str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, type: _Optional[_Union[SitemapEntry.Type, str]] = ..., resource_link: _Optional[str] = ..., title: _Optional[str] = ..., languages: _Optional[_Iterable[str]] = ..., image_link: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
