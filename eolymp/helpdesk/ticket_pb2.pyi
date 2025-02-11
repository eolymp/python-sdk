from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ticket(_message.Message):
    __slots__ = ("id", "type", "user_id", "user_email", "metadata", "status", "locale", "created_at", "updated_at", "secret", "subject", "message")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Ticket.Type]
        QUESTION: _ClassVar[Ticket.Type]
        QUOTA_INCREASE: _ClassVar[Ticket.Type]
        FEEDBACK: _ClassVar[Ticket.Type]
        ACADEMIC_PLAN_REQUEST: _ClassVar[Ticket.Type]
        SALES_REQUEST: _ClassVar[Ticket.Type]
    NONE: Ticket.Type
    QUESTION: Ticket.Type
    QUOTA_INCREASE: Ticket.Type
    FEEDBACK: Ticket.Type
    ACADEMIC_PLAN_REQUEST: Ticket.Type
    SALES_REQUEST: Ticket.Type
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Ticket.Status]
        PENDING: _ClassVar[Ticket.Status]
        AWAITING: _ClassVar[Ticket.Status]
        CLOSED: _ClassVar[Ticket.Status]
        APPROVED: _ClassVar[Ticket.Status]
        REJECTED: _ClassVar[Ticket.Status]
    UNKNOWN: Ticket.Status
    PENDING: Ticket.Status
    AWAITING: Ticket.Status
    CLOSED: Ticket.Status
    APPROVED: Ticket.Status
    REJECTED: Ticket.Status
    class Comment(_message.Message):
        __slots__ = ("id", "user_id", "user_email", "metadata", "created_at", "updated_at", "message")
        class MetadataEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        id: str
        user_id: str
        user_email: str
        metadata: _containers.ScalarMap[str, str]
        created_at: _timestamp_pb2.Timestamp
        updated_at: _timestamp_pb2.Timestamp
        message: _content_pb2.Content
        def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., user_email: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: Ticket.Type
    user_id: str
    user_email: str
    metadata: _containers.ScalarMap[str, str]
    status: Ticket.Status
    locale: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    secret: str
    subject: str
    message: _content_pb2.Content
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[Ticket.Type, str]] = ..., user_id: _Optional[str] = ..., user_email: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., status: _Optional[_Union[Ticket.Status, str]] = ..., locale: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., secret: _Optional[str] = ..., subject: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
