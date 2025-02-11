from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ticket(_message.Message):
    __slots__ = ("id", "contest_id", "participant_id", "member_id", "status", "subject", "message", "raw_message", "is_read", "reply_count", "created_at", "updated_at", "read_at", "last_reply_at", "cursor")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTRA: _ClassVar[Ticket.Extra]
        MESSAGE_RENDER: _ClassVar[Ticket.Extra]
        MESSAGE_VALUE: _ClassVar[Ticket.Extra]
    NO_EXTRA: Ticket.Extra
    MESSAGE_RENDER: Ticket.Extra
    MESSAGE_VALUE: Ticket.Extra
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Ticket.Status]
        AWAITING: _ClassVar[Ticket.Status]
        RESOLVED: _ClassVar[Ticket.Status]
        CLOSED: _ClassVar[Ticket.Status]
    UNKNOWN_STATUS: Ticket.Status
    AWAITING: Ticket.Status
    RESOLVED: Ticket.Status
    CLOSED: Ticket.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RAW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IS_READ_FIELD_NUMBER: _ClassVar[int]
    REPLY_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_REPLY_AT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    contest_id: str
    participant_id: str
    member_id: str
    status: Ticket.Status
    subject: str
    message: _content_pb2.Content
    raw_message: str
    is_read: bool
    reply_count: int
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    read_at: _timestamp_pb2.Timestamp
    last_reply_at: _timestamp_pb2.Timestamp
    cursor: str
    def __init__(self, id: _Optional[str] = ..., contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., member_id: _Optional[str] = ..., status: _Optional[_Union[Ticket.Status, str]] = ..., subject: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., raw_message: _Optional[str] = ..., is_read: bool = ..., reply_count: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., read_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_reply_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cursor: _Optional[str] = ...) -> None: ...
