from eolymp.acl import action_pb2 as _action_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Policy(_message.Message):
    __slots__ = ["allow_all", "allows", "id", "name", "resource", "subject"]
    ALLOWS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    allow_all: bool
    allows: _containers.RepeatedScalarFieldContainer[_action_pb2.Action]
    id: str
    name: str
    resource: str
    subject: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., subject: _Optional[str] = ..., resource: _Optional[str] = ..., allow_all: bool = ..., allows: _Optional[_Iterable[_Union[_action_pb2.Action, str]]] = ...) -> None: ...
