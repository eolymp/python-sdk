from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Score(_message.Message):
    __slots__ = ["accepted_at", "id", "problem_id", "score", "user_id"]
    ACCEPTED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    accepted_at: _timestamp_pb2.Timestamp
    id: str
    problem_id: str
    score: float
    user_id: str
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., user_id: _Optional[str] = ..., accepted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., score: _Optional[float] = ...) -> None: ...
