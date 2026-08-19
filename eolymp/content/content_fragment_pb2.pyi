import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Fragment(_message.Message):
    __slots__ = ("id", "resource_link", "space_link", "console_link", "path", "locale", "locales", "draft", "automatic", "visibility", "title", "content", "created_at", "updated_at", "labels")
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VISIBILITY_UNKNOWN: _ClassVar[Fragment.Visibility]
        PUBLIC: _ClassVar[Fragment.Visibility]
        PRIVATE: _ClassVar[Fragment.Visibility]
    VISIBILITY_UNKNOWN: Fragment.Visibility
    PUBLIC: Fragment.Visibility
    PRIVATE: Fragment.Visibility
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_EXTRA: _ClassVar[Fragment.Extra.Field]
            CONTENT_RENDER: _ClassVar[Fragment.Extra.Field]
            CONTENT_VALUE: _ClassVar[Fragment.Extra.Field]
        UNKNOWN_EXTRA: Fragment.Extra.Field
        CONTENT_RENDER: Fragment.Extra.Field
        CONTENT_VALUE: Fragment.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ("path", "draft", "automatic", "title", "visibility", "content", "labels", "unlabel")
        PATH_FIELD_NUMBER: _ClassVar[int]
        DRAFT_FIELD_NUMBER: _ClassVar[int]
        AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        VISIBILITY_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        UNLABEL_FIELD_NUMBER: _ClassVar[int]
        path: str
        draft: bool
        automatic: bool
        title: str
        visibility: Fragment.Visibility
        content: _content_pb2.Content
        labels: _containers.RepeatedScalarFieldContainer[str]
        unlabel: bool
        def __init__(self, path: _Optional[str] = ..., draft: _Optional[bool] = ..., automatic: _Optional[bool] = ..., title: _Optional[str] = ..., visibility: _Optional[_Union[Fragment.Visibility, str]] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., labels: _Optional[_Iterable[str]] = ..., unlabel: _Optional[bool] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_LINK_FIELD_NUMBER: _ClassVar[int]
    SPACE_LINK_FIELD_NUMBER: _ClassVar[int]
    CONSOLE_LINK_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    LOCALES_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    resource_link: str
    space_link: str
    console_link: str
    path: str
    locale: str
    locales: _containers.RepeatedScalarFieldContainer[str]
    draft: bool
    automatic: bool
    visibility: Fragment.Visibility
    title: str
    content: _content_pb2.Content
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., resource_link: _Optional[str] = ..., space_link: _Optional[str] = ..., console_link: _Optional[str] = ..., path: _Optional[str] = ..., locale: _Optional[str] = ..., locales: _Optional[_Iterable[str]] = ..., draft: _Optional[bool] = ..., automatic: _Optional[bool] = ..., visibility: _Optional[_Union[Fragment.Visibility, str]] = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...
