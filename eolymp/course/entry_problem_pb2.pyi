from eolymp.atlas import testing_feedback_pb2 as _testing_feedback_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Problem(_message.Message):
    __slots__ = ["cost", "override_feedback_policy", "problem_id", "problem_url", "submit_limit"]
    COST_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_FEEDBACK_POLICY_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_URL_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    cost: int
    override_feedback_policy: _testing_feedback_pb2.FeedbackPolicy
    problem_id: str
    problem_url: str
    submit_limit: int
    def __init__(self, problem_url: _Optional[str] = ..., problem_id: _Optional[str] = ..., cost: _Optional[int] = ..., submit_limit: _Optional[int] = ..., override_feedback_policy: _Optional[_Union[_testing_feedback_pb2.FeedbackPolicy, str]] = ...) -> None: ...
