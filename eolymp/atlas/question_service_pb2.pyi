from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import question_pb2 as _question_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuestionChangedEvent(_message.Message):
    __slots__ = ("problem_id", "before", "after")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    before: _question_pb2.Question
    after: _question_pb2.Question
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Union[_question_pb2.Question, _Mapping]] = ..., after: _Optional[_Union[_question_pb2.Question, _Mapping]] = ...) -> None: ...

class CreateQuestionInput(_message.Message):
    __slots__ = ("question",)
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    question: _question_pb2.Question
    def __init__(self, question: _Optional[_Union[_question_pb2.Question, _Mapping]] = ...) -> None: ...

class CreateQuestionOutput(_message.Message):
    __slots__ = ("question_id",)
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    question_id: str
    def __init__(self, question_id: _Optional[str] = ...) -> None: ...

class UpdateQuestionInput(_message.Message):
    __slots__ = ("patch", "question_id", "question")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_question_pb2.Question.Patch.Field]
    question_id: str
    question: _question_pb2.Question
    def __init__(self, patch: _Optional[_Iterable[_Union[_question_pb2.Question.Patch.Field, str]]] = ..., question_id: _Optional[str] = ..., question: _Optional[_Union[_question_pb2.Question, _Mapping]] = ...) -> None: ...

class UpdateQuestionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteQuestionInput(_message.Message):
    __slots__ = ("question_id",)
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    question_id: str
    def __init__(self, question_id: _Optional[str] = ...) -> None: ...

class DeleteQuestionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeQuestionInput(_message.Message):
    __slots__ = ("question_id", "version", "extra")
    QUESTION_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    question_id: str
    version: int
    extra: _containers.RepeatedScalarFieldContainer[_question_pb2.Question.Extra.Field]
    def __init__(self, question_id: _Optional[str] = ..., version: _Optional[int] = ..., extra: _Optional[_Iterable[_Union[_question_pb2.Question.Extra.Field, str]]] = ...) -> None: ...

class DescribeQuestionOutput(_message.Message):
    __slots__ = ("question",)
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    question: _question_pb2.Question
    def __init__(self, question: _Optional[_Union[_question_pb2.Question, _Mapping]] = ...) -> None: ...

class ListQuestionsInput(_message.Message):
    __slots__ = ("offset", "size", "version", "extra")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    version: int
    extra: _containers.RepeatedScalarFieldContainer[_question_pb2.Question.Extra.Field]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., version: _Optional[int] = ..., extra: _Optional[_Iterable[_Union[_question_pb2.Question.Extra.Field, str]]] = ...) -> None: ...

class ListQuestionsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_question_pb2.Question]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_question_pb2.Question, _Mapping]]] = ...) -> None: ...
