from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeStateInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeStateOutput(_message.Message):
    __slots__ = ["runtime", "source_code", "input_data"]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATA_FIELD_NUMBER: _ClassVar[int]
    runtime: str
    source_code: str
    input_data: str
    def __init__(self, runtime: _Optional[str] = ..., source_code: _Optional[str] = ..., input_data: _Optional[str] = ...) -> None: ...

class UpdateStateInput(_message.Message):
    __slots__ = ["runtime", "source_code", "input_data"]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATA_FIELD_NUMBER: _ClassVar[int]
    runtime: str
    source_code: str
    input_data: str
    def __init__(self, runtime: _Optional[str] = ..., source_code: _Optional[str] = ..., input_data: _Optional[str] = ...) -> None: ...

class UpdateStateOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
