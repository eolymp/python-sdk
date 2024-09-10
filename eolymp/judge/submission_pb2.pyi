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
    __slots__ = ["contest_id", "cost", "deleted", "error", "error_url", "groups", "id", "lang", "participant_id", "percentage", "problem_id", "score", "signature", "source", "source_url", "status", "submitted_at", "url", "verdict"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Group(_message.Message):
        __slots__ = ["cost", "cpu_time_usage", "dependencies", "feedback_policy", "index", "memory_usage", "runs", "score", "scoring_mode", "status", "testset_id", "verdict", "wall_time_usage"]
        COST_FIELD_NUMBER: _ClassVar[int]
        CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
        FEEDBACK_POLICY_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        RUNS_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SCORING_MODE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        cost: float
        cpu_time_usage: int
        dependencies: _containers.RepeatedScalarFieldContainer[int]
        feedback_policy: _testing_feedback_pb2.FeedbackPolicy
        index: int
        memory_usage: int
        runs: _containers.RepeatedCompositeFieldContainer[Submission.Run]
        score: float
        scoring_mode: _testing_scoring_pb2.ScoringMode
        status: _submission_pb2.Submission.Status
        testset_id: str
        verdict: _submission_pb2.Submission.Verdict
        wall_time_usage: int
        def __init__(self, index: _Optional[int] = ..., testset_id: _Optional[str] = ..., status: _Optional[_Union[_submission_pb2.Submission.Status, str]] = ..., verdict: _Optional[_Union[_submission_pb2.Submission.Verdict, str]] = ..., dependencies: _Optional[_Iterable[int]] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., scoring_mode: _Optional[_Union[_testing_scoring_pb2.ScoringMode, str]] = ..., feedback_policy: _Optional[_Union[_testing_feedback_pb2.FeedbackPolicy, str]] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., runs: _Optional[_Iterable[_Union[Submission.Run, _Mapping]]] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ["cost", "cpu_time_usage", "id", "index", "memory_usage", "score", "status", "test_id", "verdict", "wall_time_usage"]
        COST_FIELD_NUMBER: _ClassVar[int]
        CPU_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TEST_ID_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        WALL_TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        cost: float
        cpu_time_usage: int
        id: str
        index: int
        memory_usage: int
        score: float
        status: _submission_pb2.Submission.Status
        test_id: str
        verdict: _submission_pb2.Submission.Verdict
        wall_time_usage: int
        def __init__(self, id: _Optional[str] = ..., index: _Optional[int] = ..., test_id: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., wall_time_usage: _Optional[int] = ..., cpu_time_usage: _Optional[int] = ..., memory_usage: _Optional[int] = ..., status: _Optional[_Union[_submission_pb2.Submission.Status, str]] = ..., verdict: _Optional[_Union[_submission_pb2.Submission.Verdict, str]] = ...) -> None: ...
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_URL_FIELD_NUMBER: _ClassVar[int]
    GROUPS: Submission.Extra
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    NO_EXTRA: Submission.Extra
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNS: Submission.Extra
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    SOURCE: Submission.Extra
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    cost: float
    deleted: bool
    error: str
    error_url: str
    groups: _containers.RepeatedCompositeFieldContainer[Submission.Group]
    id: str
    lang: str
    participant_id: str
    percentage: float
    problem_id: str
    score: float
    signature: str
    source: str
    source_url: str
    status: _submission_pb2.Submission.Status
    submitted_at: _timestamp_pb2.Timestamp
    url: str
    verdict: _submission_pb2.Submission.Verdict
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., submitted_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted: bool = ..., lang: _Optional[str] = ..., source: _Optional[str] = ..., source_url: _Optional[str] = ..., signature: _Optional[str] = ..., status: _Optional[_Union[_submission_pb2.Submission.Status, str]] = ..., verdict: _Optional[_Union[_submission_pb2.Submission.Verdict, str]] = ..., error: _Optional[str] = ..., error_url: _Optional[str] = ..., cost: _Optional[float] = ..., score: _Optional[float] = ..., percentage: _Optional[float] = ..., groups: _Optional[_Iterable[_Union[Submission.Group, _Mapping]]] = ...) -> None: ...
