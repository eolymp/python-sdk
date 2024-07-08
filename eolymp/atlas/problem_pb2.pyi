from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Problem(_message.Message):
    __slots__ = ["acceptance_rate", "difficulty", "id", "links", "number", "origin", "private", "submissions_accepted", "submissions_count", "topics", "url", "visible", "vote", "vote_count"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class LinksEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACCEPTANCE_RATE_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    SUBMISSIONS_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    SUBMISSIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Problem.Extra
    URL_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    VOTE: Problem.Extra
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    acceptance_rate: float
    difficulty: int
    id: str
    links: _containers.ScalarMap[str, str]
    number: int
    origin: str
    private: bool
    submissions_accepted: int
    submissions_count: int
    topics: _containers.RepeatedScalarFieldContainer[str]
    url: str
    visible: bool
    vote: int
    vote_count: int
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., links: _Optional[_Mapping[str, str]] = ..., number: _Optional[int] = ..., visible: bool = ..., private: bool = ..., origin: _Optional[str] = ..., topics: _Optional[_Iterable[str]] = ..., acceptance_rate: _Optional[float] = ..., submissions_count: _Optional[int] = ..., submissions_accepted: _Optional[int] = ..., vote: _Optional[int] = ..., vote_count: _Optional[int] = ..., difficulty: _Optional[int] = ...) -> None: ...
