from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
SCOPE_FIELD_NUMBER: _ClassVar[int]
scope: _descriptor.FieldDescriptor

class Scope(_message.Message):
    __slots__ = ("scope",)
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    scope: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, scope: _Optional[_Iterable[str]] = ...) -> None: ...
