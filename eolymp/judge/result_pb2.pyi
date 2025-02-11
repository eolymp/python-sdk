from eolymp.judge import medal_pb2 as _medal_pb2
from eolymp.judge import score_pb2 as _score_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Result(_message.Message):
    __slots__ = ("participant_id", "member_id", "contest_id", "name", "unofficial", "disqualified", "ghost", "medal", "rank", "rank_lower", "score")
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    DISQUALIFIED_FIELD_NUMBER: _ClassVar[int]
    GHOST_FIELD_NUMBER: _ClassVar[int]
    MEDAL_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    RANK_LOWER_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    participant_id: str
    member_id: str
    contest_id: str
    name: str
    unofficial: bool
    disqualified: bool
    ghost: bool
    medal: _medal_pb2.Medal
    rank: int
    rank_lower: int
    score: _score_pb2.Score
    def __init__(self, participant_id: _Optional[str] = ..., member_id: _Optional[str] = ..., contest_id: _Optional[str] = ..., name: _Optional[str] = ..., unofficial: bool = ..., disqualified: bool = ..., ghost: bool = ..., medal: _Optional[_Union[_medal_pb2.Medal, str]] = ..., rank: _Optional[int] = ..., rank_lower: _Optional[int] = ..., score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...
