from eolymp.executor import stats_pb2 as _stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvaluationReport(_message.Message):
    __slots__ = ("task_id", "reference", "origin", "metadata", "agent", "signature", "version", "type", "status", "error_message", "runs")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[EvaluationReport.Status]
        PENDING: _ClassVar[EvaluationReport.Status]
        PROVISIONING: _ClassVar[EvaluationReport.Status]
        INITIALIZING: _ClassVar[EvaluationReport.Status]
        EXECUTING: _ClassVar[EvaluationReport.Status]
        COMPLETE: _ClassVar[EvaluationReport.Status]
        ERROR: _ClassVar[EvaluationReport.Status]
        FAILED: _ClassVar[EvaluationReport.Status]
    UNKNOWN_STATUS: EvaluationReport.Status
    PENDING: EvaluationReport.Status
    PROVISIONING: EvaluationReport.Status
    INITIALIZING: EvaluationReport.Status
    EXECUTING: EvaluationReport.Status
    COMPLETE: EvaluationReport.Status
    ERROR: EvaluationReport.Status
    FAILED: EvaluationReport.Status
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TYPE: _ClassVar[EvaluationReport.Type]
        TYPE_UPDATE: _ClassVar[EvaluationReport.Type]
        TYPE_ERROR: _ClassVar[EvaluationReport.Type]
        TYPE_FAILURE: _ClassVar[EvaluationReport.Type]
    UNKNOWN_TYPE: EvaluationReport.Type
    TYPE_UPDATE: EvaluationReport.Type
    TYPE_ERROR: EvaluationReport.Type
    TYPE_FAILURE: EvaluationReport.Type
    class Run(_message.Message):
        __slots__ = ("reference", "status", "score", "cost", "time_usage", "time_limit", "cpu_usage", "cpu_limit", "memory_usage", "memory_limit", "time_coefficient", "input_url", "output_url", "answer_url", "debug_stats", "checker_stats", "interactor_stats")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NONE: _ClassVar[EvaluationReport.Run.Status]
            PENDING: _ClassVar[EvaluationReport.Run.Status]
            EXECUTING: _ClassVar[EvaluationReport.Run.Status]
            TIMEOUT: _ClassVar[EvaluationReport.Run.Status]
            CPU_EXHAUSTED: _ClassVar[EvaluationReport.Run.Status]
            MEMORY_OVERFLOW: _ClassVar[EvaluationReport.Run.Status]
            RUNTIME_ERROR: _ClassVar[EvaluationReport.Run.Status]
            EXECUTED: _ClassVar[EvaluationReport.Run.Status]
            ACCEPTED: _ClassVar[EvaluationReport.Run.Status]
            WRONG_ANSWER: _ClassVar[EvaluationReport.Run.Status]
            VERIFICATION_FAILURE: _ClassVar[EvaluationReport.Run.Status]
            SKIPPED: _ClassVar[EvaluationReport.Run.Status]
            INTERACTION_FAILURE: _ClassVar[EvaluationReport.Run.Status]
            BLOCKED: _ClassVar[EvaluationReport.Run.Status]
        NONE: EvaluationReport.Run.Status
        PENDING: EvaluationReport.Run.Status
        EXECUTING: EvaluationReport.Run.Status
        TIMEOUT: EvaluationReport.Run.Status
        CPU_EXHAUSTED: EvaluationReport.Run.Status
        MEMORY_OVERFLOW: EvaluationReport.Run.Status
        RUNTIME_ERROR: EvaluationReport.Run.Status
        EXECUTED: EvaluationReport.Run.Status
        ACCEPTED: EvaluationReport.Run.Status
        WRONG_ANSWER: EvaluationReport.Run.Status
        VERIFICATION_FAILURE: EvaluationReport.Run.Status
        SKIPPED: EvaluationReport.Run.Status
        INTERACTION_FAILURE: EvaluationReport.Run.Status
        BLOCKED: EvaluationReport.Run.Status
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        COST_FIELD_NUMBER: _ClassVar[int]
        TIME_USAGE_FIELD_NUMBER: _ClassVar[int]
        TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
        CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
        CPU_LIMIT_FIELD_NUMBER: _ClassVar[int]
        MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
        MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
        TIME_COEFFICIENT_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_URL_FIELD_NUMBER: _ClassVar[int]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        DEBUG_STATS_FIELD_NUMBER: _ClassVar[int]
        CHECKER_STATS_FIELD_NUMBER: _ClassVar[int]
        INTERACTOR_STATS_FIELD_NUMBER: _ClassVar[int]
        reference: str
        status: EvaluationReport.Run.Status
        score: float
        cost: float
        time_usage: int
        time_limit: int
        cpu_usage: int
        cpu_limit: int
        memory_usage: int
        memory_limit: int
        time_coefficient: float
        input_url: str
        output_url: str
        answer_url: str
        debug_stats: _stats_pb2.Stats
        checker_stats: _stats_pb2.Stats
        interactor_stats: _stats_pb2.Stats
        def __init__(self, reference: _Optional[str] = ..., status: _Optional[_Union[EvaluationReport.Run.Status, str]] = ..., score: _Optional[float] = ..., cost: _Optional[float] = ..., time_usage: _Optional[int] = ..., time_limit: _Optional[int] = ..., cpu_usage: _Optional[int] = ..., cpu_limit: _Optional[int] = ..., memory_usage: _Optional[int] = ..., memory_limit: _Optional[int] = ..., time_coefficient: _Optional[float] = ..., input_url: _Optional[str] = ..., output_url: _Optional[str] = ..., answer_url: _Optional[str] = ..., debug_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., checker_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., interactor_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ...) -> None: ...
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
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    reference: str
    origin: str
    metadata: _containers.ScalarMap[str, str]
    agent: str
    signature: str
    version: int
    type: EvaluationReport.Type
    status: EvaluationReport.Status
    error_message: str
    runs: _containers.RepeatedCompositeFieldContainer[EvaluationReport.Run]
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., agent: _Optional[str] = ..., signature: _Optional[str] = ..., version: _Optional[int] = ..., type: _Optional[_Union[EvaluationReport.Type, str]] = ..., status: _Optional[_Union[EvaluationReport.Status, str]] = ..., error_message: _Optional[str] = ..., runs: _Optional[_Iterable[_Union[EvaluationReport.Run, _Mapping]]] = ...) -> None: ...
