from eolymp.annotations import resource_pb2 as _resource_pb2
from eolymp.atlas import feedback_pb2 as _feedback_pb2
from eolymp.atlas import scoring_pb2 as _scoring_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Submission(_message.Message):
    __slots__ = ["contest_id", "cost", "ern", "error", "groups", "id", "lang", "participant_id", "percentage", "problem_id", "score", "signature", "source", "status", "submitted_at"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Group(_message.Message):
        __slots__ = ["cost", "cpu_time_usage", "dependencies", "feedback_policy", "index", "memory_usage", "runs", "score", "scoring_mode", "status", "testset_id", "wall_time_usage"]
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ACCEPTED: Submission.Group.Status
        BLOCKED: Submission.Group.Status
        COST_FIELD_NUMBER: _ClassVar[int]
        CPU_EXHAUSTED: Submission.Group.Status
        CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
        FEEDBACK_POLICY_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        MEMORY_OVERFLOW: Submission.Group.Status
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        PENDING: Submission.Group.Status
        RUNS_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_ERROR: Submission.Group.Status
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SCORING_MODE_FIELD_NUMBER: _ClassVar[int]
        SKIPPED: Submission.Group.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TESTING: Submission.Group.Status
        TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT: Submission.Group.Status
        UNKNOWN: Submission.Group.Status
        VERIFICATION_ERROR: Submission.Group.Status
        WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        WRONG_ANSWER: Submission.Group.Status
        cost: float
        cpu_time_usage: int
        dependencies: _containers.RepeatedScalarFieldContainer[int]
        feedback_policy: _feedback_pb2.FeedbackPolicy
        index: int
        memory_usage: int
        runs: _containers.RepeatedCompositeFieldContainer[Submission.Run]
        score: float
        scoring_mode: _scoring_pb2.ScoringMode
        status: Submission.Group.Status
        testset_id: str
        wall_time_usage: int
        def __init__(self, index: _Optional[int] = ..., testset_id: _Optional[str] = ..., status: _Optional[_Union[Submission.Group.Status, str]] = ..., dependencies: _Optional[_Iterable[int]] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., scoring_mode: _Optional[_Union[_scoring_pb2.ScoringMode, str]] = ..., feedback_policy: _Optional[_Union[_feedback_pb2.FeedbackPolicy, str]] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., runs: _Optional[_Iterable[_Union[Submission.Run, _Mapping]]] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ["cost", "cpu_time_usage", "id", "index", "memory_usage", "score", "status", "test_id", "wall_time_usage"]
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ACCEPTED: Submission.Run.Status
        BLOCKED: Submission.Run.Status
        COST_FIELD_NUMBER: _ClassVar[int]
        CPU_EXHAUSTED: Submission.Run.Status
        CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        CREATED: Submission.Run.Status
        EXECUTING: Submission.Run.Status
        ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        MEMORY_OVERFLOW: Submission.Run.Status
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        NONE: Submission.Run.Status
        RUNTIME_ERROR: Submission.Run.Status
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SKIPPED: Submission.Run.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TEST_ID_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT: Submission.Run.Status
        VERIFICATION_ERROR: Submission.Run.Status
        WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        WRONG_ANSWER: Submission.Run.Status
        cost: float
        cpu_time_usage: int
        id: str
        index: int
        memory_usage: int
        score: float
        status: Submission.Run.Status
        test_id: str
        wall_time_usage: int
        def __init__(self, id: _Optional[str] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., index: _Optional[int] = ..., test_id: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., status: _Optional[_Union[Submission.Run.Status, str]] = ...) -> None: ...
    COMPLETE: Submission.Status
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    ERN_FIELD_NUMBER: _ClassVar[int]
    ERROR: Submission.Status
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FAILURE: Submission.Status
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    NONE: Submission.Status
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    PENDING: Submission.Status
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    TESTING: Submission.Status
    TIMEOUT: Submission.Status
    contest_id: str
    cost: float
    ern: str
    error: str
    groups: _containers.RepeatedCompositeFieldContainer[Submission.Group]
    id: str
    lang: str
    participant_id: str
    percentage: float
    problem_id: str
    score: float
    signature: str
    source: str
    status: Submission.Status
    submitted_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., ern: _Optional[str] = ..., contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lang: _Optional[str] = ..., source: _Optional[str] = ..., signature: _Optional[str] = ..., status: _Optional[_Union[Submission.Status, str]] = ..., error: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., percentage: _Optional[float] = ..., groups: _Optional[_Iterable[_Union[Submission.Group, _Mapping]]] = ...) -> None: ...
