from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.playground import run_pb2 as _run_pb2
from eolymp.wellknown import watch_pb2 as _watch_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRunInput(_message.Message):
    __slots__ = ("problem_id", "runtime", "trace", "source", "input_data", "input_ref", "example_id")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    TRACE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATA_FIELD_NUMBER: _ClassVar[int]
    INPUT_REF_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    runtime: str
    trace: bool
    source: str
    input_data: bytes
    input_ref: str
    example_id: str
    def __init__(self, problem_id: _Optional[str] = ..., runtime: _Optional[str] = ..., trace: _Optional[bool] = ..., source: _Optional[str] = ..., input_data: _Optional[bytes] = ..., input_ref: _Optional[str] = ..., example_id: _Optional[str] = ...) -> None: ...

class CreateRunOutput(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class DescribeRunInput(_message.Message):
    __slots__ = ("problem_id", "run_id")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    run_id: str
    def __init__(self, problem_id: _Optional[str] = ..., run_id: _Optional[str] = ...) -> None: ...

class DescribeRunOutput(_message.Message):
    __slots__ = ("run",)
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: _run_pb2.Run
    def __init__(self, run: _Optional[_Union[_run_pb2.Run, _Mapping]] = ...) -> None: ...

class WatchRunInput(_message.Message):
    __slots__ = ("problem_id", "run_id")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    run_id: str
    def __init__(self, problem_id: _Optional[str] = ..., run_id: _Optional[str] = ...) -> None: ...

class WatchRunOutput(_message.Message):
    __slots__ = ("run", "event")
    RUN_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    run: _run_pb2.Run
    event: _watch_pb2.WatchEventType
    def __init__(self, run: _Optional[_Union[_run_pb2.Run, _Mapping]] = ..., event: _Optional[_Union[_watch_pb2.WatchEventType, str]] = ...) -> None: ...
