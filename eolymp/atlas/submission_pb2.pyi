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
    __slots__ = ("id", "problem_id", "version", "user_id", "member_id", "submitted_at", "judged_at", "lang", "source", "source_url", "signature", "status", "verdict", "error", "error_url", "cost", "score", "percentage", "time_usage", "cpu_usage", "memory_usage", "resource_usage", "groups", "assistant_available", "cursor")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTRA: _ClassVar[Submission.Extra]
        GROUPS: _ClassVar[Submission.Extra]
        RUNS: _ClassVar[Submission.Extra]
    NO_EXTRA: Submission.Extra
    GROUPS: Submission.Extra
    RUNS: Submission.Extra
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Submission.Status]
        PENDING: _ClassVar[Submission.Status]
        PROVISIONING: _ClassVar[Submission.Status]
        INITIALIZING: _ClassVar[Submission.Status]
        TESTING: _ClassVar[Submission.Status]
        TIMEOUT: _ClassVar[Submission.Status]
        COMPLETE: _ClassVar[Submission.Status]
        ERROR: _ClassVar[Submission.Status]
        FAILURE: _ClassVar[Submission.Status]
        SKIPPED: _ClassVar[Submission.Status]
        BLOCKED: _ClassVar[Submission.Status]
    NONE: Submission.Status
    PENDING: Submission.Status
    PROVISIONING: Submission.Status
    INITIALIZING: Submission.Status
    TESTING: Submission.Status
    TIMEOUT: Submission.Status
    COMPLETE: Submission.Status
    ERROR: Submission.Status
    FAILURE: Submission.Status
    SKIPPED: Submission.Status
    BLOCKED: Submission.Status
    class Verdict(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_VERDICT: _ClassVar[Submission.Verdict]
        ACCEPTED: _ClassVar[Submission.Verdict]
        WRONG_ANSWER: _ClassVar[Submission.Verdict]
        TIME_LIMIT_EXCEEDED: _ClassVar[Submission.Verdict]
        CPU_EXHAUSTED: _ClassVar[Submission.Verdict]
        MEMORY_OVERFLOW: _ClassVar[Submission.Verdict]
        RUNTIME_ERROR: _ClassVar[Submission.Verdict]
    NO_VERDICT: Submission.Verdict
    ACCEPTED: Submission.Verdict
    WRONG_ANSWER: Submission.Verdict
    TIME_LIMIT_EXCEEDED: Submission.Verdict
    CPU_EXHAUSTED: Submission.Verdict
    MEMORY_OVERFLOW: Submission.Verdict
    RUNTIME_ERROR: Submission.Verdict
    class Run(_message.Message):
        __slots__ = ("id", "index", "time_usage", "cpu_usage", "memory_usage", "resource_usage", "input_url", "output_url", "answer_url", "cost", "score", "status", "verdict", "debug_stats", "checker_stats", "interactor_stats")
        ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_URL_FIELD_NUMBER: _ClassVar[int]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        COST_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        DEBUG_STATS_FIELD_NUMBER: _ClassVar[int]
        CHECKER_STATS_FIELD_NUMBER: _ClassVar[int]
        INTERACTOR_STATS_FIELD_NUMBER: _ClassVar[int]
        id: str
        index: int
        time_usage: int
        cpu_usage: int
        memory_usage: int
        resource_usage: float
        input_url: str
        output_url: str
        answer_url: str
        cost: float
        score: float
        status: Submission.Status
        verdict: Submission.Verdict
        debug_stats: _stats_pb2.Stats
        checker_stats: _stats_pb2.Stats
        interactor_stats: _stats_pb2.Stats
        def __init__(self, id: _Optional[str] = ..., index: _Optional[int] = ..., time_usage: _Optional[int] = ..., cpu_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[float] = ..., input_url: _Optional[str] = ..., output_url: _Optional[str] = ..., answer_url: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., status: _Optional[_Union[Submission.Status, str]] = ..., verdict: _Optional[_Union[Submission.Verdict, str]] = ..., debug_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., checker_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., interactor_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ...) -> None: ...
    class Group(_message.Message):
        __slots__ = ("index", "status", "verdict", "dependencies", "cost", "score", "scoring_mode", "feedback_policy", "time_usage", "cpu_usage", "memory_usage", "resource_usage", "runs")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
        COST_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SCORING_MODE_FIELD_NUMBER: _ClassVar[int]
        FEEDBACK_POLICY_FIELD_NUMBER: _ClassVar[int]
        TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
        RUNS_FIELD_NUMBER: _ClassVar[int]
        index: int
        status: Submission.Status
        verdict: Submission.Verdict
        dependencies: _containers.RepeatedScalarFieldContainer[int]
        cost: float
        score: float
        scoring_mode: _testing_scoring_pb2.ScoringMode
        feedback_policy: _testing_feedback_pb2.FeedbackPolicy
        time_usage: int
        cpu_usage: int
        memory_usage: int
        resource_usage: float
        runs: _containers.RepeatedCompositeFieldContainer[Submission.Run]
        def __init__(self, index: _Optional[int] = ..., status: _Optional[_Union[Submission.Status, str]] = ..., verdict: _Optional[_Union[Submission.Verdict, str]] = ..., dependencies: _Optional[_Iterable[int]] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., scoring_mode: _Optional[_Union[_testing_scoring_pb2.ScoringMode, str]] = ..., feedback_policy: _Optional[_Union[_testing_feedback_pb2.FeedbackPolicy, str]] = ..., time_usage: _Optional[int] = ..., cpu_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[float] = ..., runs: _Optional[_Iterable[_Union[Submission.Run, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    JUDGED_AT_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_URL_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
    CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_USAGE_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ASSISTANT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    problem_id: str
    version: int
    user_id: str
    member_id: str
    submitted_at: _timestamp_pb2.Timestamp
    judged_at: _timestamp_pb2.Timestamp
    lang: str
    source: str
    source_url: str
    signature: str
    status: Submission.Status
    verdict: Submission.Verdict
    error: str
    error_url: str
    cost: float
    score: float
    percentage: float
    time_usage: int
    cpu_usage: int
    memory_usage: int
    resource_usage: float
    groups: _containers.RepeatedCompositeFieldContainer[Submission.Group]
    assistant_available: bool
    cursor: str
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., version: _Optional[int] = ..., user_id: _Optional[str] = ..., member_id: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., judged_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., lang: _Optional[str] = ..., source: _Optional[str] = ..., source_url: _Optional[str] = ..., signature: _Optional[str] = ..., status: _Optional[_Union[Submission.Status, str]] = ..., verdict: _Optional[_Union[Submission.Verdict, str]] = ..., error: _Optional[str] = ..., error_url: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., percentage: _Optional[float] = ..., time_usage: _Optional[int] = ..., cpu_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., resource_usage: _Optional[float] = ..., groups: _Optional[_Iterable[_Union[Submission.Group, _Mapping]]] = ..., assistant_available: bool = ..., cursor: _Optional[str] = ...) -> None: ...
