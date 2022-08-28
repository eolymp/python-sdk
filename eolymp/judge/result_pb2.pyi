from eolymp.judge import score_pb2 as _score_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Result(_message.Message):
    __slots__ = ["contest_id", "name", "out_of_competition", "participant_id", "rank", "rank_lower", "score"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_COMPETITION_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    RANK_FIELD_NUMBER: _ClassVar[int]
    RANK_LOWER_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    name: str
    out_of_competition: bool
    participant_id: str
    rank: int
    rank_lower: int
    score: _score_pb2.Score
    def __init__(self, participant_id: _Optional[str] = ..., contest_id: _Optional[str] = ..., name: _Optional[str] = ..., out_of_competition: bool = ..., rank: _Optional[int] = ..., rank_lower: _Optional[int] = ..., score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...
