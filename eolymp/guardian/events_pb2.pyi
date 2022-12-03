from eolymp.guardian import policy_pb2 as _policy_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PolicyChangedEvent(_message.Message):
    __slots__ = ["created", "deleted"]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    created: _policy_pb2.Policy
    deleted: _policy_pb2.Policy
    def __init__(self, created: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ..., deleted: _Optional[_Union[_policy_pb2.Policy, _Mapping]] = ...) -> None: ...
