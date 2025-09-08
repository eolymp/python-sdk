from eolymp.executor import stats_pb2 as _stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StressReport(_message.Message):
    __slots__ = ("task_id", "reference", "origin", "metadata", "agent", "runs", "error_message")
    class Run(_message.Message):
        __slots__ = ("iteration", "status", "input_url", "generator_stats", "solution_stats")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NONE: _ClassVar[StressReport.Run.Status]
            PENDING: _ClassVar[StressReport.Run.Status]
            COMPLETE: _ClassVar[StressReport.Run.Status]
            FAILED: _ClassVar[StressReport.Run.Status]
        NONE: StressReport.Run.Status
        PENDING: StressReport.Run.Status
        COMPLETE: StressReport.Run.Status
        FAILED: StressReport.Run.Status
        ITERATION_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        GENERATOR_STATS_FIELD_NUMBER: _ClassVar[int]
        SOLUTION_STATS_FIELD_NUMBER: _ClassVar[int]
        iteration: int
        status: StressReport.Run.Status
        input_url: str
        generator_stats: _stats_pb2.Stats
        solution_stats: _stats_pb2.Stats
        def __init__(self, iteration: _Optional[int] = ..., status: _Optional[_Union[StressReport.Run.Status, str]] = ..., input_url: _Optional[str] = ..., generator_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., solution_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ...) -> None: ...
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
    RUNS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    reference: str
    origin: str
    metadata: _containers.ScalarMap[str, str]
    agent: str
    runs: _containers.RepeatedCompositeFieldContainer[StressReport.Run]
    error_message: str
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., agent: _Optional[str] = ..., runs: _Optional[_Iterable[_Union[StressReport.Run, _Mapping]]] = ..., error_message: _Optional[str] = ...) -> None: ...
