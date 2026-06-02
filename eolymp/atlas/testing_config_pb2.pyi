from eolymp.atlas import problem_pb2 as _problem_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestingConfig(_message.Message):
    __slots__ = ("run_count", "interactive_followup", "type")
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVE_FOLLOWUP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    run_count: int
    interactive_followup: bool
    type: _problem_pb2.Problem.Type
    def __init__(self, run_count: _Optional[int] = ..., interactive_followup: _Optional[bool] = ..., type: _Optional[_Union[_problem_pb2.Problem.Type, str]] = ...) -> None: ...
