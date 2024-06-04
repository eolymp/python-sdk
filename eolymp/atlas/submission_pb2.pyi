from eolymp.atlas import testing_feedback_pb2 as _testing_feedback_pb2
from eolymp.atlas import testing_scoring_pb2 as _testing_scoring_pb2
from eolymp.executor import stats_pb2 as _stats_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Submission(_message.Message):
    __slots__ = ["cost", "cpu_time_usage", "cursor", "error", "error_url", "groups", "id", "lang", "member_id", "memory_usage", "percentage", "problem_id", "resource_usage", "score", "signature", "source", "source_url", "status", "submitted_at", "user_id", "verdict", "wall_time_usage"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Verdict(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class CheckerExecutionData(_message.Message):
        __slots__ = ["exit_code", "log_url", "memory_usage", "wall_time_usage"]
        EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
        LOG_URL_FIELD_NUMBER: _ClassVar[int]
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        exit_code: int
        log_url: str
        memory_usage: int
        wall_time_usage: int
        def __init__(self, log_url: _Optional[str] = ..., wall_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., exit_code: _Optional[int] = ...) -> None: ...
    class Group(_message.Message):
        __slots__ = ["cost", "cpu_time_usage", "dependencies", "feedback_policy", "index", "memory_usage", "resource_usage", "runs", "score", "scoring_mode", "status", "testset_id", "verdict", "wall_time_usage"]
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
        INTERACTION_ERROR: Submission.Group.Status
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
        VERDICT_FIELD_NUMBER: _ClassVar[int]
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
        verdict: Submission.Verdict
        wall_time_usage: int
        def __init__(self, index: _Optional[int] = ..., testset_id: _Optional[str] = ..., status: _Optional[_Union[Submission.Group.Status, str]] = ..., verdict: _Optional[_Union[Submission.Verdict, str]] = ..., dependencies: _Optional[_Iterable[int]] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., scoring_mode: _Optional[_Union[_testing_scoring_pb2.ScoringMode, str]] = ..., feedback_policy: _Optional[_Union[_testing_feedback_pb2.FeedbackPolicy, str]] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[float] = ..., runs: _Optional[_Iterable[_Union[Submission.Run, _Mapping]]] = ...) -> None: ...
    class InteractorExecutionData(_message.Message):
        __slots__ = ["exit_code", "log_url", "memory_usage", "wall_time_usage"]
        EXIT_CODE_FIELD_NUMBER: _ClassVar[int]
        LOG_URL_FIELD_NUMBER: _ClassVar[int]
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        exit_code: int
        log_url: str
        memory_usage: int
        wall_time_usage: int
        def __init__(self, log_url: _Optional[str] = ..., wall_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., exit_code: _Optional[int] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ["checker_execution_data", "checker_stats", "cost", "cpu_time_usage", "id", "index", "interactor_execution_data", "interactor_stats", "memory_usage", "output_url", "resource_usage", "score", "stats", "status", "stderr_url", "test_id", "verdict", "wall_time_usage"]
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ACCEPTED: Submission.Run.Status
        BLOCKED: Submission.Run.Status
        CHECKER_EXECUTION_DATA_FIELD_NUMBER: _ClassVar[int]
        CHECKER_STATS_FIELD_NUMBER: _ClassVar[int]
        COMPLETE: Submission.Run.Status
        COST_FIELD_NUMBER: _ClassVar[int]
        CPU_EXHAUSTED: Submission.Run.Status
        CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        CREATED: Submission.Run.Status
        EXECUTING: Submission.Run.Status
        ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        INTERACTION_ERROR: Submission.Run.Status
        INTERACTOR_EXECUTION_DATA_FIELD_NUMBER: _ClassVar[int]
        INTERACTOR_STATS_FIELD_NUMBER: _ClassVar[int]
        MEMORY_OVERFLOW: Submission.Run.Status
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        NO_STATUS: Submission.Run.Status
        OUTPUT_URL_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_ERROR: Submission.Run.Status
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SKIPPED: Submission.Run.Status
        STATS_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        STDERR_URL_FIELD_NUMBER: _ClassVar[int]
        TEST_ID_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT: Submission.Run.Status
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        VERIFICATION_ERROR: Submission.Run.Status
        WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        WRONG_ANSWER: Submission.Run.Status
        checker_execution_data: Submission.CheckerExecutionData
        checker_stats: _stats_pb2.Stats
        cost: float
        cpu_time_usage: int
        id: str
        index: int
        interactor_execution_data: Submission.InteractorExecutionData
        interactor_stats: _stats_pb2.Stats
        memory_usage: int
        output_url: str
        resource_usage: float
        score: float
        stats: _stats_pb2.Stats
        status: Submission.Run.Status
        stderr_url: str
        test_id: str
        verdict: Submission.Verdict
        wall_time_usage: int
        def __init__(self, id: _Optional[str] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[float] = ..., output_url: _Optional[str] = ..., stderr_url: _Optional[str] = ..., index: _Optional[int] = ..., test_id: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., status: _Optional[_Union[Submission.Run.Status, str]] = ..., verdict: _Optional[_Union[Submission.Verdict, str]] = ..., stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., checker_execution_data: _Optional[_Union[Submission.CheckerExecutionData, _Mapping]] = ..., checker_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., interactor_execution_data: _Optional[_Union[Submission.InteractorExecutionData, _Mapping]] = ..., interactor_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ...) -> None: ...
    ACCEPTED: Submission.Verdict
    COMPLETE: Submission.Status
    COST_FIELD_NUMBER: _ClassVar[int]
    CPU_EXHAUSTED: Submission.Verdict
    CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    ERROR: Submission.Status
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_URL_FIELD_NUMBER: _ClassVar[int]
    FAILURE: Submission.Status
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMORY_OVERFLOW: Submission.Verdict
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    NONE: Submission.Status
    NO_VERDICT: Submission.Verdict
    PENDING: Submission.Status
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_ERROR: Submission.Verdict
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    TESTING: Submission.Status
    TIMEOUT: Submission.Status
    TIME_LIMIT_EXCEEDED: Submission.Verdict
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
    WRONG_ANSWER: Submission.Verdict
    cost: float
    cpu_time_usage: int
    cursor: str
    error: str
    error_url: str
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
    source_url: str
    status: Submission.Status
    submitted_at: _timestamp_pb2.Timestamp
    user_id: str
    verdict: Submission.Verdict
    wall_time_usage: int
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., user_id: _Optional[str] = ..., member_id: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lang: _Optional[str] = ..., source: _Optional[str] = ..., source_url: _Optional[str] = ..., signature: _Optional[str] = ..., status: _Optional[_Union[Submission.Status, str]] = ..., verdict: _Optional[_Union[Submission.Verdict, str]] = ..., error: _Optional[str] = ..., error_url: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., percentage: _Optional[float] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[float] = ..., groups: _Optional[_Iterable[_Union[Submission.Group, _Mapping]]] = ..., cursor: _Optional[str] = ...) -> None: ...
