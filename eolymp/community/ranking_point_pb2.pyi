from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RankingPoint(_message.Message):
    __slots__ = ["event_id", "id", "member_id", "rank", "rank_lower", "score"]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    RANK_LOWER_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    id: str
    member_id: str
    rank: int
    rank_lower: int
    score: int
    def __init__(self, id: _Optional[str] = ..., member_id: _Optional[str] = ..., event_id: _Optional[str] = ..., rank: _Optional[int] = ..., rank_lower: _Optional[int] = ..., score: _Optional[int] = ...) -> None: ...
