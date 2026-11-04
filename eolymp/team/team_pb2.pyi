import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Team(_message.Message):
    __slots__ = ("id", "name", "captain_id", "members", "disbanded", "created_at", "disbanded_at")
    class Patch(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class Member(_message.Message):
        __slots__ = ("member_id", "joined_at")
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        JOINED_AT_FIELD_NUMBER: _ClassVar[int]
        member_id: str
        joined_at: _timestamp_pb2.Timestamp
        def __init__(self, member_id: _Optional[str] = ..., joined_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CAPTAIN_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    DISBANDED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DISBANDED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    captain_id: str
    members: _containers.RepeatedCompositeFieldContainer[Team.Member]
    disbanded: bool
    created_at: _timestamp_pb2.Timestamp
    disbanded_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., captain_id: _Optional[str] = ..., members: _Optional[_Iterable[_Union[Team.Member, _Mapping]]] = ..., disbanded: _Optional[bool] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., disbanded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
