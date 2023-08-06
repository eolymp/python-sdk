from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import problem_pb2 as _problem_pb2
from eolymp.atlas import statement_pb2 as _statement_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImportPolygonProblemInput(_message.Message):
    __slots__ = ["password", "url", "username"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    password: str
    url: str
    username: str
    def __init__(self, url: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class ImportPolygonProblemOutput(_message.Message):
    __slots__ = ["job_id", "problem_id"]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., job_id: _Optional[str] = ...) -> None: ...
