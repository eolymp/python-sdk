from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SeedScoreboardContestTask(_message.Message):
    __slots__ = ("scoreboard_id", "contest_id")
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    contest_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ..., contest_id: _Optional[str] = ...) -> None: ...

class RebuildScoreboardTask(_message.Message):
    __slots__ = ("scoreboard_id",)
    SCOREBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    scoreboard_id: str
    def __init__(self, scoreboard_id: _Optional[str] = ...) -> None: ...
