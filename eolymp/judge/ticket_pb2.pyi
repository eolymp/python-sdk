from eolymp.annotations import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ticket(_message.Message):
    __slots__ = ["contest_id", "created_at", "ern", "id", "is_open", "is_read", "is_read_by_owner", "is_read_by_participant", "message", "needs_reply", "participant_id", "subject"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ERN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_OPEN_FIELD_NUMBER: _ClassVar[int]
    IS_READ_BY_OWNER_FIELD_NUMBER: _ClassVar[int]
    IS_READ_BY_PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    IS_READ_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NEEDS_REPLY_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    created_at: _timestamp_pb2.Timestamp
    ern: str
    id: str
    is_open: bool
    is_read: bool
    is_read_by_owner: bool
    is_read_by_participant: bool
    message: str
    needs_reply: bool
    participant_id: str
    subject: str
    def __init__(self, id: _Optional[str] = ..., ern: _Optional[str] = ..., contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., subject: _Optional[str] = ..., message: _Optional[str] = ..., is_open: bool = ..., is_read_by_participant: bool = ..., is_read_by_owner: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_read: bool = ..., needs_reply: bool = ...) -> None: ...
