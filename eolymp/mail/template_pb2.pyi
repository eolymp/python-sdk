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

class Template(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "key", "draft", "subject", "content", "automatic", "locale", "alternative_locales")
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_EXTRA: _ClassVar[Template.Extra.Field]
            CONTENT_VALUE: _ClassVar[Template.Extra.Field]
            CONTENT_RENDER: _ClassVar[Template.Extra.Field]
        UNKNOWN_EXTRA: Template.Extra.Field
        CONTENT_VALUE: Template.Extra.Field
        CONTENT_RENDER: Template.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ("key", "draft", "subject", "content", "automatic")
        KEY_FIELD_NUMBER: _ClassVar[int]
        DRAFT_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        key: str
        draft: bool
        subject: str
        content: _content_pb2.Content
        automatic: bool
        def __init__(self, key: _Optional[str] = ..., draft: _Optional[bool] = ..., subject: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., automatic: _Optional[bool] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    ALTERNATIVE_LOCALES_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    key: str
    draft: bool
    subject: str
    content: _content_pb2.Content
    automatic: bool
    locale: str
    alternative_locales: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., key: _Optional[str] = ..., draft: _Optional[bool] = ..., subject: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., automatic: _Optional[bool] = ..., locale: _Optional[str] = ..., alternative_locales: _Optional[_Iterable[str]] = ...) -> None: ...
