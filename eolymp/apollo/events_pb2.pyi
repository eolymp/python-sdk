from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StarAddedEvent(_message.Message):
    __slots__ = ["problem_id", "user_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    user_id: str
    def __init__(self, problem_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class StarRemovedEvent(_message.Message):
    __slots__ = ["problem_id", "user_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    user_id: str
    def __init__(self, problem_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...
