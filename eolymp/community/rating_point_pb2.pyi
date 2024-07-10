from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RatingPoint(_message.Message):
    __slots__ = ["id", "ref", "source", "target_link", "timestamp", "value"]
    class Source(_message.Message):
        __slots__ = ["id", "name", "penalty", "rank", "rank_lower", "rank_total", "score", "tie_breaker", "url"]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PENALTY_FIELD_NUMBER: _ClassVar[int]
        RANK_FIELD_NUMBER: _ClassVar[int]
        RANK_LOWER_FIELD_NUMBER: _ClassVar[int]
        RANK_TOTAL_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        TIE_BREAKER_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        penalty: int
        rank: int
        rank_lower: int
        rank_total: int
        score: int
        tie_breaker: int
        url: str
        def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., score: _Optional[int] = ..., penalty: _Optional[int] = ..., tie_breaker: _Optional[int] = ..., rank: _Optional[int] = ..., rank_lower: _Optional[int] = ..., rank_total: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LINK_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    ref: str
    source: RatingPoint.Source
    target_link: str
    timestamp: _timestamp_pb2.Timestamp
    value: int
    def __init__(self, id: _Optional[str] = ..., ref: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[int] = ..., source: _Optional[_Union[RatingPoint.Source, _Mapping]] = ..., target_link: _Optional[str] = ...) -> None: ...
