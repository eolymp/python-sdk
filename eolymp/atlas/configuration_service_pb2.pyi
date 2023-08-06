from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConfigurePolygonInput(_message.Message):
    __slots__ = ["password", "username"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    password: str
    username: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class ConfigurePolygonOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribePolygonInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribePolygonOutput(_message.Message):
    __slots__ = ["password_set", "username"]
    PASSWORD_SET_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    password_set: bool
    username: str
    def __init__(self, username: _Optional[str] = ..., password_set: bool = ...) -> None: ...
