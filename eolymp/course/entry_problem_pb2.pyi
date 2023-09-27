from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Problem(_message.Message):
    __slots__ = ["problem_url"]
    PROBLEM_URL_FIELD_NUMBER: _ClassVar[int]
    problem_url: str
    def __init__(self, problem_url: _Optional[str] = ...) -> None: ...
