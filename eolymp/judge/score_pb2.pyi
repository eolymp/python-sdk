from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Score(_message.Message):
    __slots__ = ["breakdown", "offset", "penalty", "score"]
    class FetchingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Problem(_message.Message):
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
        breakdown: _containers.RepeatedCompositeFieldContainer[Score.Testset]
        penalty: float
        percentage: float
        problem_id: str
        score: float
        solved: bool
        solved_at: _timestamp_pb2.Timestamp
        solved_in: int
        def __init__(self, problem_id: _Optional[str] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., solved: bool = ..., percentage: _Optional[float] = ..., attempts: _Optional[int] = ..., solved_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., solved_in: _Optional[int] = ..., breakdown: _Optional[_Iterable[_Union[Score.Testset, _Mapping]]] = ...) -> None: ...
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
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PENALTY_FIELD_NUMBER: _ClassVar[int]
    PUNCTUAL: Score.FetchingMode
    SCORE_FIELD_NUMBER: _ClassVar[int]
    breakdown: _containers.RepeatedCompositeFieldContainer[Score.Problem]
    offset: int
    penalty: float
    score: float
    def __init__(self, offset: _Optional[int] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., breakdown: _Optional[_Iterable[_Union[Score.Problem, _Mapping]]] = ...) -> None: ...
