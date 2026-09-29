from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.executor import file_pb2 as _file_pb2
from eolymp.executor import run_pb2 as _run_pb2
from eolymp.wellknown import watch_pb2 as _watch_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRunInput(_message.Message):
    __slots__ = ("program", "arguments", "interactor", "input_url", "input_content", "wall_time_limit", "cpu_time_limit", "memory_limit")
    class Program(_message.Message):
        __slots__ = ("runtime", "source", "files")
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        FILES_FIELD_NUMBER: _ClassVar[int]
        runtime: str
        source: str
        files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
        def __init__(self, runtime: _Optional[str] = ..., source: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...
    PROGRAM_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CPU_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    program: CreateRunInput.Program
    arguments: _containers.RepeatedScalarFieldContainer[str]
    interactor: CreateRunInput.Program
    input_url: str
    input_content: str
    wall_time_limit: int
    cpu_time_limit: int
    memory_limit: int
    def __init__(self, program: _Optional[_Union[CreateRunInput.Program, _Mapping]] = ..., arguments: _Optional[_Iterable[str]] = ..., interactor: _Optional[_Union[CreateRunInput.Program, _Mapping]] = ..., input_url: _Optional[str] = ..., input_content: _Optional[str] = ..., wall_time_limit: _Optional[int] = ..., cpu_time_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ...) -> None: ...

class CreateRunOutput(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class DescribeRunInput(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class DescribeRunOutput(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: _run_pb2.Run
    def __init__(self, run: _Optional[_Union[_run_pb2.Run, _Mapping]] = ...) -> None: ...

class WatchRunInput(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class WatchRunOutput(_message.Message):
    __slots__ = ("event", "run")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    RUN_FIELD_NUMBER: _ClassVar[int]
    event: _watch_pb2.WatchEventType
    run: _run_pb2.Run
    def __init__(self, event: _Optional[_Union[_watch_pb2.WatchEventType, str]] = ..., run: _Optional[_Union[_run_pb2.Run, _Mapping]] = ...) -> None: ...
