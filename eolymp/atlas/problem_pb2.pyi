from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Problem(_message.Message):
    __slots__ = ["acceptance_rate", "constraints", "difficulty", "id", "links", "number", "origin", "score", "submissions_accepted", "submissions_count", "topics", "type", "url", "visible", "vote", "vote_count"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Constraints(_message.Message):
        __slots__ = ["cpu_limit_max", "cpu_limit_min", "memory_limit_max", "memory_limit_min", "time_limit_max", "time_limit_min"]
        CPU_LIMIT_MAX_FIELD_NUMBER: _ClassVar[int]
        CPU_LIMIT_MIN_FIELD_NUMBER: _ClassVar[int]
        MEMORY_LIMIT_MAX_FIELD_NUMBER: _ClassVar[int]
        MEMORY_LIMIT_MIN_FIELD_NUMBER: _ClassVar[int]
        TIME_LIMIT_MAX_FIELD_NUMBER: _ClassVar[int]
        TIME_LIMIT_MIN_FIELD_NUMBER: _ClassVar[int]
        cpu_limit_max: int
        cpu_limit_min: int
        memory_limit_max: int
        memory_limit_min: int
        time_limit_max: int
        time_limit_min: int
        def __init__(self, time_limit_min: _Optional[int] = ..., time_limit_max: _Optional[int] = ..., cpu_limit_min: _Optional[int] = ..., cpu_limit_max: _Optional[int] = ..., memory_limit_min: _Optional[int] = ..., memory_limit_max: _Optional[int] = ...) -> None: ...
    class LinksEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACCEPTANCE_RATE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    OUTPUT: Problem.Type
    PROGRAMMING: Problem.Type
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SQL: Problem.Type
    SUBMISSIONS_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    SUBMISSIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Problem.Extra
    UNKNOWN_TYPE: Problem.Type
    URL_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    VOTE: Problem.Extra
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    acceptance_rate: float
    constraints: Problem.Constraints
    difficulty: int
    id: str
    links: _containers.ScalarMap[str, str]
    number: int
    origin: str
    score: float
    submissions_accepted: int
    submissions_count: int
    topics: _containers.RepeatedScalarFieldContainer[str]
    type: Problem.Type
    url: str
    visible: bool
    vote: int
    vote_count: int
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., type: _Optional[_Union[Problem.Type, str]] = ..., links: _Optional[_Mapping[str, str]] = ..., number: _Optional[int] = ..., visible: bool = ..., origin: _Optional[str] = ..., topics: _Optional[_Iterable[str]] = ..., score: _Optional[float] = ..., constraints: _Optional[_Union[Problem.Constraints, _Mapping]] = ..., acceptance_rate: _Optional[float] = ..., submissions_count: _Optional[int] = ..., submissions_accepted: _Optional[int] = ..., vote: _Optional[int] = ..., vote_count: _Optional[int] = ..., difficulty: _Optional[int] = ...) -> None: ...
