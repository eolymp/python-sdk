from eolymp.judge import medal_pb2 as _medal_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Scoreboard(_message.Message):
    __slots__ = ("modes", "rounds", "columns")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESULT: _ClassVar[Scoreboard.Mode]
        FROZEN: _ClassVar[Scoreboard.Mode]
        UPSOLVE: _ClassVar[Scoreboard.Mode]
    RESULT: Scoreboard.Mode
    FROZEN: Scoreboard.Mode
    UPSOLVE: Scoreboard.Mode
    class Round(_message.Message):
        __slots__ = ("id", "title")
        ID_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        id: str
        title: str
        def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...
    class Column(_message.Message):
        __slots__ = ("id", "type", "title", "choices", "sortable", "filterable")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_TYPE: _ClassVar[Scoreboard.Column.Type]
            ROUND_SCORE: _ClassVar[Scoreboard.Column.Type]
            PROBLEM_SCORE: _ClassVar[Scoreboard.Column.Type]
            STRING: _ClassVar[Scoreboard.Column.Type]
            NUMBER: _ClassVar[Scoreboard.Column.Type]
            CHOICE: _ClassVar[Scoreboard.Column.Type]
            DATE: _ClassVar[Scoreboard.Column.Type]
            EMAIL: _ClassVar[Scoreboard.Column.Type]
            CHECKBOX: _ClassVar[Scoreboard.Column.Type]
            COUNTRY: _ClassVar[Scoreboard.Column.Type]
            REGION: _ClassVar[Scoreboard.Column.Type]
            INSTITUTION: _ClassVar[Scoreboard.Column.Type]
        UNKNOWN_TYPE: Scoreboard.Column.Type
        ROUND_SCORE: Scoreboard.Column.Type
        PROBLEM_SCORE: Scoreboard.Column.Type
        STRING: Scoreboard.Column.Type
        NUMBER: Scoreboard.Column.Type
        CHOICE: Scoreboard.Column.Type
        DATE: Scoreboard.Column.Type
        EMAIL: Scoreboard.Column.Type
        CHECKBOX: Scoreboard.Column.Type
        COUNTRY: Scoreboard.Column.Type
        REGION: Scoreboard.Column.Type
        INSTITUTION: Scoreboard.Column.Type
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        CHOICES_FIELD_NUMBER: _ClassVar[int]
        SORTABLE_FIELD_NUMBER: _ClassVar[int]
        FILTERABLE_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: Scoreboard.Column.Type
        title: str
        choices: _containers.RepeatedScalarFieldContainer[str]
        sortable: bool
        filterable: bool
        def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[Scoreboard.Column.Type, str]] = ..., title: _Optional[str] = ..., choices: _Optional[_Iterable[str]] = ..., sortable: bool = ..., filterable: bool = ...) -> None: ...
    class Row(_message.Message):
        __slots__ = ("id", "member_id", "index", "rank", "rank_length", "score", "penalty", "tie_breaker", "unofficial", "disqualified", "medal", "values")
        class Value(_message.Message):
            __slots__ = ("column_id", "round_score", "problem_score", "string", "number")
            COLUMN_ID_FIELD_NUMBER: _ClassVar[int]
            ROUND_SCORE_FIELD_NUMBER: _ClassVar[int]
            PROBLEM_SCORE_FIELD_NUMBER: _ClassVar[int]
            STRING_FIELD_NUMBER: _ClassVar[int]
            NUMBER_FIELD_NUMBER: _ClassVar[int]
            column_id: str
            round_score: Scoreboard.Row.RoundScore
            problem_score: Scoreboard.Row.ProblemScore
            string: str
            number: str
            def __init__(self, column_id: _Optional[str] = ..., round_score: _Optional[_Union[Scoreboard.Row.RoundScore, _Mapping]] = ..., problem_score: _Optional[_Union[Scoreboard.Row.ProblemScore, _Mapping]] = ..., string: _Optional[str] = ..., number: _Optional[str] = ...) -> None: ...
        class RoundScore(_message.Message):
            __slots__ = ("score", "penalty", "tie_breaker", "unofficial", "disqualified", "medal")
            SCORE_FIELD_NUMBER: _ClassVar[int]
            PENALTY_FIELD_NUMBER: _ClassVar[int]
            TIE_BREAKER_FIELD_NUMBER: _ClassVar[int]
            UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
            DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
            MEDAL_FIELD_NUMBER: _ClassVar[int]
            score: float
            penalty: float
            tie_breaker: int
            unofficial: bool
            disqualified: bool
            medal: _medal_pb2.Medal
            def __init__(self, score: _Optional[float] = ..., penalty: _Optional[float] = ..., tie_breaker: _Optional[int] = ..., unofficial: bool = ..., disqualified: bool = ..., medal: _Optional[_Union[_medal_pb2.Medal, str]] = ...) -> None: ...
        class ProblemScore(_message.Message):
            __slots__ = ("score", "penalty", "attempts", "percentage", "time")
            SCORE_FIELD_NUMBER: _ClassVar[int]
            PENALTY_FIELD_NUMBER: _ClassVar[int]
            ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
            PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            score: float
            penalty: float
            attempts: int
            percentage: float
            time: int
            def __init__(self, score: _Optional[float] = ..., penalty: _Optional[float] = ..., attempts: _Optional[int] = ..., percentage: _Optional[float] = ..., time: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        RANK_FIELD_NUMBER: _ClassVar[int]
        RANK_LENGTH_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        TIE_BREAKER_FIELD_NUMBER: _ClassVar[int]
        UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
        DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
        MEDAL_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        id: str
        member_id: str
        index: int
        rank: int
        rank_length: int
        score: float
        penalty: float
        tie_breaker: int
        unofficial: bool
        disqualified: bool
        medal: _medal_pb2.Medal
        values: _containers.RepeatedCompositeFieldContainer[Scoreboard.Row.Value]
        def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., index: _Optional[int] = ..., rank: _Optional[int] = ..., rank_length: _Optional[int] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ..., tie_breaker: _Optional[int] = ..., unofficial: bool = ..., disqualified: bool = ..., medal: _Optional[_Union[_medal_pb2.Medal, str]] = ..., values: _Optional[_Iterable[_Union[Scoreboard.Row.Value, _Mapping]]] = ...) -> None: ...
    MODES_FIELD_NUMBER: _ClassVar[int]
    ROUNDS_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    modes: _containers.RepeatedScalarFieldContainer[Scoreboard.Mode]
    rounds: _containers.RepeatedCompositeFieldContainer[Scoreboard.Round]
    columns: _containers.RepeatedCompositeFieldContainer[Scoreboard.Column]
    def __init__(self, modes: _Optional[_Iterable[_Union[Scoreboard.Mode, str]]] = ..., rounds: _Optional[_Iterable[_Union[Scoreboard.Round, _Mapping]]] = ..., columns: _Optional[_Iterable[_Union[Scoreboard.Column, _Mapping]]] = ...) -> None: ...
