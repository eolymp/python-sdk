from eolymp.community import member_user_pb2 as _member_user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Team(_message.Message):
    __slots__ = ["staffed", "users"]
    STAFFED_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    staffed: bool
    users: _containers.RepeatedCompositeFieldContainer[_member_user_pb2.User]
    def __init__(self, staffed: bool = ..., users: _Optional[_Iterable[_Union[_member_user_pb2.User, _Mapping]]] = ...) -> None: ...
