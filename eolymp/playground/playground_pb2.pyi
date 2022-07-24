from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.playground import run_pb2 as _run_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRunInput(_message.Message):
    __slots__ = ["input", "input_content", "input_ern", "input_object_id", "lang", "problem_ern", "runtime", "source", "source_ern"]
    INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_ERN_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    INPUT_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ERN_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ERN_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    input: str
    input_content: bytes
    input_ern: str
    input_object_id: str
    lang: str
    problem_ern: str
    runtime: str
    source: str
    source_ern: str
    def __init__(self, lang: _Optional[str] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., source_ern: _Optional[str] = ..., input_ern: _Optional[str] = ..., problem_ern: _Optional[str] = ..., input: _Optional[str] = ..., input_content: _Optional[bytes] = ..., input_object_id: _Optional[str] = ...) -> None: ...

class CreateRunOutput(_message.Message):
    __slots__ = ["run_id"]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class DescribeRunInput(_message.Message):
    __slots__ = ["run_id"]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class DescribeRunOutput(_message.Message):
    __slots__ = ["run"]
    RUN_FIELD_NUMBER: _ClassVar[int]
    run: _run_pb2.Run
    def __init__(self, run: _Optional[_Union[_run_pb2.Run, _Mapping]] = ...) -> None: ...
