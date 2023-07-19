from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TestingConfig(_message.Message):
    __slots__ = ["run_count"]
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    run_count: int
    def __init__(self, run_count: _Optional[int] = ...) -> None: ...
