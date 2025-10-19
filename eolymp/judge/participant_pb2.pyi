import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.judge import medal_pb2 as _medal_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Participant(_message.Message):
    __slots__ = ("id", "member_id", "display_name", "role", "unofficial", "inactive", "disqualified", "ghost", "finalized", "medal", "status", "started_at", "end_at", "bonus_time", "violation_count", "passcode", "certificate_id", "submits")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Participant.Status]
        WAITING: _ClassVar[Participant.Status]
        READY: _ClassVar[Participant.Status]
        ACTIVE: _ClassVar[Participant.Status]
        COMPLETE: _ClassVar[Participant.Status]
        UPSOLVE: _ClassVar[Participant.Status]
        BLOCKED: _ClassVar[Participant.Status]
        PAUSED: _ClassVar[Participant.Status]
    UNKNOWN_STATUS: Participant.Status
    WAITING: Participant.Status
    READY: Participant.Status
    ACTIVE: Participant.Status
    COMPLETE: Participant.Status
    UPSOLVE: Participant.Status
    BLOCKED: Participant.Status
    PAUSED: Participant.Status
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARTICIPANT: _ClassVar[Participant.Role]
        STAFF: _ClassVar[Participant.Role]
        TESTER: _ClassVar[Participant.Role]
        AUTHOR: _ClassVar[Participant.Role]
        COORDINATOR: _ClassVar[Participant.Role]
    PARTICIPANT: Participant.Role
    STAFF: Participant.Role
    TESTER: Participant.Role
    AUTHOR: Participant.Role
    COORDINATOR: Participant.Role
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ALL: _ClassVar[Participant.Patch.Field]
            DISPLAY_NAME: _ClassVar[Participant.Patch.Field]
            ROLE: _ClassVar[Participant.Patch.Field]
            BONUS_TIME: _ClassVar[Participant.Patch.Field]
            UNOFFICIAL: _ClassVar[Participant.Patch.Field]
            MEDAL: _ClassVar[Participant.Patch.Field]
            INACTIVE: _ClassVar[Participant.Patch.Field]
            PASSCODE: _ClassVar[Participant.Patch.Field]
        ALL: Participant.Patch.Field
        DISPLAY_NAME: Participant.Patch.Field
        ROLE: Participant.Patch.Field
        BONUS_TIME: Participant.Patch.Field
        UNOFFICIAL: Participant.Patch.Field
        MEDAL: Participant.Patch.Field
        INACTIVE: Participant.Patch.Field
        PASSCODE: Participant.Patch.Field
        def __init__(self) -> None: ...
    class Submit(_message.Message):
        __slots__ = ("problem_id", "counter")
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        COUNTER_FIELD_NUMBER: _ClassVar[int]
        problem_id: str
        counter: int
        def __init__(self, problem_id: _Optional[str] = ..., counter: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
    GHOST_FIELD_NUMBER: _ClassVar[int]
    FINALIZED_FIELD_NUMBER: _ClassVar[int]
    MEDAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    END_AT_FIELD_NUMBER: _ClassVar[int]
    BONUS_TIME_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMITS_FIELD_NUMBER: _ClassVar[int]
    id: str
    member_id: str
    display_name: str
    role: Participant.Role
    unofficial: bool
    inactive: bool
    disqualified: bool
    ghost: bool
    finalized: bool
    medal: _medal_pb2.Medal
    status: Participant.Status
    started_at: _timestamp_pb2.Timestamp
    end_at: _timestamp_pb2.Timestamp
    bonus_time: int
    violation_count: int
    passcode: str
    certificate_id: str
    submits: _containers.RepeatedCompositeFieldContainer[Participant.Submit]
    def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., display_name: _Optional[str] = ..., role: _Optional[_Union[Participant.Role, str]] = ..., unofficial: bool = ..., inactive: bool = ..., disqualified: bool = ..., ghost: bool = ..., finalized: bool = ..., medal: _Optional[_Union[_medal_pb2.Medal, str]] = ..., status: _Optional[_Union[Participant.Status, str]] = ..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., end_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., bonus_time: _Optional[int] = ..., violation_count: _Optional[int] = ..., passcode: _Optional[str] = ..., certificate_id: _Optional[str] = ..., submits: _Optional[_Iterable[_Union[Participant.Submit, _Mapping]]] = ...) -> None: ...
