from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TestingConfig(_message.Message):
    __slots__ = ("run_count", "interactive_followup")
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVE_FOLLOWUP_FIELD_NUMBER: _ClassVar[int]
    run_count: int
    interactive_followup: bool
    def __init__(self, run_count: _Optional[int] = ..., interactive_followup: bool = ...) -> None: ...
