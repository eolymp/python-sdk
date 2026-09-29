from eolymp.executor import script_pb2 as _script_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionTask(_message.Message):
    __slots__ = ("task_id", "reference", "origin", "metadata", "program", "arguments", "interactor", "input_url", "input_content", "wall_time_limit", "cpu_time_limit", "memory_limit", "file_size_limit", "redirect_stderr_to_stdout", "trace")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CPU_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_STDERR_TO_STDOUT_FIELD_NUMBER: _ClassVar[int]
    TRACE_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    reference: str
    origin: str
    metadata: _containers.ScalarMap[str, str]
    program: _script_pb2.Script
    arguments: _containers.RepeatedScalarFieldContainer[str]
    interactor: _script_pb2.Script
    input_url: str
    input_content: str
    wall_time_limit: int
    cpu_time_limit: int
    memory_limit: int
    file_size_limit: int
    redirect_stderr_to_stdout: bool
    trace: bool
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., program: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., arguments: _Optional[_Iterable[str]] = ..., interactor: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., input_url: _Optional[str] = ..., input_content: _Optional[str] = ..., wall_time_limit: _Optional[int] = ..., cpu_time_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ..., file_size_limit: _Optional[int] = ..., redirect_stderr_to_stdout: _Optional[bool] = ..., trace: _Optional[bool] = ...) -> None: ...
