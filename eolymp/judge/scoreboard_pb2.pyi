from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Scoreboard(_message.Message):
    __slots__ = ["columns", "modes"]
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Column(_message.Message):
        __slots__ = ["filterable", "id", "sortable", "title", "type"]
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        FILTERABLE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        PROBLEM_SCORE: Scoreboard.Column.Type
        ROUND_SCORE: Scoreboard.Column.Type
        SORTABLE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_TYPE: Scoreboard.Column.Type
        filterable: bool
        id: str
        sortable: bool
        title: str
        type: Scoreboard.Column.Type
        def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[Scoreboard.Column.Type, str]] = ..., title: _Optional[str] = ..., sortable: bool = ..., filterable: bool = ...) -> None: ...
    class Row(_message.Message):
        __slots__ = ["disqualified", "id", "index", "member_id", "penalty", "rank", "rank_length", "score", "tie_breaker", "unofficial", "values"]
        class ProblemScore(_message.Message):
            __slots__ = ["attempts", "penalty", "percentage", "score", "time"]
            ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
            PENALTY_FIELD_NUMBER: _ClassVar[int]
            PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            SCORE_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            attempts: int
            penalty: float
            percentage: float
            score: float
            time: int
            def __init__(self, score: _Optional[float] = ..., penalty: _Optional[float] = ..., attempts: _Optional[int] = ..., percentage: _Optional[float] = ..., time: _Optional[int] = ...) -> None: ...
        class RoundScore(_message.Message):
            __slots__ = ["disqualified", "penalty", "score", "tie_breaker", "unofficial"]
            DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
            PENALTY_FIELD_NUMBER: _ClassVar[int]
            SCORE_FIELD_NUMBER: _ClassVar[int]
            TIE_BREAKER_FIELD_NUMBER: _ClassVar[int]
            UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
            disqualified: bool
            penalty: float
            score: float
            tie_breaker: int
            unofficial: bool
            def __init__(self, score: _Optional[float] = ..., penalty: _Optional[float] = ..., tie_breaker: _Optional[int] = ..., unofficial: bool = ..., disqualified: bool = ...) -> None: ...
        class Value(_message.Message):
            __slots__ = ["column_id", "problem_score", "round_score"]
            COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
            PROBLEM_SCORE_FIELD_NUMBER: _ClassVar[int]
            ROUND_SCORE_FIELD_NUMBER: _ClassVar[int]
            column_id: str
            problem_score: Scoreboard.Row.ProblemScore
            round_score: Scoreboard.Row.RoundScore
            def __init__(self, column_id: _Optional[str] = ..., round_score: _Optional[_Union[Scoreboard.Row.RoundScore, _Mapping]] = ..., problem_score: _Optional[_Union[Scoreboard.Row.ProblemScore, _Mapping]] = ...) -> None: ...
        DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        RANK_FIELD_NUMBER: _ClassVar[int]
        RANK_LENGTH_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        TIE_BREAKER_FIELD_NUMBER: _ClassVar[int]
        UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        disqualified: bool
        id: str
        index: int
        member_id: str
        penalty: float
        rank: int
        rank_length: int
        score: float
        tie_breaker: int
        unofficial: bool
        values: _containers.RepeatedCompositeFieldContainer[Scoreboard.Row.Value]
        def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., index: _Optional[int] = ..., rank: _Optional[int] = ..., rank_length: _Optional[int] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., tie_breaker: _Optional[int] = ..., unofficial: bool = ..., disqualified: bool = ..., values: _Optional[_Iterable[_Union[Scoreboard.Row.Value, _Mapping]]] = ...) -> None: ...
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    FROZEN: Scoreboard.Mode
    MODES_FIELD_NUMBER: _ClassVar[int]
    RESULT: Scoreboard.Mode
    UPSOLVE: Scoreboard.Mode
    columns: _containers.RepeatedCompositeFieldContainer[Scoreboard.Column]
    modes: _containers.RepeatedScalarFieldContainer[Scoreboard.Mode]
    def __init__(self, modes: _Optional[_Iterable[_Union[Scoreboard.Mode, str]]] = ..., columns: _Optional[_Iterable[_Union[Scoreboard.Column, _Mapping]]] = ...) -> None: ...
