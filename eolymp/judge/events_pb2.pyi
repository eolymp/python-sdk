from eolymp.judge import contest_pb2 as _contest_pb2
from eolymp.judge import participant_pb2 as _participant_pb2
from eolymp.judge import score_pb2 as _score_pb2
from eolymp.judge import submission_pb2 as _submission_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParticipantChangedEvent(_message.Message):
    __slots__ = ["after", "before"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    after: _participant_pb2.Participant
    before: _participant_pb2.Participant
    def __init__(self, before: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ..., after: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class ParticipantJoinedEvent(_message.Message):
    __slots__ = ["contest", "participant"]
    CONTEST_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_FIELD_NUMBER: _ClassVar[int]
    contest: _contest_pb2.Contest
    participant: _participant_pb2.Participant
    def __init__(self, contest: _Optional[_Union[_contest_pb2.Contest, _Mapping]] = ..., participant: _Optional[_Union[_participant_pb2.Participant, _Mapping]] = ...) -> None: ...

class RebuildScoreEvent(_message.Message):
    __slots__ = ["activity_id", "contest_id"]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ..., activity_id: _Optional[str] = ...) -> None: ...

class RetestProblemEvent(_message.Message):
    __slots__ = ["activity_id", "contest_id", "problem_id"]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., activity_id: _Optional[str] = ...) -> None: ...

class ScoreUpdatedEvent(_message.Message):
    __slots__ = ["contest_id", "participant_id", "score", "unofficial"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    score: _score_pb2.Score
    unofficial: bool
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., unofficial: bool = ..., score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class SubmissionCompletedEvent(_message.Message):
    __slots__ = ["submission"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...
