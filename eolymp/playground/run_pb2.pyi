from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Run(_message.Message):
    __slots__ = ["cpu_time_usage", "error", "exit_code", "id", "input", "lang", "memory_usage", "output", "signal", "source", "status", "wall_time_usage"]
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
    INPUT_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    MEMORY_OVERFLOW: Run.Status
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    NONE: Run.Status
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    PENDING: Run.Status
    SIGNAL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT: Run.Status
    WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
    cpu_time_usage: int
    error: str
    exit_code: int
    id: str
    input: str
    lang: str
    memory_usage: int
    output: str
    signal: int
    source: str
    status: Run.Status
    wall_time_usage: int
    def __init__(self, id: _Optional[str] = ..., lang: _Optional[str] = ..., source: _Optional[str] = ..., input: _Optional[str] = ..., status: _Optional[_Union[Run.Status, str]] = ..., error: _Optional[str] = ..., exit_code: _Optional[int] = ..., signal: _Optional[int] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., output: _Optional[str] = ...) -> None: ...
