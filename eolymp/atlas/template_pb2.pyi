from eolymp.annotations import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Template(_message.Message):
    __slots__ = ["footer", "header", "id", "problem_id", "runtime", "source"]
    FOOTER_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    footer: str
    header: str
    id: str
    problem_id: str
    runtime: str
    source: str
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., header: _Optional[str] = ..., footer: _Optional[str] = ...) -> None: ...
