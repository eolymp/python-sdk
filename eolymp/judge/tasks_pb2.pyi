import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RetestProblemTask(_message.Message):
    __slots__ = ("contest_id", "problem_id")
    class Checkpoint(_message.Message):
        __slots__ = ("submitted_before", "retested")
        SUBMITTED_BEFORE_FIELD_NUMBER: _ClassVar[int]
        RETESTED_FIELD_NUMBER: _ClassVar[int]
        submitted_before: _timestamp_pb2.Timestamp
        retested: int
        def __init__(self, submitted_before: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., retested: _Optional[int] = ...) -> None: ...
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class RebuildScoreTask(_message.Message):
    __slots__ = ("contest_id",)
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class AnalyzeContestTask(_message.Message):
    __slots__ = ("contest_id",)
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...
