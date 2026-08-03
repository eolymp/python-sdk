from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Question(_message.Message):
    __slots__ = ("id", "index", "type", "content", "score", "multiple", "options", "answers")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TYPE: _ClassVar[Question.Type]
        CHOICE: _ClassVar[Question.Type]
        TEXT: _ClassVar[Question.Type]
    UNKNOWN_TYPE: Question.Type
    CHOICE: Question.Type
    TEXT: Question.Type
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[Question.Extra.Field]
            CONTENT_RENDER: _ClassVar[Question.Extra.Field]
            CONTENT_VALUE: _ClassVar[Question.Extra.Field]
        UNKNOWN_FIELD: Question.Extra.Field
        CONTENT_RENDER: Question.Extra.Field
        CONTENT_VALUE: Question.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[Question.Patch.Field]
            INDEX: _ClassVar[Question.Patch.Field]
            TYPE: _ClassVar[Question.Patch.Field]
            CONTENT: _ClassVar[Question.Patch.Field]
            SCORE: _ClassVar[Question.Patch.Field]
            MULTIPLE: _ClassVar[Question.Patch.Field]
            OPTIONS: _ClassVar[Question.Patch.Field]
            ANSWERS: _ClassVar[Question.Patch.Field]
        UNKNOWN_FIELD: Question.Patch.Field
        INDEX: Question.Patch.Field
        TYPE: Question.Patch.Field
        CONTENT: Question.Patch.Field
        SCORE: Question.Patch.Field
        MULTIPLE: Question.Patch.Field
        OPTIONS: Question.Patch.Field
        ANSWERS: Question.Patch.Field
        def __init__(self) -> None: ...
    class Option(_message.Message):
        __slots__ = ("id", "index", "content", "correct")
        ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        CORRECT_FIELD_NUMBER: _ClassVar[int]
        id: str
        index: int
        content: _content_pb2.Content
        correct: bool
        def __init__(self, id: _Optional[str] = ..., index: _Optional[int] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., correct: _Optional[bool] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    MULTIPLE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ANSWERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    index: int
    type: Question.Type
    content: _content_pb2.Content
    score: float
    multiple: bool
    options: _containers.RepeatedCompositeFieldContainer[Question.Option]
    answers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., index: _Optional[int] = ..., type: _Optional[_Union[Question.Type, str]] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., score: _Optional[float] = ..., multiple: _Optional[bool] = ..., options: _Optional[_Iterable[_Union[Question.Option, _Mapping]]] = ..., answers: _Optional[_Iterable[str]] = ...) -> None: ...
