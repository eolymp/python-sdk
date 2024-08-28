from eolymp.executor import stats_pb2 as _stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerationReport(_message.Message):
    __slots__ = ["agent", "error", "origin", "reference", "runs", "task_id"]
    class Run(_message.Message):
        __slots__ = ["answer_generator_stats", "answer_url", "input_generator_stats", "input_url", "reference", "status"]
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ANSWER_GENERATOR_STATS_FIELD_NUMBER: _ClassVar[int]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        COMPLETE: GenerationReport.Run.Status
        FAILED: GenerationReport.Run.Status
        INPUT_GENERATOR_STATS_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        NONE: GenerationReport.Run.Status
        PENDING: GenerationReport.Run.Status
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        answer_generator_stats: _stats_pb2.Stats
        answer_url: str
        input_generator_stats: _stats_pb2.Stats
        input_url: str
        reference: str
        status: GenerationReport.Run.Status
        def __init__(self, reference: _Optional[str] = ..., status: _Optional[_Union[GenerationReport.Run.Status, str]] = ..., input_url: _Optional[str] = ..., answer_url: _Optional[str] = ..., input_generator_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., answer_generator_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ...) -> None: ...
    AGENT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    agent: str
    error: str
    origin: str
    reference: str
    runs: _containers.RepeatedCompositeFieldContainer[GenerationReport.Run]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., agent: _Optional[str] = ..., error: _Optional[str] = ..., runs: _Optional[_Iterable[_Union[GenerationReport.Run, _Mapping]]] = ...) -> None: ...
