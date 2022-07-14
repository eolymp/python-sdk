from eolymp.annotations import resource_pb2 as _resource_pb2
from eolymp.atlas import feedback_pb2 as _feedback_pb2
from eolymp.atlas import scoring_pb2 as _scoring_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Testset(_message.Message):
    __slots__ = ["dependencies", "feedback_policy", "file_size_limit", "id", "index", "memory_limit", "problem_id", "scoring_mode", "time_limit"]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_POLICY_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCORING_MODE_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    dependencies: _containers.RepeatedScalarFieldContainer[int]
    feedback_policy: _feedback_pb2.FeedbackPolicy
    file_size_limit: int
    id: str
    index: int
    memory_limit: int
    problem_id: str
    scoring_mode: _scoring_pb2.ScoringMode
    time_limit: int
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., index: _Optional[int] = ..., time_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ..., file_size_limit: _Optional[int] = ..., dependencies: _Optional[_Iterable[int]] = ..., scoring_mode: _Optional[_Union[_scoring_pb2.ScoringMode, str]] = ..., feedback_policy: _Optional[_Union[_feedback_pb2.FeedbackPolicy, str]] = ...) -> None: ...
