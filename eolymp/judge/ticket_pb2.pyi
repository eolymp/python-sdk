from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ticket(_message.Message):
    __slots__ = ["contest_id", "created_at", "cursor", "id", "is_read", "last_reply_at", "member_id", "message", "participant_id", "raw_message", "read_at", "reply_count", "status", "subject", "updated_at"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AWAITING: Ticket.Status
    CLOSED: Ticket.Status
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_READ_FIELD_NUMBER: _ClassVar[int]
    LAST_REPLY_AT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_RENDER: Ticket.Extra
    MESSAGE_VALUE: Ticket.Extra
    NO_EXTRA: Ticket.Extra
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    RAW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    REPLY_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESOLVED: Ticket.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STATUS: Ticket.Status
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    created_at: _timestamp_pb2.Timestamp
    cursor: str
    id: str
    is_read: bool
    last_reply_at: _timestamp_pb2.Timestamp
    member_id: str
    message: _content_pb2.Content
    participant_id: str
    raw_message: str
    read_at: _timestamp_pb2.Timestamp
    reply_count: int
    status: Ticket.Status
    subject: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., member_id: _Optional[str] = ..., status: _Optional[_Union[Ticket.Status, str]] = ..., subject: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., raw_message: _Optional[str] = ..., is_read: bool = ..., reply_count: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., read_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_reply_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cursor: _Optional[str] = ...) -> None: ...
