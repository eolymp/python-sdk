from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Solution(_message.Message):
    __slots__ = ["id", "name", "runtime", "secret", "source", "source_url", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CORRECT: Solution.Type
    DONT_RUN: Solution.Type
    FAILURE: Solution.Type
    ID_FIELD_NUMBER: _ClassVar[int]
    INCORRECT: Solution.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    OVERFLOW: Solution.Type
    OVERFLOW_OR_ACCEPTED: Solution.Type
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT: Solution.Type
    TIMEOUT_OR_ACCEPTED: Solution.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNSET: Solution.Type
    WRONG_ANSWER: Solution.Type
    id: str
    name: str
    runtime: str
    secret: bool
    source: str
    source_url: str
    type: Solution.Type
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., secret: bool = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., source_url: _Optional[str] = ..., type: _Optional[_Union[Solution.Type, str]] = ...) -> None: ...
