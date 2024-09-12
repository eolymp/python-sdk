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
    __slots__ = ["cost", "cpu_usage", "cursor", "error", "error_url", "groups", "id", "judged_at", "lang", "member_id", "memory_usage", "percentage", "problem_id", "resource_usage", "score", "signature", "source", "source_url", "status", "submitted_at", "time_usage", "user_id", "verdict", "version"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Verdict(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Group(_message.Message):
        __slots__ = ["cost", "cpu_usage", "dependencies", "feedback_policy", "index", "memory_usage", "resource_usage", "runs", "score", "scoring_mode", "status", "time_usage", "verdict"]
        COST_FIELD_NUMBER: _ClassVar[int]
        CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
        DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
        FEEDBACK_POLICY_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
        RUNS_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SCORING_MODE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        cost: float
        cpu_usage: int
        dependencies: _containers.RepeatedScalarFieldContainer[int]
        feedback_policy: _testing_feedback_pb2.FeedbackPolicy
        index: int
        memory_usage: int
        resource_usage: float
        runs: _containers.RepeatedCompositeFieldContainer[Submission.Run]
        score: float
        scoring_mode: _testing_scoring_pb2.ScoringMode
        status: Submission.Status
        time_usage: int
        verdict: Submission.Verdict
        def __init__(self, index: _Optional[int] = ..., status: _Optional[_Union[Submission.Status, str]] = ..., verdict: _Optional[_Union[Submission.Verdict, str]] = ..., dependencies: _Optional[_Iterable[int]] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., scoring_mode: _Optional[_Union[_testing_scoring_pb2.ScoringMode, str]] = ..., feedback_policy: _Optional[_Union[_testing_feedback_pb2.FeedbackPolicy, str]] = ..., time_usage: _Optional[int] = ..., cpu_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[float] = ..., runs: _Optional[_Iterable[_Union[Submission.Run, _Mapping]]] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ["answer_url", "checker_stats", "cost", "cpu_usage", "debug_stats", "id", "index", "input_url", "interactor_stats", "memory_usage", "output_url", "resource_usage", "score", "status", "time_usage", "verdict"]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        CHECKER_STATS_FIELD_NUMBER: _ClassVar[int]
        COST_FIELD_NUMBER: _ClassVar[int]
        CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
        DEBUG_STATS_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        INTERACTOR_STATS_FIELD_NUMBER: _ClassVar[int]
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_URL_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        answer_url: str
        checker_stats: _stats_pb2.Stats
        cost: float
        cpu_usage: int
        debug_stats: _stats_pb2.Stats
        id: str
        index: int
        input_url: str
        interactor_stats: _stats_pb2.Stats
        memory_usage: int
        output_url: str
        resource_usage: float
        score: float
        status: Submission.Status
        time_usage: int
        verdict: Submission.Verdict
        def __init__(self, id: _Optional[str] = ..., index: _Optional[int] = ..., time_usage: _Optional[int] = ..., cpu_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[float] = ..., input_url: _Optional[str] = ..., output_url: _Optional[str] = ..., answer_url: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., status: _Optional[_Union[Submission.Status, str]] = ..., verdict: _Optional[_Union[Submission.Verdict, str]] = ..., debug_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., checker_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., interactor_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ...) -> None: ...
    ACCEPTED: Submission.Verdict
    BLOCKED: Submission.Status
    COMPLETE: Submission.Status
    COST_FIELD_NUMBER: _ClassVar[int]
    CPU_EXHAUSTED: Submission.Verdict
    CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    ERROR: Submission.Status
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_URL_FIELD_NUMBER: _ClassVar[int]
    FAILURE: Submission.Status
    GROUPS: Submission.Extra
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    JUDGED_AT_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMORY_OVERFLOW: Submission.Verdict
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    NONE: Submission.Status
    NO_EXTRA: Submission.Extra
    NO_VERDICT: Submission.Verdict
    PENDING: Submission.Status
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    RUNS: Submission.Extra
    RUNTIME_ERROR: Submission.Verdict
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SKIPPED: Submission.Status
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    TESTING: Submission.Status
    TIMEOUT: Submission.Status
    TIME_LIMIT_EXCEEDED: Submission.Verdict
    TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    WRONG_ANSWER: Submission.Verdict
    cost: float
    cpu_usage: int
    cursor: str
    error: str
    error_url: str
    groups: _containers.RepeatedCompositeFieldContainer[Submission.Group]
    id: str
    judged_at: _timestamp_pb2.Timestamp
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
    time_usage: int
    user_id: str
    verdict: Submission.Verdict
    version: int
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., version: _Optional[int] = ..., user_id: _Optional[str] = ..., member_id: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., judged_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lang: _Optional[str] = ..., source: _Optional[str] = ..., source_url: _Optional[str] = ..., signature: _Optional[str] = ..., status: _Optional[_Union[Submission.Status, str]] = ..., verdict: _Optional[_Union[Submission.Verdict, str]] = ..., error: _Optional[str] = ..., error_url: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., percentage: _Optional[float] = ..., time_usage: _Optional[int] = ..., cpu_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[float] = ..., groups: _Optional[_Iterable[_Union[Submission.Group, _Mapping]]] = ..., cursor: _Optional[str] = ...) -> None: ...
