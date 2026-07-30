from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Validation(_message.Message):
    __slots__ = ("id", "problem_id", "version", "status", "verdict", "error", "error_url", "total", "checked", "valid", "invalid", "groups")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Validation.Status]
        PENDING: _ClassVar[Validation.Status]
        TESTING: _ClassVar[Validation.Status]
        COMPLETE: _ClassVar[Validation.Status]
        ERROR: _ClassVar[Validation.Status]
        FAILURE: _ClassVar[Validation.Status]
        SKIPPED: _ClassVar[Validation.Status]
        PROVISIONING: _ClassVar[Validation.Status]
        INITIALIZING: _ClassVar[Validation.Status]
        CANCELLED: _ClassVar[Validation.Status]
    NONE: Validation.Status
    PENDING: Validation.Status
    TESTING: Validation.Status
    COMPLETE: Validation.Status
    ERROR: Validation.Status
    FAILURE: Validation.Status
    SKIPPED: Validation.Status
    PROVISIONING: Validation.Status
    INITIALIZING: Validation.Status
    CANCELLED: Validation.Status
    class Verdict(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_VERDICT: _ClassVar[Validation.Verdict]
        VALID: _ClassVar[Validation.Verdict]
        INVALID: _ClassVar[Validation.Verdict]
        BROKEN: _ClassVar[Validation.Verdict]
    NO_VERDICT: Validation.Verdict
    VALID: Validation.Verdict
    INVALID: Validation.Verdict
    BROKEN: Validation.Verdict
    class Run(_message.Message):
        __slots__ = ("id", "index", "status", "verdict", "input_url", "output_url")
        ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_URL_FIELD_NUMBER: _ClassVar[int]
        id: str
        index: int
        status: Validation.Status
        verdict: Validation.Verdict
        input_url: str
        output_url: str
        def __init__(self, id: _Optional[str] = ..., index: _Optional[int] = ..., status: _Optional[_Union[Validation.Status, str]] = ..., verdict: _Optional[_Union[Validation.Verdict, str]] = ..., input_url: _Optional[str] = ..., output_url: _Optional[str] = ...) -> None: ...
    class Group(_message.Message):
        __slots__ = ("index", "testset_id", "runs")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
        RUNS_FIELD_NUMBER: _ClassVar[int]
        index: int
        testset_id: str
        runs: _containers.RepeatedCompositeFieldContainer[Validation.Run]
        def __init__(self, index: _Optional[int] = ..., testset_id: _Optional[str] = ..., runs: _Optional[_Iterable[_Union[Validation.Run, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_URL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    CHECKED_FIELD_NUMBER: _ClassVar[int]
    VALID_FIELD_NUMBER: _ClassVar[int]
    INVALID_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    id: str
    problem_id: str
    version: int
    status: Validation.Status
    verdict: Validation.Verdict
    error: str
    error_url: str
    total: int
    checked: int
    valid: int
    invalid: int
    groups: _containers.RepeatedCompositeFieldContainer[Validation.Group]
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., version: _Optional[int] = ..., status: _Optional[_Union[Validation.Status, str]] = ..., verdict: _Optional[_Union[Validation.Verdict, str]] = ..., error: _Optional[str] = ..., error_url: _Optional[str] = ..., total: _Optional[int] = ..., checked: _Optional[int] = ..., valid: _Optional[int] = ..., invalid: _Optional[int] = ..., groups: _Optional[_Iterable[_Union[Validation.Group, _Mapping]]] = ...) -> None: ...
