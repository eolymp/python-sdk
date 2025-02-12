from eolymp.executor import stats_pb2 as _stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerationReport(_message.Message):
    __slots__ = ("task_id", "reference", "origin", "metadata", "agent", "runs", "error_message")
    class Run(_message.Message):
        __slots__ = ("reference", "status", "valid", "input_url", "answer_url", "input_generator_stats", "answer_generator_stats", "error_message")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NONE: _ClassVar[GenerationReport.Run.Status]
            PENDING: _ClassVar[GenerationReport.Run.Status]
            COMPLETE: _ClassVar[GenerationReport.Run.Status]
            FAILED: _ClassVar[GenerationReport.Run.Status]
        NONE: GenerationReport.Run.Status
        PENDING: GenerationReport.Run.Status
        COMPLETE: GenerationReport.Run.Status
        FAILED: GenerationReport.Run.Status
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        VALID_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        INPUT_GENERATOR_STATS_FIELD_NUMBER: _ClassVar[int]
        ANSWER_GENERATOR_STATS_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        reference: str
        status: GenerationReport.Run.Status
        valid: bool
        input_url: str
        answer_url: str
        input_generator_stats: _stats_pb2.Stats
        answer_generator_stats: _stats_pb2.Stats
        error_message: str
        def __init__(self, reference: _Optional[str] = ..., status: _Optional[_Union[GenerationReport.Run.Status, str]] = ..., valid: bool = ..., input_url: _Optional[str] = ..., answer_url: _Optional[str] = ..., input_generator_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., answer_generator_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., error_message: _Optional[str] = ...) -> None: ...
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
    runs: _containers.RepeatedCompositeFieldContainer[GenerationReport.Run]
    error_message: str
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., agent: _Optional[str] = ..., runs: _Optional[_Iterable[_Union[GenerationReport.Run, _Mapping]]] = ..., error_message: _Optional[str] = ...) -> None: ...
