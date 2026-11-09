import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Sitemap(_message.Message):
    __slots__ = ()
    class Chunk(_message.Message):
        __slots__ = ("id", "size", "updated_at")
        ID_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        id: str
        size: int
        updated_at: _timestamp_pb2.Timestamp
        def __init__(self, id: _Optional[str] = ..., size: _Optional[int] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Entry(_message.Message):
        __slots__ = ("type", "resource_link", "title", "languages", "image_link", "attributes", "created_at", "updated_at")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_TYPE: _ClassVar[Sitemap.Entry.Type]
            PROBLEM: _ClassVar[Sitemap.Entry.Type]
            PROBLEM_EDITORIAL: _ClassVar[Sitemap.Entry.Type]
            CONTEST: _ClassVar[Sitemap.Entry.Type]
            CONTEST_PAGE: _ClassVar[Sitemap.Entry.Type]
            CONTEST_SCOREBOARD: _ClassVar[Sitemap.Entry.Type]
            COURSE: _ClassVar[Sitemap.Entry.Type]
            COURSE_MODULE: _ClassVar[Sitemap.Entry.Type]
            COURSE_MATERIAL: _ClassVar[Sitemap.Entry.Type]
            POST: _ClassVar[Sitemap.Entry.Type]
            PAGE: _ClassVar[Sitemap.Entry.Type]
            MEMBER: _ClassVar[Sitemap.Entry.Type]
            PRODUCT: _ClassVar[Sitemap.Entry.Type]
        UNKNOWN_TYPE: Sitemap.Entry.Type
        PROBLEM: Sitemap.Entry.Type
        PROBLEM_EDITORIAL: Sitemap.Entry.Type
        CONTEST: Sitemap.Entry.Type
        CONTEST_PAGE: Sitemap.Entry.Type
        CONTEST_SCOREBOARD: Sitemap.Entry.Type
        COURSE: Sitemap.Entry.Type
        COURSE_MODULE: Sitemap.Entry.Type
        COURSE_MATERIAL: Sitemap.Entry.Type
        POST: Sitemap.Entry.Type
        PAGE: Sitemap.Entry.Type
        MEMBER: Sitemap.Entry.Type
        PRODUCT: Sitemap.Entry.Type
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
        type: Sitemap.Entry.Type
        resource_link: str
        title: str
        languages: _containers.RepeatedScalarFieldContainer[str]
        image_link: str
        attributes: _containers.ScalarMap[str, str]
        created_at: _timestamp_pb2.Timestamp
        updated_at: _timestamp_pb2.Timestamp
        def __init__(self, type: _Optional[_Union[Sitemap.Entry.Type, str]] = ..., resource_link: _Optional[str] = ..., title: _Optional[str] = ..., languages: _Optional[_Iterable[str]] = ..., image_link: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
