from eolymp.atlas import submission_pb2 as _submission_pb2
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
    __slots__ = ("id", "url", "contest_id", "problem_id", "participant_id", "submitted_at", "deleted", "lang", "source", "source_url", "signature", "status", "verdict", "error", "error_url", "cost", "score", "percentage", "groups")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTRA: _ClassVar[Submission.Extra]
        SOURCE: _ClassVar[Submission.Extra]
        GROUPS: _ClassVar[Submission.Extra]
        RUNS: _ClassVar[Submission.Extra]
    NO_EXTRA: Submission.Extra
    SOURCE: Submission.Extra
    GROUPS: Submission.Extra
    RUNS: Submission.Extra
    class Run(_message.Message):
        __slots__ = ("id", "index", "test_id", "cost", "score", "wall_time_usage", "cpu_time_usage", "memory_usage", "status", "verdict")
        ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        TEST_ID_FIELD_NUMBER: _ClassVar[int]
        COST_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        id: str
        index: int
        test_id: str
        cost: float
        score: float
        wall_time_usage: int
        cpu_time_usage: int
        memory_usage: int
        status: _submission_pb2.Submission.Status
        verdict: _submission_pb2.Submission.Verdict
        def __init__(self, id: _Optional[str] = ..., index: _Optional[int] = ..., test_id: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., status: _Optional[_Union[_submission_pb2.Submission.Status, str]] = ..., verdict: _Optional[_Union[_submission_pb2.Submission.Verdict, str]] = ...) -> None: ...
    class Group(_message.Message):
        __slots__ = ("index", "testset_id", "status", "verdict", "dependencies", "cost", "score", "scoring_mode", "feedback_policy", "wall_time_usage", "cpu_time_usage", "memory_usage", "runs")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
        COST_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SCORING_MODE_FIELD_NUMBER: _ClassVar[int]
        FEEDBACK_POLICY_FIELD_NUMBER: _ClassVar[int]
        WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        RUNS_FIELD_NUMBER: _ClassVar[int]
        index: int
        testset_id: str
        status: _submission_pb2.Submission.Status
        verdict: _submission_pb2.Submission.Verdict
        dependencies: _containers.RepeatedScalarFieldContainer[int]
        cost: float
        score: float
        scoring_mode: _testing_scoring_pb2.ScoringMode
        feedback_policy: _testing_feedback_pb2.FeedbackPolicy
        wall_time_usage: int
        cpu_time_usage: int
        memory_usage: int
        runs: _containers.RepeatedCompositeFieldContainer[Submission.Run]
        def __init__(self, index: _Optional[int] = ..., testset_id: _Optional[str] = ..., status: _Optional[_Union[_submission_pb2.Submission.Status, str]] = ..., verdict: _Optional[_Union[_submission_pb2.Submission.Verdict, str]] = ..., dependencies: _Optional[_Iterable[int]] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., scoring_mode: _Optional[_Union[_testing_scoring_pb2.ScoringMode, str]] = ..., feedback_policy: _Optional[_Union[_testing_feedback_pb2.FeedbackPolicy, str]] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., runs: _Optional[_Iterable[_Union[Submission.Run, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
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
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    contest_id: str
    problem_id: str
    participant_id: str
    submitted_at: _timestamp_pb2.Timestamp
    deleted: bool
    lang: str
    source: str
    source_url: str
    signature: str
    status: _submission_pb2.Submission.Status
    verdict: _submission_pb2.Submission.Verdict
    error: str
    error_url: str
    cost: float
    score: float
    percentage: float
    groups: _containers.RepeatedCompositeFieldContainer[Submission.Group]
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted: bool = ..., lang: _Optional[str] = ..., source: _Optional[str] = ..., source_url: _Optional[str] = ..., signature: _Optional[str] = ..., status: _Optional[_Union[_submission_pb2.Submission.Status, str]] = ..., verdict: _Optional[_Union[_submission_pb2.Submission.Verdict, str]] = ..., error: _Optional[str] = ..., error_url: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., percentage: _Optional[float] = ..., groups: _Optional[_Iterable[_Union[Submission.Group, _Mapping]]] = ...) -> None: ...
