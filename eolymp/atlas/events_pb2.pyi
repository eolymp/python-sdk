from eolymp.atlas import scoring_score_pb2 as _scoring_score_pb2
from eolymp.atlas import submission_pb2 as _submission_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PermissionsDeletedEvent(_message.Message):
    __slots__ = ["problem_id", "user_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    user_id: str
    def __init__(self, problem_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class ScoreUpdatedEvent(_message.Message):
    __slots__ = ["score"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: _scoring_score_pb2.Score
    def __init__(self, score: _Optional[_Union[_scoring_score_pb2.Score, _Mapping]] = ...) -> None: ...

class SubmissionCompleteEvent(_message.Message):
    __slots__ = ["submission", "update"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    update: bool
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ..., update: bool = ...) -> None: ...
