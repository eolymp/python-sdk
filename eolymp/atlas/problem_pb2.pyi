from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.atlas import form_pb2 as _form_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Problem(_message.Message):
    __slots__ = ("id", "url", "type", "number", "visible", "origin", "language", "title", "content", "download_link", "author", "source", "languages", "topics", "score", "constraints", "acceptance_rate", "submissions_count", "submissions_accepted", "vote", "vote_count", "difficulty", "submission_form", "examples")
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
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_EXTRA: _ClassVar[Problem.Extra.Field]
            CONTENT_VALUE: _ClassVar[Problem.Extra.Field]
            CONTENT_RENDER: _ClassVar[Problem.Extra.Field]
        UNKNOWN_EXTRA: Problem.Extra.Field
        CONTENT_VALUE: Problem.Extra.Field
        CONTENT_RENDER: Problem.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_PATCH: _ClassVar[Problem.Patch.Field]
            VISIBLE: _ClassVar[Problem.Patch.Field]
            PRIVATE: _ClassVar[Problem.Patch.Field]
            TOPICS: _ClassVar[Problem.Patch.Field]
            DIFFICULTY: _ClassVar[Problem.Patch.Field]
            ORIGIN: _ClassVar[Problem.Patch.Field]
            TYPE: _ClassVar[Problem.Patch.Field]
            NUMBER: _ClassVar[Problem.Patch.Field]
        UNKNOWN_PATCH: Problem.Patch.Field
        VISIBLE: Problem.Patch.Field
        PRIVATE: Problem.Patch.Field
        TOPICS: Problem.Patch.Field
        DIFFICULTY: Problem.Patch.Field
        ORIGIN: Problem.Patch.Field
        TYPE: Problem.Patch.Field
        NUMBER: Problem.Patch.Field
        def __init__(self) -> None: ...
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
    class Example(_message.Message):
        __slots__ = ("index", "input_url", "answer_url")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        index: int
        input_url: str
        answer_url: str
        def __init__(self, index: _Optional[int] = ..., input_url: _Optional[str] = ..., answer_url: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    ACCEPTANCE_RATE_FIELD_NUMBER: _ClassVar[int]
    SUBMISSIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUBMISSIONS_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    VOTE_FIELD_NUMBER: _ClassVar[int]
    VOTE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_FORM_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    type: Problem.Type
    number: int
    visible: bool
    origin: str
    language: str
    title: str
    content: _content_pb2.Content
    download_link: str
    author: str
    source: str
    languages: _containers.RepeatedScalarFieldContainer[str]
    topics: _containers.RepeatedScalarFieldContainer[str]
    score: float
    constraints: Problem.Constraints
    acceptance_rate: float
    submissions_count: int
    submissions_accepted: int
    vote: int
    vote_count: int
    difficulty: int
    submission_form: _form_pb2.Form
    examples: _containers.RepeatedCompositeFieldContainer[Problem.Example]
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., type: _Optional[_Union[Problem.Type, str]] = ..., number: _Optional[int] = ..., visible: bool = ..., origin: _Optional[str] = ..., language: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., download_link: _Optional[str] = ..., author: _Optional[str] = ..., source: _Optional[str] = ..., languages: _Optional[_Iterable[str]] = ..., topics: _Optional[_Iterable[str]] = ..., score: _Optional[float] = ..., constraints: _Optional[_Union[Problem.Constraints, _Mapping]] = ..., acceptance_rate: _Optional[float] = ..., submissions_count: _Optional[int] = ..., submissions_accepted: _Optional[int] = ..., vote: _Optional[int] = ..., vote_count: _Optional[int] = ..., difficulty: _Optional[int] = ..., submission_form: _Optional[_Union[_form_pb2.Form, _Mapping]] = ..., examples: _Optional[_Iterable[_Union[Problem.Example, _Mapping]]] = ...) -> None: ...
