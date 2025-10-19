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
    __slots__ = ("id", "path", "locale", "draft", "title", "content", "created_at", "updated_at", "labels")
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
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_PATCH: _ClassVar[Fragment.Patch.Field]
            PATH: _ClassVar[Fragment.Patch.Field]
            LOCALE: _ClassVar[Fragment.Patch.Field]
            DRAFT: _ClassVar[Fragment.Patch.Field]
            TITLE: _ClassVar[Fragment.Patch.Field]
            CONTENT: _ClassVar[Fragment.Patch.Field]
            LABELS: _ClassVar[Fragment.Patch.Field]
        UNKNOWN_PATCH: Fragment.Patch.Field
        PATH: Fragment.Patch.Field
        LOCALE: Fragment.Patch.Field
        DRAFT: Fragment.Patch.Field
        TITLE: Fragment.Patch.Field
        CONTENT: Fragment.Patch.Field
        LABELS: Fragment.Patch.Field
        def __init__(self) -> None: ...
    class Translation(_message.Message):
        __slots__ = ("id", "locale", "title", "content", "automatic")
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        id: str
        locale: str
        title: str
        content: _content_pb2.Content
        automatic: bool
        def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., automatic: bool = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    path: str
    locale: str
    draft: bool
    title: str
    content: _content_pb2.Content
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., path: _Optional[str] = ..., locale: _Optional[str] = ..., draft: bool = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...
