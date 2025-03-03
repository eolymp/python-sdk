from eolymp.community import email_type_pb2 as _email_type_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Campaign(_message.Message):
    __slots__ = ("id", "type", "created_at", "name", "subject", "content", "recipients_count", "pending_count", "sent_count", "error_count")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[Campaign.Patch]
        TYPE: _ClassVar[Campaign.Patch]
        NAME: _ClassVar[Campaign.Patch]
        SUBJECT: _ClassVar[Campaign.Patch]
        CONTENT: _ClassVar[Campaign.Patch]
        LOCALE: _ClassVar[Campaign.Patch]
    ALL: Campaign.Patch
    TYPE: Campaign.Patch
    NAME: Campaign.Patch
    SUBJECT: Campaign.Patch
    CONTENT: Campaign.Patch
    LOCALE: Campaign.Patch
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[Campaign.Extra]
        CONTENT_VALUE: _ClassVar[Campaign.Extra]
        CONTENT_RENDER: _ClassVar[Campaign.Extra]
    UNKNOWN_EXTRA: Campaign.Extra
    CONTENT_VALUE: Campaign.Extra
    CONTENT_RENDER: Campaign.Extra
    class Translation(_message.Message):
        __slots__ = ("id", "locale", "subject", "content", "automatic")
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        id: str
        locale: str
        subject: str
        content: _content_pb2.Content
        automatic: bool
        def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., subject: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., automatic: bool = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    PENDING_COUNT_FIELD_NUMBER: _ClassVar[int]
    SENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: _email_type_pb2.EmailType
    created_at: _timestamp_pb2.Timestamp
    name: str
    subject: str
    content: _content_pb2.Content
    recipients_count: int
    pending_count: int
    sent_count: int
    error_count: int
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[_email_type_pb2.EmailType, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., subject: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., recipients_count: _Optional[int] = ..., pending_count: _Optional[int] = ..., sent_count: _Optional[int] = ..., error_count: _Optional[int] = ...) -> None: ...
