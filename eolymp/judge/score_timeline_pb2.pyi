from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScoreTimelinePoint(_message.Message):
    __slots__ = ("offset", "score", "penalty")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    PENALTY_FIELD_NUMBER: _ClassVar[int]
    offset: int
    score: float
    penalty: float
    def __init__(self, offset: _Optional[int] = ..., score: _Optional[float] = ..., penalty: _Optional[float] = ...) -> None: ...
