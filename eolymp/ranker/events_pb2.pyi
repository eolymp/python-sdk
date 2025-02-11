from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RebuildScoreboardEvent(_message.Message):
    __slots__ = ("space_id", "scoreboard_id", "activity_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    scoreboard_id: str
    activity_id: str
    def __init__(self, space_id: _Optional[str] = ..., scoreboard_id: _Optional[str] = ..., activity_id: _Optional[str] = ...) -> None: ...
