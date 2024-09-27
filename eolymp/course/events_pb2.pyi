from eolymp.course import assignment_pb2 as _assignment_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AssignmentChangedEvent(_message.Message):
    __slots__ = ["after", "before"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    after: _assignment_pb2.Assignment
    before: _assignment_pb2.Assignment
    def __init__(self, before: _Optional[_Union[_assignment_pb2.Assignment, _Mapping]] = ..., after: _Optional[_Union[_assignment_pb2.Assignment, _Mapping]] = ...) -> None: ...
