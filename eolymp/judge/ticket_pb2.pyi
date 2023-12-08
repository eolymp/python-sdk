from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ticket(_message.Message):
    __slots__ = ["contest_id", "created_at", "ern", "id", "is_open", "is_read", "is_read_by_owner", "is_read_by_participant", "member_id", "message", "needs_reply", "participant_id", "raw_message", "subject"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ERN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    IS_READ_BY_OWNER_FIELD_NUMBER: _ClassVar[int]
    IS_READ_BY_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    IS_READ_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_RENDER: Ticket.Extra
    MESSAGE_VALUE: Ticket.Extra
    NEEDS_REPLY_FIELD_NUMBER: _ClassVar[int]
    NO_EXTRA: Ticket.Extra
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    RAW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    created_at: _timestamp_pb2.Timestamp
    ern: str
    id: str
    is_open: bool
    is_read: bool
    is_read_by_owner: bool
    is_read_by_participant: bool
    member_id: str
    message: _content_pb2.Content
    needs_reply: bool
    participant_id: str
    raw_message: str
    subject: str
    def __init__(self, id: _Optional[str] = ..., ern: _Optional[str] = ..., contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., member_id: _Optional[str] = ..., subject: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., raw_message: _Optional[str] = ..., is_open: bool = ..., is_read_by_participant: bool = ..., is_read_by_owner: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_read: bool = ..., needs_reply: bool = ...) -> None: ...
