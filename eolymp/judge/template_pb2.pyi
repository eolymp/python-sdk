from eolymp.annotations import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Template(_message.Message):
    __slots__ = ["ern", "footer_ern", "header_ern", "id", "problem_id", "runtime", "source_ern"]
    ERN_FIELD_NUMBER: _ClassVar[int]
    FOOTER_ERN_FIELD_NUMBER: _ClassVar[int]
    HEADER_ERN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ERN_FIELD_NUMBER: _ClassVar[int]
    ern: str
    footer_ern: str
    header_ern: str
    id: str
    problem_id: str
    runtime: str
    source_ern: str
    def __init__(self, id: _Optional[str] = ..., ern: _Optional[str] = ..., problem_id: _Optional[str] = ..., runtime: _Optional[str] = ..., source_ern: _Optional[str] = ..., header_ern: _Optional[str] = ..., footer_ern: _Optional[str] = ...) -> None: ...
