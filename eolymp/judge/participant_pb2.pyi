from eolymp.judge import medal_pb2 as _medal_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Participant(_message.Message):
    __slots__ = ("id", "member_id", "display_name", "unofficial", "inactive", "disqualified", "ghost", "medal", "status", "started_at", "started_in", "end_at", "end_in", "bonus_time", "passcode", "submits")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Participant.Status]
        WAITING: _ClassVar[Participant.Status]
        READY: _ClassVar[Participant.Status]
        ACTIVE: _ClassVar[Participant.Status]
        COMPLETE: _ClassVar[Participant.Status]
        UPSOLVE: _ClassVar[Participant.Status]
        BLOCKED: _ClassVar[Participant.Status]
    UNKNOWN_STATUS: Participant.Status
    WAITING: Participant.Status
    READY: Participant.Status
    ACTIVE: Participant.Status
    COMPLETE: Participant.Status
    UPSOLVE: Participant.Status
    BLOCKED: Participant.Status
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
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
    GHOST_FIELD_NUMBER: _ClassVar[int]
    MEDAL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_IN_FIELD_NUMBER: _ClassVar[int]
    END_AT_FIELD_NUMBER: _ClassVar[int]
    END_IN_FIELD_NUMBER: _ClassVar[int]
    BONUS_TIME_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    SUBMITS_FIELD_NUMBER: _ClassVar[int]
    id: str
    member_id: str
    display_name: str
    unofficial: bool
    inactive: bool
    disqualified: bool
    ghost: bool
    medal: _medal_pb2.Medal
    status: Participant.Status
    started_at: _timestamp_pb2.Timestamp
    started_in: int
    end_at: _timestamp_pb2.Timestamp
    end_in: int
    bonus_time: int
    passcode: str
    submits: _containers.RepeatedCompositeFieldContainer[Participant.Submit]
    def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., display_name: _Optional[str] = ..., unofficial: bool = ..., inactive: bool = ..., disqualified: bool = ..., ghost: bool = ..., medal: _Optional[_Union[_medal_pb2.Medal, str]] = ..., status: _Optional[_Union[Participant.Status, str]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_in: _Optional[int] = ..., end_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_in: _Optional[int] = ..., bonus_time: _Optional[int] = ..., passcode: _Optional[str] = ..., submits: _Optional[_Iterable[_Union[Participant.Submit, _Mapping]]] = ...) -> None: ...
