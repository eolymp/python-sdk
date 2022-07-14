from eolymp.atlas import permission_pb2 as _permission_pb2
from eolymp.atlas import problem_pb2 as _problem_pb2
from eolymp.atlas import score_pb2 as _score_pb2
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

class PermissionsUpdatedEvent(_message.Message):
    __slots__ = ["permission", "problem_id"]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    permission: _permission_pb2.Permission
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., permission: _Optional[_Union[_permission_pb2.Permission, _Mapping]] = ...) -> None: ...

class ProblemDeletedEvent(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ProblemUpdatedEvent(_message.Message):
    __slots__ = ["problem"]
    PROBLEM_FIELD_NUMBER: _ClassVar[int]
    problem: _problem_pb2.Problem
    def __init__(self, problem: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ...) -> None: ...

class ScoreUpdatedEvent(_message.Message):
    __slots__ = ["score"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: _score_pb2.Score
    def __init__(self, score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class SubmissionCompleteEvent(_message.Message):
    __slots__ = ["submission", "update"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    update: bool
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ..., update: bool = ...) -> None: ...
