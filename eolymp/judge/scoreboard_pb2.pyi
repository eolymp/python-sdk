from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Scoreboard(_message.Message):
    __slots__ = ["attempt_penalty", "contest_id", "default", "freeze_in", "freeze_time", "id", "name", "status", "visible"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Row(_message.Message):
        __slots__ = ["breakdown", "name", "participant_id", "penalty", "rank", "rank_lower", "score", "scoreboard_id"]
        BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        RANK_FIELD_NUMBER: _ClassVar[int]
        RANK_LOWER_FIELD_NUMBER: _ClassVar[int]
        SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        breakdown: _containers.RepeatedCompositeFieldContainer[Scoreboard.Score]
        name: str
        participant_id: str
        penalty: float
        rank: int
        rank_lower: int
        score: float
        scoreboard_id: str
        def __init__(self, participant_id: _Optional[str] = ..., scoreboard_id: _Optional[str] = ..., name: _Optional[str] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., rank: _Optional[int] = ..., rank_lower: _Optional[int] = ..., breakdown: _Optional[_Iterable[_Union[Scoreboard.Score, _Mapping]]] = ...) -> None: ...
    class Score(_message.Message):
        __slots__ = ["attempts", "breakdown", "penalty", "percentage", "problem_id", "score", "solved", "solved_at", "solved_in"]
        ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SOLVED_AT_FIELD_NUMBER: _ClassVar[int]
        SOLVED_FIELD_NUMBER: _ClassVar[int]
        SOLVED_IN_FIELD_NUMBER: _ClassVar[int]
        attempts: int
        breakdown: _containers.RepeatedCompositeFieldContainer[Scoreboard.Testset]
        penalty: float
        percentage: float
        problem_id: str
        score: float
        solved: bool
        solved_at: _timestamp_pb2.Timestamp
        solved_in: int
        def __init__(self, problem_id: _Optional[str] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., solved: bool = ..., percentage: _Optional[float] = ..., attempts: _Optional[int] = ..., solved_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., solved_in: _Optional[int] = ..., breakdown: _Optional[_Iterable[_Union[Scoreboard.Testset, _Mapping]]] = ...) -> None: ...
    class Testset(_message.Message):
        __slots__ = ["cost", "index", "score", "testset_id"]
        COST_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
        cost: float
        index: int
        score: float
        testset_id: str
        def __init__(self, testset_id: _Optional[str] = ..., index: _Optional[int] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ...) -> None: ...
    ACTIVE: Scoreboard.Status
    ATTEMPT_PENALTY_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    FAILED: Scoreboard.Status
    FREEZE_IN_FIELD_NUMBER: _ClassVar[int]
    FREEZE_TIME_FIELD_NUMBER: _ClassVar[int]
    FROZEN: Scoreboard.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REBUILDING: Scoreboard.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: Scoreboard.Status
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    attempt_penalty: int
    contest_id: str
    default: bool
    freeze_in: int
    freeze_time: _timestamp_pb2.Timestamp
    id: str
    name: str
    status: Scoreboard.Status
    visible: bool
    def __init__(self, id: _Optional[str] = ..., contest_id: _Optional[str] = ..., name: _Optional[str] = ..., default: bool = ..., visible: bool = ..., attempt_penalty: _Optional[int] = ..., status: _Optional[_Union[Scoreboard.Status, str]] = ..., freeze_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., freeze_in: _Optional[int] = ...) -> None: ...
