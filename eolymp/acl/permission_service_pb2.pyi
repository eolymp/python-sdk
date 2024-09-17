from eolymp.acl import action_pb2 as _action_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IntrospectPermissionsInput(_message.Message):
    __slots__ = ["resource"]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    resource: str
    def __init__(self, resource: _Optional[str] = ...) -> None: ...

class IntrospectPermissionsOutput(_message.Message):
    __slots__ = ["actions"]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[_action_pb2.Action]
    def __init__(self, actions: _Optional[_Iterable[_Union[_action_pb2.Action, str]]] = ...) -> None: ...
