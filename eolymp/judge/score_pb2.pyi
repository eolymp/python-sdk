from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Score(_message.Message):
    __slots__ = ("valid_after", "valid_until", "timestamp", "score", "penalty", "tie_breaker", "upsolve", "breakdown")
    class FetchingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTUAL: _ClassVar[Score.FetchingMode]
        PUNCTUAL: _ClassVar[Score.FetchingMode]
        LATEST: _ClassVar[Score.FetchingMode]
        FROZEN: _ClassVar[Score.FetchingMode]
        UPSOLVE: _ClassVar[Score.FetchingMode]
    ACTUAL: Score.FetchingMode
    PUNCTUAL: Score.FetchingMode
    LATEST: Score.FetchingMode
    FROZEN: Score.FetchingMode
    UPSOLVE: Score.FetchingMode
    class Problem(_message.Message):
        __slots__ = ("problem_id", "score", "penalty", "solved", "percentage", "attempts", "solved_at", "solved_in", "changed", "breakdown")
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        SOLVED_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        SOLVED_AT_FIELD_NUMBER: _ClassVar[int]
        SOLVED_IN_FIELD_NUMBER: _ClassVar[int]
        CHANGED_FIELD_NUMBER: _ClassVar[int]
        BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
        problem_id: str
        score: float
        penalty: float
        solved: bool
        percentage: float
        attempts: int
        solved_at: _timestamp_pb2.Timestamp
        solved_in: int
        changed: bool
        breakdown: _containers.RepeatedCompositeFieldContainer[Score.Testset]
        def __init__(self, problem_id: _Optional[str] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., solved: bool = ..., percentage: _Optional[float] = ..., attempts: _Optional[int] = ..., solved_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., solved_in: _Optional[int] = ..., changed: bool = ..., breakdown: _Optional[_Iterable[_Union[Score.Testset, _Mapping]]] = ...) -> None: ...
    class Testset(_message.Message):
        __slots__ = ("testset_id", "index", "cost", "score")
        TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        COST_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        testset_id: str
        index: int
        cost: float
        score: float
        def __init__(self, testset_id: _Optional[str] = ..., index: _Optional[int] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ...) -> None: ...
    VALID_AFTER_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    PENALTY_FIELD_NUMBER: _ClassVar[int]
    TIE_BREAKER_FIELD_NUMBER: _ClassVar[int]
    UPSOLVE_FIELD_NUMBER: _ClassVar[int]
    BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    valid_after: int
    valid_until: int
    timestamp: _timestamp_pb2.Timestamp
    score: float
    penalty: float
    tie_breaker: int
    upsolve: bool
    breakdown: _containers.RepeatedCompositeFieldContainer[Score.Problem]
    def __init__(self, valid_after: _Optional[int] = ..., valid_until: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., tie_breaker: _Optional[int] = ..., upsolve: bool = ..., breakdown: _Optional[_Iterable[_Union[Score.Problem, _Mapping]]] = ...) -> None: ...
