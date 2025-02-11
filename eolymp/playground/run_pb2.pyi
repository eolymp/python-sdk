from eolymp.executor import usage_pb2 as _usage_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Run(_message.Message):
    __slots__ = ("id", "runtime", "source_url", "input_url", "status", "error", "exit_code", "signal", "wall_time_usage", "cpu_time_usage", "memory_usage", "resource_usage", "output_url")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Run.Status]
        PENDING: _ClassVar[Run.Status]
        PROVISIONING: _ClassVar[Run.Status]
        INITIALIZING: _ClassVar[Run.Status]
        EXECUTING: _ClassVar[Run.Status]
        EXECUTED: _ClassVar[Run.Status]
        TIMEOUT: _ClassVar[Run.Status]
        CPU_EXHAUSTED: _ClassVar[Run.Status]
        MEMORY_OVERFLOW: _ClassVar[Run.Status]
        ERROR: _ClassVar[Run.Status]
        FAILURE: _ClassVar[Run.Status]
    NONE: Run.Status
    PENDING: Run.Status
    PROVISIONING: Run.Status
    INITIALIZING: Run.Status
    EXECUTING: Run.Status
    EXECUTED: Run.Status
    TIMEOUT: Run.Status
    CPU_EXHAUSTED: Run.Status
    MEMORY_OVERFLOW: Run.Status
    ERROR: Run.Status
    FAILURE: Run.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
    CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    runtime: str
    source_url: str
    input_url: str
    status: Run.Status
    error: str
    exit_code: int
    signal: int
    wall_time_usage: int
    cpu_time_usage: int
    memory_usage: int
    resource_usage: _usage_pb2.ResourceUsage
    output_url: str
    def __init__(self, id: _Optional[str] = ..., runtime: _Optional[str] = ..., source_url: _Optional[str] = ..., input_url: _Optional[str] = ..., status: _Optional[_Union[Run.Status, str]] = ..., error: _Optional[str] = ..., exit_code: _Optional[int] = ..., signal: _Optional[int] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[_Union[_usage_pb2.ResourceUsage, _Mapping]] = ..., output_url: _Optional[str] = ...) -> None: ...
