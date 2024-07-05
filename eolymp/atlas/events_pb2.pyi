from eolymp.acl import acl_service_pb2 as _acl_service_pb2
from eolymp.atlas import problem_pb2 as _problem_pb2
from eolymp.atlas import scoring_score_pb2 as _scoring_score_pb2
from eolymp.atlas import statement_pb2 as _statement_pb2
from eolymp.atlas import submission_pb2 as _submission_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BookmarkChangedEvent(_message.Message):
    __slots__ = ["after", "before", "member_id", "problem_id"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    after: bool
    before: bool
    member_id: str
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., member_id: _Optional[str] = ..., before: bool = ..., after: bool = ...) -> None: ...

class PermissionChangedEvent(_message.Message):
    __slots__ = ["after", "before", "problem_id", "user_id"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    after: _acl_service_pb2.Permission
    before: _acl_service_pb2.Permission
    problem_id: str
    user_id: str
    def __init__(self, problem_id: _Optional[str] = ..., user_id: _Optional[str] = ..., before: _Optional[_Union[_acl_service_pb2.Permission, _Mapping]] = ..., after: _Optional[_Union[_acl_service_pb2.Permission, _Mapping]] = ...) -> None: ...

class ProblemChangedEvent(_message.Message):
    __slots__ = ["after", "before"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    after: _problem_pb2.Problem
    before: _problem_pb2.Problem
    def __init__(self, before: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ..., after: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ...) -> None: ...

class ScoreUpdatedEvent(_message.Message):
    __slots__ = ["score"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: _scoring_score_pb2.Score
    def __init__(self, score: _Optional[_Union[_scoring_score_pb2.Score, _Mapping]] = ...) -> None: ...

class StatementChangedEvent(_message.Message):
    __slots__ = ["after", "before", "problem_id"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    after: _statement_pb2.Statement
    before: _statement_pb2.Statement
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ..., after: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class SubmissionCompleteEvent(_message.Message):
    __slots__ = ["submission", "update"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    update: bool
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ..., update: bool = ...) -> None: ...
