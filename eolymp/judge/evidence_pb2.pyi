import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Evidence(_message.Message):
    __slots__ = ("id", "submission", "pair")
    class Span(_message.Message):
        __slots__ = ("from_line", "to_line")
        FROM_LINE_FIELD_NUMBER: _ClassVar[int]
        TO_LINE_FIELD_NUMBER: _ClassVar[int]
        from_line: int
        to_line: int
        def __init__(self, from_line: _Optional[int] = ..., to_line: _Optional[int] = ...) -> None: ...
    class Submission(_message.Message):
        __slots__ = ("submission_id", "submitted_at", "spans")
        SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
        SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
        SPANS_FIELD_NUMBER: _ClassVar[int]
        submission_id: str
        submitted_at: _timestamp_pb2.Timestamp
        spans: _containers.RepeatedCompositeFieldContainer[Evidence.Span]
        def __init__(self, submission_id: _Optional[str] = ..., submitted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., spans: _Optional[_Iterable[_Union[Evidence.Span, _Mapping]]] = ...) -> None: ...
    class Pair(_message.Message):
        __slots__ = ("left", "right", "score")
        LEFT_FIELD_NUMBER: _ClassVar[int]
        RIGHT_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        left: Evidence.Submission
        right: Evidence.Submission
        score: float
        def __init__(self, left: _Optional[_Union[Evidence.Submission, _Mapping]] = ..., right: _Optional[_Union[Evidence.Submission, _Mapping]] = ..., score: _Optional[float] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    id: str
    submission: Evidence.Submission
    pair: Evidence.Pair
    def __init__(self, id: _Optional[str] = ..., submission: _Optional[_Union[Evidence.Submission, _Mapping]] = ..., pair: _Optional[_Union[Evidence.Pair, _Mapping]] = ...) -> None: ...
