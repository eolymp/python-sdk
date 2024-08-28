from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Stats(_message.Message):
    __slots__ = ["cpu_time_duration", "exit_code", "memory_peak", "signal", "stderr_url", "stdin_url", "stdout_url", "wall_time_duration"]
    CPU_TIME_DURATION_FIELD_NUMBER: _ClassVar[int]
    EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_PEAK_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    STDERR_URL_FIELD_NUMBER: _ClassVar[int]
    STDIN_URL_FIELD_NUMBER: _ClassVar[int]
    STDOUT_URL_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_DURATION_FIELD_NUMBER: _ClassVar[int]
    cpu_time_duration: int
    exit_code: int
    memory_peak: int
    signal: int
    stderr_url: str
    stdin_url: str
    stdout_url: str
    wall_time_duration: int
    def __init__(self, stdin_url: _Optional[str] = ..., stdout_url: _Optional[str] = ..., stderr_url: _Optional[str] = ..., wall_time_duration: _Optional[int] = ..., cpu_time_duration: _Optional[int] = ..., memory_peak: _Optional[int] = ..., signal: _Optional[int] = ..., exit_code: _Optional[int] = ...) -> None: ...
