from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Score(_message.Message):
    __slots__ = ["breakdown", "penalty", "score", "tie_breaker", "timestamp", "upsolve", "valid_after", "valid_until"]
    class FetchingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Problem(_message.Message):
        __slots__ = ["attempts", "breakdown", "changed", "penalty", "percentage", "problem_id", "score", "solved", "solved_at", "solved_in"]
        ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
        CHANGED_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SOLVED_AT_FIELD_NUMBER: _ClassVar[int]
        SOLVED_FIELD_NUMBER: _ClassVar[int]
        SOLVED_IN_FIELD_NUMBER: _ClassVar[int]
        attempts: int
        breakdown: _containers.RepeatedCompositeFieldContainer[Score.Testset]
        changed: bool
        penalty: float
        percentage: float
        problem_id: str
        score: float
        solved: bool
        solved_at: _timestamp_pb2.Timestamp
        solved_in: int
        def __init__(self, problem_id: _Optional[str] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., solved: bool = ..., percentage: _Optional[float] = ..., attempts: _Optional[int] = ..., solved_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., solved_in: _Optional[int] = ..., changed: bool = ..., breakdown: _Optional[_Iterable[_Union[Score.Testset, _Mapping]]] = ...) -> None: ...
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
    ACTUAL: Score.FetchingMode
    BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    FROZEN: Score.FetchingMode
    LATEST: Score.FetchingMode
    PENALTY_FIELD_NUMBER: _ClassVar[int]
    PUNCTUAL: Score.FetchingMode
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TIE_BREAKER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPSOLVE: Score.FetchingMode
    UPSOLVE_FIELD_NUMBER: _ClassVar[int]
    VALID_AFTER_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    breakdown: _containers.RepeatedCompositeFieldContainer[Score.Problem]
    penalty: float
    score: float
    tie_breaker: int
    timestamp: _timestamp_pb2.Timestamp
    upsolve: bool
    valid_after: int
    valid_until: int
    def __init__(self, valid_after: _Optional[int] = ..., valid_until: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., tie_breaker: _Optional[int] = ..., upsolve: bool = ..., breakdown: _Optional[_Iterable[_Union[Score.Problem, _Mapping]]] = ...) -> None: ...
