from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Solution(_message.Message):
    __slots__ = ("id", "name", "secret", "runtime", "source", "type", "assertions", "status", "submission_id")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
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
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Solution.Status]
        PENDING: _ClassVar[Solution.Status]
        PASS: _ClassVar[Solution.Status]
        FAIL: _ClassVar[Solution.Status]
        ERROR: _ClassVar[Solution.Status]
    UNKNOWN_STATUS: Solution.Status
    PENDING: Solution.Status
    PASS: Solution.Status
    FAIL: Solution.Status
    ERROR: Solution.Status
    class Assertion(_message.Message):
        __slots__ = ("testset_id", "type")
        TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        testset_id: str
        type: Solution.Type
        def __init__(self, testset_id: _Optional[str] = ..., type: _Optional[_Union[Solution.Type, str]] = ...) -> None: ...
    class Patch(_message.Message):
        __slots__ = ("name", "secret", "runtime", "source", "type", "assertions", "clear_assertions")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SECRET_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ASSERTIONS_FIELD_NUMBER: _ClassVar[int]
        CLEAR_ASSERTIONS_FIELD_NUMBER: _ClassVar[int]
        name: str
        secret: bool
        runtime: str
        source: str
        type: Solution.Type
        assertions: _containers.RepeatedCompositeFieldContainer[Solution.Assertion]
        clear_assertions: bool
        def __init__(self, name: _Optional[str] = ..., secret: _Optional[bool] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., type: _Optional[_Union[Solution.Type, str]] = ..., assertions: _Optional[_Iterable[_Union[Solution.Assertion, _Mapping]]] = ..., clear_assertions: _Optional[bool] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSERTIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    secret: bool
    runtime: str
    source: str
    type: Solution.Type
    assertions: _containers.RepeatedCompositeFieldContainer[Solution.Assertion]
    status: Solution.Status
    submission_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., secret: _Optional[bool] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., type: _Optional[_Union[Solution.Type, str]] = ..., assertions: _Optional[_Iterable[_Union[Solution.Assertion, _Mapping]]] = ..., status: _Optional[_Union[Solution.Status, str]] = ..., submission_id: _Optional[str] = ...) -> None: ...
