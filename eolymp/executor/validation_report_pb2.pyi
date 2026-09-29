from eolymp.executor import stats_pb2 as _stats_pb2
from eolymp.executor import warning_pb2 as _warning_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ValidationReport(_message.Message):
    __slots__ = ("task_id", "reference", "origin", "metadata", "agent", "status", "runs", "error_message", "warnings", "warnings_truncated")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[ValidationReport.Status]
        PENDING: _ClassVar[ValidationReport.Status]
        PROVISIONING: _ClassVar[ValidationReport.Status]
        INITIALIZING: _ClassVar[ValidationReport.Status]
        EXECUTING: _ClassVar[ValidationReport.Status]
        COMPLETE: _ClassVar[ValidationReport.Status]
        ERROR: _ClassVar[ValidationReport.Status]
        FAILED: _ClassVar[ValidationReport.Status]
    UNKNOWN_STATUS: ValidationReport.Status
    PENDING: ValidationReport.Status
    PROVISIONING: ValidationReport.Status
    INITIALIZING: ValidationReport.Status
    EXECUTING: ValidationReport.Status
    COMPLETE: ValidationReport.Status
    ERROR: ValidationReport.Status
    FAILED: ValidationReport.Status
    class Run(_message.Message):
        __slots__ = ("reference", "status", "valid", "accepted", "validator_stats", "checker_stats", "error_message")
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        VALID_FIELD_NUMBER: _ClassVar[int]
        ACCEPTED_FIELD_NUMBER: _ClassVar[int]
        VALIDATOR_STATS_FIELD_NUMBER: _ClassVar[int]
        CHECKER_STATS_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        reference: str
        status: ValidationReport.Status
        valid: bool
        accepted: bool
        validator_stats: _stats_pb2.Stats
        checker_stats: _stats_pb2.Stats
        error_message: str
        def __init__(self, reference: _Optional[str] = ..., status: _Optional[_Union[ValidationReport.Status, str]] = ..., valid: _Optional[bool] = ..., accepted: _Optional[bool] = ..., validator_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., checker_stats: _Optional[_Union[_stats_pb2.Stats, _Mapping]] = ..., error_message: _Optional[str] = ...) -> None: ...
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
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    reference: str
    origin: str
    metadata: _containers.ScalarMap[str, str]
    agent: str
    status: ValidationReport.Status
    runs: _containers.RepeatedCompositeFieldContainer[ValidationReport.Run]
    error_message: str
    warnings: _containers.RepeatedCompositeFieldContainer[_warning_pb2.Warning]
    warnings_truncated: bool
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., agent: _Optional[str] = ..., status: _Optional[_Union[ValidationReport.Status, str]] = ..., runs: _Optional[_Iterable[_Union[ValidationReport.Run, _Mapping]]] = ..., error_message: _Optional[str] = ..., warnings: _Optional[_Iterable[_Union[_warning_pb2.Warning, _Mapping]]] = ..., warnings_truncated: _Optional[bool] = ...) -> None: ...
