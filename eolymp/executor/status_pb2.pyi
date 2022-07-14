from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Status(_message.Message):
    __slots__ = ["agent", "error", "failure", "origin", "reference", "runs", "signature", "type", "version"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Run(_message.Message):
        __slots__ = ["cost", "cpu_time_limit", "cpu_time_usage", "exit_code", "interactor_log", "memory_limit", "memory_usage", "output", "reference", "score", "signal", "status", "stderr", "verifier_log", "wall_time_limit", "wall_time_usage"]
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ACCEPTED: Status.Run.Status
        COST_FIELD_NUMBER: _ClassVar[int]
        CPU_EXHAUSTED: Status.Run.Status
        CPU_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
        CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        EXECUTED: Status.Run.Status
        EXECUTING: Status.Run.Status
        EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
        INTERACTOR_LOG_FIELD_NUMBER: _ClassVar[int]
        MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
        MEMORY_OVERFLOW: Status.Run.Status
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        NONE: Status.Run.Status
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        PENDING: Status.Run.Status
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_ERROR: Status.Run.Status
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SIGNAL_FIELD_NUMBER: _ClassVar[int]
        SKIPPED: Status.Run.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        STDERR_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT: Status.Run.Status
        VERIFICATION_FAILURE: Status.Run.Status
        VERIFIER_LOG_FIELD_NUMBER: _ClassVar[int]
        WALL_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
        WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        WRONG_ANSWER: Status.Run.Status
        cost: float
        cpu_time_limit: int
        cpu_time_usage: int
        exit_code: int
        interactor_log: str
        memory_limit: int
        memory_usage: int
        output: str
        reference: str
        score: float
        signal: int
        status: Status.Run.Status
        stderr: str
        verifier_log: str
        wall_time_limit: int
        wall_time_usage: int
        def __init__(self, reference: _Optional[str] = ..., status: _Optional[_Union[Status.Run.Status, str]] = ..., score: _Optional[float] = ..., cost: _Optional[float] = ..., wall_time_usage: _Optional[int] = ..., wall_time_limit: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., cpu_time_limit: _Optional[int] = ..., memory_usage: _Optional[int] = ..., memory_limit: _Optional[int] = ..., exit_code: _Optional[int] = ..., signal: _Optional[int] = ..., output: _Optional[str] = ..., stderr: _Optional[str] = ..., verifier_log: _Optional[str] = ..., interactor_log: _Optional[str] = ...) -> None: ...
    AGENT_FIELD_NUMBER: _ClassVar[int]
    ERROR: Status.Type
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FAILURE: Status.Type
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    NONE: Status.Type
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE: Status.Type
    VERSION_FIELD_NUMBER: _ClassVar[int]
    agent: str
    error: str
    failure: str
    origin: str
    reference: str
    runs: _containers.RepeatedCompositeFieldContainer[Status.Run]
    signature: str
    type: Status.Type
    version: int
    def __init__(self, reference: _Optional[str] = ..., origin: _Optional[str] = ..., type: _Optional[_Union[Status.Type, str]] = ..., error: _Optional[str] = ..., failure: _Optional[str] = ..., runs: _Optional[_Iterable[_Union[Status.Run, _Mapping]]] = ..., signature: _Optional[str] = ..., version: _Optional[int] = ..., agent: _Optional[str] = ...) -> None: ...
