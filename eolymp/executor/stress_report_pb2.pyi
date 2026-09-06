from eolymp.executor import evaluation_report_pb2 as _evaluation_report_pb2
from eolymp.executor import stats_pb2 as _stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StressReport(_message.Message):
    __slots__ = ("task_id", "reference", "origin", "metadata", "agent", "status", "runs", "error_message")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[StressReport.Status]
        PENDING: _ClassVar[StressReport.Status]
        PROVISIONING: _ClassVar[StressReport.Status]
        INITIALIZING: _ClassVar[StressReport.Status]
        EXECUTING: _ClassVar[StressReport.Status]
        COMPLETE: _ClassVar[StressReport.Status]
        ERROR: _ClassVar[StressReport.Status]
        FAILED: _ClassVar[StressReport.Status]
    UNKNOWN_STATUS: StressReport.Status
    PENDING: StressReport.Status
    PROVISIONING: StressReport.Status
    INITIALIZING: StressReport.Status
    EXECUTING: StressReport.Status
    COMPLETE: StressReport.Status
    ERROR: StressReport.Status
    FAILED: StressReport.Status
    class Verdict(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_VERDICT: _ClassVar[StressReport.Verdict]
        PASSED: _ClassVar[StressReport.Verdict]
        COUNTEREXAMPLE: _ClassVar[StressReport.Verdict]
        INVALID: _ClassVar[StressReport.Verdict]
        BROKEN: _ClassVar[StressReport.Verdict]
    UNKNOWN_VERDICT: StressReport.Verdict
    PASSED: StressReport.Verdict
    COUNTEREXAMPLE: StressReport.Verdict
    INVALID: StressReport.Verdict
    BROKEN: StressReport.Verdict
    class Result(_message.Message):
        __slots__ = ("name", "status", "unexpected", "output_url", "stats", "checker_stats")
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        UNEXPECTED_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_URL_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        CHECKER_STATS_FIELD_NUMBER: _ClassVar[int]
        name: str
        status: _evaluation_report_pb2.EvaluationReport.Run.Status
        unexpected: bool
        output_url: str
        stats: _stats_pb2.Stats
        checker_stats: _stats_pb2.Stats
        def __init__(self, name: _Optional[str] = ..., status: _Optional[_Union[_evaluation_report_pb2.EvaluationReport.Run.Status, str]] = ..., unexpected: _Optional[bool] = ..., output_url: _Optional[str] = ..., stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., checker_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ("index", "verdict", "arguments", "input_url", "answer_url", "generator_stats", "validator_stats", "reference_stats", "results")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        GENERATOR_STATS_FIELD_NUMBER: _ClassVar[int]
        VALIDATOR_STATS_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_STATS_FIELD_NUMBER: _ClassVar[int]
        RESULTS_FIELD_NUMBER: _ClassVar[int]
        index: int
        verdict: StressReport.Verdict
        arguments: _containers.RepeatedScalarFieldContainer[str]
        input_url: str
        answer_url: str
        generator_stats: _stats_pb2.Stats
        validator_stats: _stats_pb2.Stats
        reference_stats: _stats_pb2.Stats
        results: _containers.RepeatedCompositeFieldContainer[StressReport.Result]
        def __init__(self, index: _Optional[int] = ..., verdict: _Optional[_Union[StressReport.Verdict, str]] = ..., arguments: _Optional[_Iterable[str]] = ..., input_url: _Optional[str] = ..., answer_url: _Optional[str] = ..., generator_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., validator_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., reference_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., results: _Optional[_Iterable[_Union[StressReport.Result, _Mapping]]] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    reference: str
    origin: str
    metadata: _containers.ScalarMap[str, str]
    agent: str
    status: StressReport.Status
    runs: _containers.RepeatedCompositeFieldContainer[StressReport.Run]
    error_message: str
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., agent: _Optional[str] = ..., status: _Optional[_Union[StressReport.Status, str]] = ..., runs: _Optional[_Iterable[_Union[StressReport.Run, _Mapping]]] = ..., error_message: _Optional[str] = ...) -> None: ...
