from eolymp.atlas import testing_feedback_pb2 as _testing_feedback_pb2
from eolymp.atlas import testing_scoring_pb2 as _testing_scoring_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Submission(_message.Message):
    __slots__ = ["cost", "cpu_time_usage", "error", "groups", "id", "lang", "member_id", "memory_usage", "percentage", "problem_id", "resource_usage", "score", "signature", "source", "status", "submitted_at", "user_id", "wall_time_usage"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Group(_message.Message):
        __slots__ = ["cost", "cpu_time_usage", "dependencies", "feedback_policy", "index", "memory_usage", "resource_usage", "runs", "score", "scoring_mode", "status", "testset_id", "wall_time_usage"]
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
        RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
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
        feedback_policy: _testing_feedback_pb2.FeedbackPolicy
        index: int
        memory_usage: int
        resource_usage: float
        runs: _containers.RepeatedCompositeFieldContainer[Submission.Run]
        score: float
        scoring_mode: _testing_scoring_pb2.ScoringMode
        status: Submission.Group.Status
        testset_id: str
        wall_time_usage: int
        def __init__(self, index: _Optional[int] = ..., testset_id: _Optional[str] = ..., status: _Optional[_Union[Submission.Group.Status, str]] = ..., dependencies: _Optional[_Iterable[int]] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., scoring_mode: _Optional[_Union[_testing_scoring_pb2.ScoringMode, str]] = ..., feedback_policy: _Optional[_Union[_testing_feedback_pb2.FeedbackPolicy, str]] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[float] = ..., runs: _Optional[_Iterable[_Union[Submission.Run, _Mapping]]] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ["cost", "cpu_time_usage", "id", "index", "memory_usage", "resource_usage", "score", "status", "test_id", "wall_time_usage"]
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
        RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
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
        resource_usage: float
        score: float
        status: Submission.Run.Status
        test_id: str
        wall_time_usage: int
        def __init__(self, id: _Optional[str] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[float] = ..., index: _Optional[int] = ..., test_id: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., status: _Optional[_Union[Submission.Run.Status, str]] = ...) -> None: ...
    COMPLETE: Submission.Status
    COST_FIELD_NUMBER: _ClassVar[int]
    CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR: Submission.Status
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FAILURE: Submission.Status
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    NONE: Submission.Status
    PENDING: Submission.Status
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    TESTING: Submission.Status
    TIMEOUT: Submission.Status
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
    cost: float
    cpu_time_usage: int
    error: str
    groups: _containers.RepeatedCompositeFieldContainer[Submission.Group]
    id: str
    lang: str
    member_id: str
    memory_usage: int
    percentage: float
    problem_id: str
    resource_usage: float
    score: float
    signature: str
    source: str
    status: Submission.Status
    submitted_at: _timestamp_pb2.Timestamp
    user_id: str
    wall_time_usage: int
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., user_id: _Optional[str] = ..., member_id: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lang: _Optional[str] = ..., source: _Optional[str] = ..., signature: _Optional[str] = ..., status: _Optional[_Union[Submission.Status, str]] = ..., error: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., percentage: _Optional[float] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[float] = ..., groups: _Optional[_Iterable[_Union[Submission.Group, _Mapping]]] = ...) -> None: ...
