from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Solution(_message.Message):
    __slots__ = ["id", "name", "secret", "runtime", "source", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNSET: _ClassVar[Solution.Type]
        CORRECT: _ClassVar[Solution.Type]
        INCORRECT: _ClassVar[Solution.Type]
        WRONG_ANSWER: _ClassVar[Solution.Type]
        TIMEOUT: _ClassVar[Solution.Type]
        OVERFLOW: _ClassVar[Solution.Type]
        TIMEOUT_OR_ACCEPTED: _ClassVar[Solution.Type]
        OVERFLOW_OR_ACCEPTED: _ClassVar[Solution.Type]
        DONT_RUN: _ClassVar[Solution.Type]
        FAILURE: _ClassVar[Solution.Type]
    UNSET: Solution.Type
    CORRECT: Solution.Type
    INCORRECT: Solution.Type
    WRONG_ANSWER: Solution.Type
    TIMEOUT: Solution.Type
    OVERFLOW: Solution.Type
    TIMEOUT_OR_ACCEPTED: Solution.Type
    OVERFLOW_OR_ACCEPTED: Solution.Type
    DONT_RUN: Solution.Type
    FAILURE: Solution.Type
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    secret: bool
    runtime: str
    source: str
    type: Solution.Type
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., secret: bool = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., type: _Optional[_Union[Solution.Type, str]] = ...) -> None: ...
