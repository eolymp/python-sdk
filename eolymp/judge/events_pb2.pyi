from eolymp.judge import participant_pb2 as _participant_pb2
from eolymp.judge import score_pb2 as _score_pb2
from eolymp.judge import submission_pb2 as _submission_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

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
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., unofficial: bool = ..., score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class ParticipantChangedEvent(_message.Message):
    __slots__ = ("contest_id", "before", "after")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    before: _participant_pb2.Participant
    after: _participant_pb2.Participant
    def __init__(self, contest_id: _Optional[str] = ..., before: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ..., after: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class ParticipantJoinedEvent(_message.Message):
    __slots__ = ("contest_id", "participant")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant: _participant_pb2.Participant
    def __init__(self, contest_id: _Optional[str] = ..., participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class RetestProblemEvent(_message.Message):
    __slots__ = ("contest_id", "problem_id", "activity_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    activity_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., activity_id: _Optional[str] = ...) -> None: ...
