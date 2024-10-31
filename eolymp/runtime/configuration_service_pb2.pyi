from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigureRuntimeConfigInput(_message.Message):
    __slots__ = ["allowed_runtime"]
    ALLOWED_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    allowed_runtime: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allowed_runtime: _Optional[_Iterable[str]] = ...) -> None: ...

class ConfigureRuntimeConfigOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeRuntimeConfigInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeRuntimeConfigOutput(_message.Message):
    __slots__ = ["allowed_runtime"]
    ALLOWED_RUNTIME_FIELD_NUMBER: _ClassVar[int]
    allowed_runtime: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, allowed_runtime: _Optional[_Iterable[str]] = ...) -> None: ...
