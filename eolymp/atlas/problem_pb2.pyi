from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Problem(_message.Message):
    __slots__ = ("id", "url", "type", "links", "number", "visible", "origin", "title", "content", "topics", "score", "constraints", "acceptance_rate", "submissions_count", "submissions_accepted", "vote", "vote_count", "difficulty")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[Problem.Extra]
        VOTE: _ClassVar[Problem.Extra]
        TITLE: _ClassVar[Problem.Extra]
        CONTENT_VALUE: _ClassVar[Problem.Extra]
        CONTENT_RENDER: _ClassVar[Problem.Extra]
    UNKNOWN_EXTRA: Problem.Extra
    VOTE: Problem.Extra
    TITLE: Problem.Extra
    CONTENT_VALUE: Problem.Extra
    CONTENT_RENDER: Problem.Extra
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TYPE: _ClassVar[Problem.Type]
        PROGRAM: _ClassVar[Problem.Type]
        FUNCTION: _ClassVar[Problem.Type]
        OUTPUT: _ClassVar[Problem.Type]
        SQL: _ClassVar[Problem.Type]
        ML: _ClassVar[Problem.Type]
    UNKNOWN_TYPE: Problem.Type
    PROGRAM: Problem.Type
    FUNCTION: Problem.Type
    OUTPUT: Problem.Type
    SQL: Problem.Type
    ML: Problem.Type
    class Constraints(_message.Message):
        __slots__ = ("time_limit_min", "time_limit_max", "cpu_limit_min", "cpu_limit_max", "memory_limit_min", "memory_limit_max")
        TIME_LIMIT_MIN_FIELD_NUMBER: _ClassVar[int]
        TIME_LIMIT_MAX_FIELD_NUMBER: _ClassVar[int]
        CPU_LIMIT_MIN_FIELD_NUMBER: _ClassVar[int]
        CPU_LIMIT_MAX_FIELD_NUMBER: _ClassVar[int]
        MEMORY_LIMIT_MIN_FIELD_NUMBER: _ClassVar[int]
        MEMORY_LIMIT_MAX_FIELD_NUMBER: _ClassVar[int]
        time_limit_min: int
        time_limit_max: int
        cpu_limit_min: int
        cpu_limit_max: int
        memory_limit_min: int
        memory_limit_max: int
        def __init__(self, time_limit_min: _Optional[int] = ..., time_limit_max: _Optional[int] = ..., cpu_limit_min: _Optional[int] = ..., cpu_limit_max: _Optional[int] = ..., memory_limit_min: _Optional[int] = ..., memory_limit_max: _Optional[int] = ...) -> None: ...
    class LinksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    ACCEPTANCE_RATE_FIELD_NUMBER: _ClassVar[int]
    SUBMISSIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUBMISSIONS_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    type: Problem.Type
    links: _containers.ScalarMap[str, str]
    number: int
    visible: bool
    origin: str
    title: str
    content: _content_pb2.Content
    topics: _containers.RepeatedScalarFieldContainer[str]
    score: float
    constraints: Problem.Constraints
    acceptance_rate: float
    submissions_count: int
    submissions_accepted: int
    vote: int
    vote_count: int
    difficulty: int
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., type: _Optional[_Union[Problem.Type, str]] = ..., links: _Optional[_Mapping[str, str]] = ..., number: _Optional[int] = ..., visible: bool = ..., origin: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., topics: _Optional[_Iterable[str]] = ..., score: _Optional[float] = ..., constraints: _Optional[_Union[Problem.Constraints, _Mapping]] = ..., acceptance_rate: _Optional[float] = ..., submissions_count: _Optional[int] = ..., submissions_accepted: _Optional[int] = ..., vote: _Optional[int] = ..., vote_count: _Optional[int] = ..., difficulty: _Optional[int] = ...) -> None: ...
