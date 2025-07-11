from eolymp.acl import action_pb2 as _action_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Policy(_message.Message):
    __slots__ = ("id", "name", "principal", "resource", "allow_all", "allows")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_FIELD_NUMBER: _ClassVar[int]
    ALLOWS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    principal: str
    resource: str
    allow_all: bool
    allows: _containers.RepeatedScalarFieldContainer[_action_pb2.Action]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., principal: _Optional[str] = ..., resource: _Optional[str] = ..., allow_all: bool = ..., allows: _Optional[_Iterable[_Union[_action_pb2.Action, str]]] = ...) -> None: ...
