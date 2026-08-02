from eolymp.judge import score_pb2 as _score_pb2
from eolymp.judge import submission_pb2 as _submission_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubmissionCompletedEvent(_message.Message):
    __slots__ = ("contest_id", "submission")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    submission: _submission_pb2.Submission
    def __init__(self, contest_id: _Optional[str] = ..., submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...

class RebuildScoreEvent(_message.Message):
    __slots__ = ("contest_id", "activity_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    activity_id: str
    def __init__(self, contest_id: _Optional[str] = ..., activity_id: _Optional[str] = ...) -> None: ...

class ScoreChangedEvent(_message.Message):
    __slots__ = ("contest_id", "participant_id", "unofficial", "score")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    unofficial: bool
    score: _score_pb2.Score
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., unofficial: _Optional[bool] = ..., score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class RetestProblemEvent(_message.Message):
    __slots__ = ("contest_id", "problem_id", "activity_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    activity_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., activity_id: _Optional[str] = ...) -> None: ...

class ScoreboardRowChangedEvent(_message.Message):
    __slots__ = ("contest_id", "kind", "participant_id", "member_id", "version")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_KIND: _ClassVar[ScoreboardRowChangedEvent.Kind]
        RESULT: _ClassVar[ScoreboardRowChangedEvent.Kind]
        FROZEN: _ClassVar[ScoreboardRowChangedEvent.Kind]
        UPSOLVE: _ClassVar[ScoreboardRowChangedEvent.Kind]
    UNKNOWN_KIND: ScoreboardRowChangedEvent.Kind
    RESULT: ScoreboardRowChangedEvent.Kind
    FROZEN: ScoreboardRowChangedEvent.Kind
    UPSOLVE: ScoreboardRowChangedEvent.Kind
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    kind: ScoreboardRowChangedEvent.Kind
    participant_id: str
    member_id: str
    version: int
    def __init__(self, contest_id: _Optional[str] = ..., kind: _Optional[_Union[ScoreboardRowChangedEvent.Kind, str]] = ..., participant_id: _Optional[str] = ..., member_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...
