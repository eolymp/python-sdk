from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.playground import run_pb2 as _run_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRunInput(_message.Message):
    __slots__ = ["atlas_problem_id", "input", "input_content", "input_object_id", "judge_problem_id", "lang", "source"]
    ATLAS_PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    INPUT_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JUDGE_PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    atlas_problem_id: str
    input: str
    input_content: bytes
    input_object_id: str
    judge_problem_id: str
    lang: str
    source: str
    def __init__(self, lang: _Optional[str] = ..., source: _Optional[str] = ..., input: _Optional[str] = ..., input_content: _Optional[bytes] = ..., input_object_id: _Optional[str] = ..., atlas_problem_id: _Optional[str] = ..., judge_problem_id: _Optional[str] = ...) -> None: ...

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
