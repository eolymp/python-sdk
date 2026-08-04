from eolymp.universe import space_pb2 as _space_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceChangedEvent(_message.Message):
    __slots__ = ("before", "after")
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    before: _space_pb2.Space
    after: _space_pb2.Space
    def __init__(self, before: _Optional[_Union[_space_pb2.Space, _Mapping]] = ..., after: _Optional[_Union[_space_pb2.Space, _Mapping]] = ...) -> None: ...
