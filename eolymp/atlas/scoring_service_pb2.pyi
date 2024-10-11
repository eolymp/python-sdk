from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import scoring_score_pb2 as _scoring_score_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeProblemGradingInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeProblemGradingOutput(_message.Message):
    __slots__ = ["ranges"]
    class Range(_message.Message):
        __slots__ = ["grade", "upper_bound"]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
        grade: int
        upper_bound: float
        def __init__(self, grade: _Optional[int] = ..., upper_bound: _Optional[float] = ...) -> None: ...
    RANGES_FIELD_NUMBER: _ClassVar[int]
    ranges: _containers.RepeatedCompositeFieldContainer[DescribeProblemGradingOutput.Range]
    def __init__(self, ranges: _Optional[_Iterable[_Union[DescribeProblemGradingOutput.Range, _Mapping]]] = ...) -> None: ...

class DescribeScoreInput(_message.Message):
    __slots__ = ["member_id"]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    def __init__(self, member_id: _Optional[str] = ...) -> None: ...

class DescribeScoreOutput(_message.Message):
    __slots__ = ["score"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: _scoring_score_pb2.Score
    def __init__(self, score: _Optional[_Union[_scoring_score_pb2.Score, _Mapping]] = ...) -> None: ...

class ScoreChangedEvent(_message.Message):
    __slots__ = ["after", "before", "member_id", "problem_id"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    after: _scoring_score_pb2.Score
    before: _scoring_score_pb2.Score
    member_id: str
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., member_id: _Optional[str] = ..., before: _Optional[_Union[_scoring_score_pb2.Score, _Mapping]] = ..., after: _Optional[_Union[_scoring_score_pb2.Score, _Mapping]] = ...) -> None: ...
