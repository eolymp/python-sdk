from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ticket(_message.Message):
    __slots__ = ["created_at", "id", "locale", "message", "metadata", "secret", "status", "subject", "type", "updated_at", "user_email", "user_id"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Comment(_message.Message):
        __slots__ = ["created_at", "id", "message", "metadata", "updated_at", "user_email", "user_id"]
        class MetadataEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        created_at: _timestamp_pb2.Timestamp
        id: str
        message: _content_pb2.Content
        metadata: _containers.ScalarMap[str, str]
        updated_at: _timestamp_pb2.Timestamp
        user_email: str
        user_id: str
        def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., user_email: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACADEMIC_PLAN_REQUEST: Ticket.Type
    APPROVED: Ticket.Status
    AWAITING: Ticket.Status
    CLOSED: Ticket.Status
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK: Ticket.Type
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NONE: Ticket.Type
    PENDING: Ticket.Status
    QUESTION: Ticket.Type
    QUOTA_INCREASE: Ticket.Type
    REJECTED: Ticket.Status
    SALES_REQUEST: Ticket.Type
    SECRET_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: Ticket.Status
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    id: str
    locale: str
    message: _content_pb2.Content
    metadata: _containers.ScalarMap[str, str]
    secret: str
    status: Ticket.Status
    subject: str
    type: Ticket.Type
    updated_at: _timestamp_pb2.Timestamp
    user_email: str
    user_id: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[Ticket.Type, str]] = ..., user_id: _Optional[str] = ..., user_email: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., status: _Optional[_Union[Ticket.Status, str]] = ..., locale: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., secret: _Optional[str] = ..., subject: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
