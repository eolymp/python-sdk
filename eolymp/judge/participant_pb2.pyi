from eolymp.annotations import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Participant(_message.Message):
    __slots__ = ["bonus_time", "complete_at", "complete_in", "contest_id", "end_at", "end_in", "ern", "id", "member_id", "name", "out_of_competition", "passcode", "started_at", "started_in", "status", "submits"]
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
    BONUS_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETE: Participant.Status
    COMPLETE_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_IN_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    END_AT_FIELD_NUMBER: _ClassVar[int]
    END_IN_FIELD_NUMBER: _ClassVar[int]
    ERN_FIELD_NUMBER: _ClassVar[int]
    GHOST: Participant.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE: Participant.Status
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NONE: Participant.Status
    OUT_OF_COMPETITION_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    READY: Participant.Status
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_IN_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBMITS_FIELD_NUMBER: _ClassVar[int]
    UNREGISTERED: Participant.Status
    bonus_time: int
    complete_at: _timestamp_pb2.Timestamp
    complete_in: int
    contest_id: str
    end_at: _timestamp_pb2.Timestamp
    end_in: int
    ern: str
    id: str
    member_id: str
    name: str
    out_of_competition: bool
    passcode: str
    started_at: _timestamp_pb2.Timestamp
    started_in: int
    status: Participant.Status
    submits: _containers.RepeatedCompositeFieldContainer[Participant.Submit]
    def __init__(self, id: _Optional[str] = ..., ern: _Optional[str] = ..., contest_id: _Optional[str] = ..., member_id: _Optional[str] = ..., name: _Optional[str] = ..., out_of_competition: bool = ..., status: _Optional[_Union[Participant.Status, str]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_in: _Optional[int] = ..., end_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_in: _Optional[int] = ..., complete_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_in: _Optional[int] = ..., bonus_time: _Optional[int] = ..., passcode: _Optional[str] = ..., submits: _Optional[_Iterable[_Union[Participant.Submit, _Mapping]]] = ...) -> None: ...
