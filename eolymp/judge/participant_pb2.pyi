from eolymp.judge import medal_pb2 as _medal_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Participant(_message.Message):
    __slots__ = ["bonus_time", "contest_id", "disqualified", "end_at", "end_in", "ghost", "id", "inactive", "medal", "member_id", "name", "passcode", "started_at", "started_in", "status", "submits", "unofficial"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Submit(_message.Message):
        __slots__ = ["counter", "problem_id"]
        COUNTER_FIELD_NUMBER: _ClassVar[int]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        counter: int
        problem_id: str
        def __init__(self, problem_id: _Optional[str] = ..., counter: _Optional[int] = ...) -> None: ...
    ACTIVE: Participant.Status
    BLOCKED: Participant.Status
    BONUS_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: Participant.Status
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
    END_AT_FIELD_NUMBER: _ClassVar[int]
    END_IN_FIELD_NUMBER: _ClassVar[int]
    GHOST_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    MEDAL_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    READY: Participant.Status
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_IN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBMITS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STATUS: Participant.Status
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    UPSOLVE: Participant.Status
    WAITING: Participant.Status
    bonus_time: int
    contest_id: str
    disqualified: bool
    end_at: _timestamp_pb2.Timestamp
    end_in: int
    ghost: bool
    id: str
    inactive: bool
    medal: _medal_pb2.Medal
    member_id: str
    name: str
    passcode: str
    started_at: _timestamp_pb2.Timestamp
    started_in: int
    status: Participant.Status
    submits: _containers.RepeatedCompositeFieldContainer[Participant.Submit]
    unofficial: bool
    def __init__(self, id: _Optional[str] = ..., contest_id: _Optional[str] = ..., member_id: _Optional[str] = ..., name: _Optional[str] = ..., unofficial: bool = ..., inactive: bool = ..., disqualified: bool = ..., ghost: bool = ..., medal: _Optional[_Union[_medal_pb2.Medal, str]] = ..., status: _Optional[_Union[Participant.Status, str]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_in: _Optional[int] = ..., end_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_in: _Optional[int] = ..., bonus_time: _Optional[int] = ..., passcode: _Optional[str] = ..., submits: _Optional[_Iterable[_Union[Participant.Submit, _Mapping]]] = ...) -> None: ...
