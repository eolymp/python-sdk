import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Invitation(_message.Message):
    __slots__ = ("id", "team_id", "member_id", "inviter_id", "status", "created_at", "expires_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Invitation.Status]
        PENDING: _ClassVar[Invitation.Status]
        ACCEPTED: _ClassVar[Invitation.Status]
        DECLINED: _ClassVar[Invitation.Status]
        REVOKED: _ClassVar[Invitation.Status]
        EXPIRED: _ClassVar[Invitation.Status]
    UNKNOWN_STATUS: Invitation.Status
    PENDING: Invitation.Status
    ACCEPTED: Invitation.Status
    DECLINED: Invitation.Status
    REVOKED: Invitation.Status
    EXPIRED: Invitation.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    TEAM_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    INVITER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    team_id: str
    member_id: str
    inviter_id: str
    status: Invitation.Status
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., team_id: _Optional[str] = ..., member_id: _Optional[str] = ..., inviter_id: _Optional[str] = ..., status: _Optional[_Union[Invitation.Status, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
