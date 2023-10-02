from eolymp.cognito import user_pb2 as _user_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserChangedEvent(_message.Message):
    __slots__ = ["after", "before"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    after: _user_pb2.User
    before: _user_pb2.User
    def __init__(self, before: _Optional[_Union[_user_pb2.User, _Mapping]] = ..., after: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...
