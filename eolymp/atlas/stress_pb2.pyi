from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.atlas import submission_pb2 as _submission_pb2
from eolymp.executor import stats_pb2 as _stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Stress(_message.Message):
    __slots__ = ("id", "version", "generator", "arguments", "reference_id", "solution_ids", "iterations", "deadline", "continue_on_failure", "time_limit", "cpu_limit", "memory_limit", "status", "error", "runs")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Stress.Status]
        PENDING: _ClassVar[Stress.Status]
        PROVISIONING: _ClassVar[Stress.Status]
        INITIALIZING: _ClassVar[Stress.Status]
        RUNNING: _ClassVar[Stress.Status]
        COMPLETE: _ClassVar[Stress.Status]
        ERROR: _ClassVar[Stress.Status]
        FAILURE: _ClassVar[Stress.Status]
        CANCELLED: _ClassVar[Stress.Status]
    UNKNOWN_STATUS: Stress.Status
    PENDING: Stress.Status
    PROVISIONING: Stress.Status
    INITIALIZING: Stress.Status
    RUNNING: Stress.Status
    COMPLETE: Stress.Status
    ERROR: Stress.Status
    FAILURE: Stress.Status
    CANCELLED: Stress.Status
    class Verdict(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_VERDICT: _ClassVar[Stress.Verdict]
        PASSED: _ClassVar[Stress.Verdict]
        COUNTEREXAMPLE: _ClassVar[Stress.Verdict]
        INVALID: _ClassVar[Stress.Verdict]
        BROKEN: _ClassVar[Stress.Verdict]
    UNKNOWN_VERDICT: Stress.Verdict
    PASSED: Stress.Verdict
    COUNTEREXAMPLE: Stress.Verdict
    INVALID: Stress.Verdict
    BROKEN: Stress.Verdict
    class Result(_message.Message):
        __slots__ = ("solution_id", "verdict", "unexpected", "output_url", "stats", "checker_stats")
        SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        UNEXPECTED_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_URL_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        CHECKER_STATS_FIELD_NUMBER: _ClassVar[int]
        solution_id: str
        verdict: _submission_pb2.Submission.Verdict
        unexpected: bool
        output_url: str
        stats: _stats_pb2.Stats
        checker_stats: _stats_pb2.Stats
        def __init__(self, solution_id: _Optional[str] = ..., verdict: _Optional[_Union[_submission_pb2.Submission.Verdict, str]] = ..., unexpected: _Optional[bool] = ..., output_url: _Optional[str] = ..., stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., checker_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ...) -> None: ...
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
        verdict: Stress.Verdict
        arguments: _containers.RepeatedScalarFieldContainer[str]
        input_url: str
        answer_url: str
        generator_stats: _stats_pb2.Stats
        validator_stats: _stats_pb2.Stats
        reference_stats: _stats_pb2.Stats
        results: _containers.RepeatedCompositeFieldContainer[Stress.Result]
        def __init__(self, index: _Optional[int] = ..., verdict: _Optional[_Union[Stress.Verdict, str]] = ..., arguments: _Optional[_Iterable[str]] = ..., input_url: _Optional[str] = ..., answer_url: _Optional[str] = ..., generator_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., validator_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., reference_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., results: _Optional[_Iterable[_Union[Stress.Result, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GENERATOR_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_IDS_FIELD_NUMBER: _ClassVar[int]
    ITERATIONS_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: int
    generator: str
    arguments: _containers.RepeatedScalarFieldContainer[str]
    reference_id: str
    solution_ids: _containers.RepeatedScalarFieldContainer[str]
    iterations: int
    deadline: int
    continue_on_failure: bool
    time_limit: int
    cpu_limit: int
    memory_limit: int
    status: Stress.Status
    error: str
    runs: _containers.RepeatedCompositeFieldContainer[Stress.Run]
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., generator: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ..., reference_id: _Optional[str] = ..., solution_ids: _Optional[_Iterable[str]] = ..., iterations: _Optional[int] = ..., deadline: _Optional[int] = ..., continue_on_failure: _Optional[bool] = ..., time_limit: _Optional[int] = ..., cpu_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ..., status: _Optional[_Union[Stress.Status, str]] = ..., error: _Optional[str] = ..., runs: _Optional[_Iterable[_Union[Stress.Run, _Mapping]]] = ...) -> None: ...
