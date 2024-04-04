from eolymp.executor import usage_pb2 as _usage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Stats(_message.Message):
    __slots__ = ["cpu_time_duration", "cpu_time_usage", "exit_code", "memory_peak", "memory_usage", "overall_usage", "resource_usage", "signal", "stderr_url", "stdin_url", "stdout_url", "wall_time_duration", "wall_time_usage"]
    CPU_TIME_DURATION_FIELD_NUMBER: _ClassVar[int]
    CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_PEAK_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    OVERALL_USAGE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    STDERR_URL_FIELD_NUMBER: _ClassVar[int]
    STDIN_URL_FIELD_NUMBER: _ClassVar[int]
    STDOUT_URL_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_DURATION_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
    cpu_time_duration: int
    cpu_time_usage: float
    exit_code: int
    memory_peak: int
    memory_usage: float
    overall_usage: float
    resource_usage: _usage_pb2.ResourceUsage
    signal: int
    stderr_url: str
    stdin_url: str
    stdout_url: str
    wall_time_duration: int
    wall_time_usage: float
    def __init__(self, stdin_url: _Optional[str] = ..., stdout_url: _Optional[str] = ..., stderr_url: _Optional[str] = ..., overall_usage: _Optional[float] = ..., wall_time_duration: _Optional[int] = ..., wall_time_usage: _Optional[float] = ..., cpu_time_duration: _Optional[int] = ..., cpu_time_usage: _Optional[float] = ..., memory_peak: _Optional[int] = ..., memory_usage: _Optional[float] = ..., resource_usage: _Optional[_Union[_usage_pb2.ResourceUsage, _Mapping]] = ..., exit_code: _Optional[int] = ..., signal: _Optional[int] = ...) -> None: ...
