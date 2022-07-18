from eolymp.executor import usage_pb2 as _usage_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Run(_message.Message):
    __slots__ = ["cpu_time_usage", "error", "exit_code", "id", "input", "input_ern", "lang", "memory_usage", "output", "output_ern", "problem_ern", "resource_usage", "runtime", "signal", "source", "source_ern", "status", "wall_time_usage"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CPU_EXHAUSTED: Run.Status
    CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR: Run.Status
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXECUTED: Run.Status
    EXECUTING: Run.Status
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    FAILURE: Run.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_ERN_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    MEMORY_OVERFLOW: Run.Status
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    NONE: Run.Status
    OUTPUT_ERN_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    PENDING: Run.Status
    PROBLEM_ERN_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ERN_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT: Run.Status
    WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
    cpu_time_usage: int
    error: str
    exit_code: int
    id: str
    input: str
    input_ern: str
    lang: str
    memory_usage: int
    output: str
    output_ern: str
    problem_ern: str
    resource_usage: _usage_pb2.ResourceUsage
    runtime: str
    signal: int
    source: str
    source_ern: str
    status: Run.Status
    wall_time_usage: int
    def __init__(self, id: _Optional[str] = ..., lang: _Optional[str] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., source_ern: _Optional[str] = ..., input: _Optional[str] = ..., input_ern: _Optional[str] = ..., status: _Optional[_Union[Run.Status, str]] = ..., error: _Optional[str] = ..., exit_code: _Optional[int] = ..., signal: _Optional[int] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[_Union[_usage_pb2.ResourceUsage, _Mapping]] = ..., output: _Optional[str] = ..., output_ern: _Optional[str] = ..., problem_ern: _Optional[str] = ...) -> None: ...
