from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Student(_message.Message):
    __slots__ = ["course_id", "display_name", "id", "member_id"]
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    display_name: str
    id: str
    member_id: str
    def __init__(self, id: _Optional[str] = ..., course_id: _Optional[str] = ..., member_id: _Optional[str] = ..., display_name: _Optional[str] = ...) -> None: ...
