import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.atlas import submission_pb2 as _submission_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Evidence(_message.Message):
    __slots__ = ("id", "submission", "pair", "session")
    class Submission(_message.Message):
        __slots__ = ("submission_id", "submitted_at")
        SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
        SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
        submission_id: str
        submitted_at: _timestamp_pb2.Timestamp
        def __init__(self, submission_id: _Optional[str] = ..., submitted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Pair(_message.Message):
        __slots__ = ("left", "right", "score")
        LEFT_FIELD_NUMBER: _ClassVar[int]
        RIGHT_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        left: Evidence.Submission
        right: Evidence.Submission
        score: float
        def __init__(self, left: _Optional[_Union[Evidence.Submission, _Mapping]] = ..., right: _Optional[_Union[Evidence.Submission, _Mapping]] = ..., score: _Optional[float] = ...) -> None: ...
    class Attempt(_message.Message):
        __slots__ = ("submission_id", "problem_id", "submitted_at", "verdict")
        SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        submission_id: str
        problem_id: str
        submitted_at: _timestamp_pb2.Timestamp
        verdict: _submission_pb2.Submission.Verdict
        def __init__(self, submission_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., submitted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., verdict: _Optional[_Union[_submission_pb2.Submission.Verdict, str]] = ...) -> None: ...
    class Session(_message.Message):
        __slots__ = ("to", "value", "typical", "attempts")
        FROM_FIELD_NUMBER: _ClassVar[int]
        TO_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TYPICAL_FIELD_NUMBER: _ClassVar[int]
        ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        to: _timestamp_pb2.Timestamp
        value: float
        typical: float
        attempts: _containers.RepeatedCompositeFieldContainer[Evidence.Attempt]
        def __init__(self, to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., value: _Optional[float] = ..., typical: _Optional[float] = ..., attempts: _Optional[_Iterable[_Union[Evidence.Attempt, _Mapping]]] = ..., **kwargs) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    PAIR_FIELD_NUMBER: _ClassVar[int]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    submission: Evidence.Submission
    pair: Evidence.Pair
    session: Evidence.Session
    def __init__(self, id: _Optional[str] = ..., submission: _Optional[_Union[Evidence.Submission, _Mapping]] = ..., pair: _Optional[_Union[Evidence.Pair, _Mapping]] = ..., session: _Optional[_Union[Evidence.Session, _Mapping]] = ...) -> None: ...
