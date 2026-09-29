from eolymp.executor import stats_pb2 as _stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecutionReport(_message.Message):
    __slots__ = ("task_id", "reference", "origin", "metadata", "agent", "status", "outcome", "error_message", "stats", "interactor_stats", "interaction_url", "trace_url")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[ExecutionReport.Status]
        PENDING: _ClassVar[ExecutionReport.Status]
        PROVISIONING: _ClassVar[ExecutionReport.Status]
        INITIALIZING: _ClassVar[ExecutionReport.Status]
        EXECUTING: _ClassVar[ExecutionReport.Status]
        COMPLETE: _ClassVar[ExecutionReport.Status]
        ERROR: _ClassVar[ExecutionReport.Status]
        FAILED: _ClassVar[ExecutionReport.Status]
    UNKNOWN_STATUS: ExecutionReport.Status
    PENDING: ExecutionReport.Status
    PROVISIONING: ExecutionReport.Status
    INITIALIZING: ExecutionReport.Status
    EXECUTING: ExecutionReport.Status
    COMPLETE: ExecutionReport.Status
    ERROR: ExecutionReport.Status
    FAILED: ExecutionReport.Status
    class Outcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_OUTCOME: _ClassVar[ExecutionReport.Outcome]
        EXECUTED: _ClassVar[ExecutionReport.Outcome]
        RUNTIME_ERROR: _ClassVar[ExecutionReport.Outcome]
        TIMEOUT: _ClassVar[ExecutionReport.Outcome]
        MEMORY_OVERFLOW: _ClassVar[ExecutionReport.Outcome]
        IDLENESS_LIMIT_EXCEEDED: _ClassVar[ExecutionReport.Outcome]
        INTERACTION_FAILURE: _ClassVar[ExecutionReport.Outcome]
    UNKNOWN_OUTCOME: ExecutionReport.Outcome
    EXECUTED: ExecutionReport.Outcome
    RUNTIME_ERROR: ExecutionReport.Outcome
    TIMEOUT: ExecutionReport.Outcome
    MEMORY_OVERFLOW: ExecutionReport.Outcome
    IDLENESS_LIMIT_EXCEEDED: ExecutionReport.Outcome
    INTERACTION_FAILURE: ExecutionReport.Outcome
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
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_STATS_FIELD_NUMBER: _ClassVar[int]
    INTERACTION_URL_FIELD_NUMBER: _ClassVar[int]
    TRACE_URL_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    reference: str
    origin: str
    metadata: _containers.ScalarMap[str, str]
    agent: str
    status: ExecutionReport.Status
    outcome: ExecutionReport.Outcome
    error_message: str
    stats: _stats_pb2.Stats
    interactor_stats: _stats_pb2.Stats
    interaction_url: str
    trace_url: str
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., agent: _Optional[str] = ..., status: _Optional[_Union[ExecutionReport.Status, str]] = ..., outcome: _Optional[_Union[ExecutionReport.Outcome, str]] = ..., error_message: _Optional[str] = ..., stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., interactor_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., interaction_url: _Optional[str] = ..., trace_url: _Optional[str] = ...) -> None: ...
