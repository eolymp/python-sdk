from eolymp.judge import medal_pb2 as _medal_pb2
from eolymp.judge import score_pb2 as _score_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Result(_message.Message):
    __slots__ = ["contest_id", "disqualified", "ghost", "medal", "member_id", "name", "participant_id", "rank", "rank_lower", "score", "unofficial"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
    GHOST_FIELD_NUMBER: _ClassVar[int]
    MEDAL_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    RANK_LOWER_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    disqualified: bool
    ghost: bool
    medal: _medal_pb2.Medal
    member_id: str
    name: str
    participant_id: str
    rank: int
    rank_lower: int
    score: _score_pb2.Score
    unofficial: bool
    def __init__(self, participant_id: _Optional[str] = ..., member_id: _Optional[str] = ..., contest_id: _Optional[str] = ..., name: _Optional[str] = ..., unofficial: bool = ..., disqualified: bool = ..., ghost: bool = ..., medal: _Optional[_Union[_medal_pb2.Medal, str]] = ..., rank: _Optional[int] = ..., rank_lower: _Optional[int] = ..., score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class ResultV2(_message.Message):
    __slots__ = ["breakdown", "country", "cursor", "display_name", "disqualified", "ghost", "index", "medal", "member_id", "penalty", "picture", "rank", "rank_to", "score", "unofficial"]
    class ProblemScore(_message.Message):
        __slots__ = ["attempts", "penalty", "problem_id", "score", "solved", "solved_in"]
        ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SOLVED_FIELD_NUMBER: _ClassVar[int]
        SOLVED_IN_FIELD_NUMBER: _ClassVar[int]
        attempts: int
        penalty: float
        problem_id: str
        score: float
        solved: bool
        solved_in: int
        def __init__(self, problem_id: _Optional[str] = ..., solved: bool = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., attempts: _Optional[int] = ..., solved_in: _Optional[int] = ...) -> None: ...
    class RoundScore(_message.Message):
        __slots__ = ["breakdown", "penalty", "round_id", "score"]
        BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        ROUND_ID_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        breakdown: _containers.RepeatedCompositeFieldContainer[ResultV2.ProblemScore]
        penalty: float
        round_id: str
        score: float
        def __init__(self, round_id: _Optional[str] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., breakdown: _Optional[_Iterable[_Union[ResultV2.ProblemScore, _Mapping]]] = ...) -> None: ...
    BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
    GHOST_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    MEDAL_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PENALTY_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    RANK_TO_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    breakdown: _containers.RepeatedCompositeFieldContainer[ResultV2.RoundScore]
    country: str
    cursor: str
    display_name: str
    disqualified: bool
    ghost: bool
    index: int
    medal: _medal_pb2.Medal
    member_id: str
    penalty: float
    picture: str
    rank: int
    rank_to: int
    score: float
    unofficial: bool
    def __init__(self, member_id: _Optional[str] = ..., display_name: _Optional[str] = ..., picture: _Optional[str] = ..., country: _Optional[str] = ..., unofficial: bool = ..., disqualified: bool = ..., ghost: bool = ..., medal: _Optional[_Union[_medal_pb2.Medal, str]] = ..., index: _Optional[int] = ..., rank: _Optional[int] = ..., rank_to: _Optional[int] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., breakdown: _Optional[_Iterable[_Union[ResultV2.RoundScore, _Mapping]]] = ..., cursor: _Optional[str] = ...) -> None: ...
