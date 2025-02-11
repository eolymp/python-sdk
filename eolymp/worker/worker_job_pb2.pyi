from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Job(_message.Message):
    __slots__ = ("id", "type", "namespace", "status", "progress", "total", "inputs", "outputs", "created_at", "started_at", "progress_at", "complete_at", "logs_url")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Job.Status]
        CREATED: _ClassVar[Job.Status]
        STARTED: _ClassVar[Job.Status]
        COMPLETE: _ClassVar[Job.Status]
        ERROR: _ClassVar[Job.Status]
    UNKNOWN: Job.Status
    CREATED: Job.Status
    STARTED: Job.Status
    COMPLETE: Job.Status
    ERROR: Job.Status
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_PATCH: _ClassVar[Job.Patch]
        PATCH_ALL: _ClassVar[Job.Patch]
        PATCH_PROGRESS: _ClassVar[Job.Patch]
        PATCH_OUTPUTS: _ClassVar[Job.Patch]
        PATCH_LOGS_URL: _ClassVar[Job.Patch]
        PATCH_STATUS: _ClassVar[Job.Patch]
    UNKNOWN_PATCH: Job.Patch
    PATCH_ALL: Job.Patch
    PATCH_PROGRESS: Job.Patch
    PATCH_OUTPUTS: Job.Patch
    PATCH_LOGS_URL: Job.Patch
    PATCH_STATUS: Job.Patch
    class InputsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class OutputsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_AT_FIELD_NUMBER: _ClassVar[int]
    LOGS_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: str
    namespace: str
    status: Job.Status
    progress: int
    total: int
    inputs: _containers.ScalarMap[str, str]
    outputs: _containers.ScalarMap[str, str]
    created_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    progress_at: _timestamp_pb2.Timestamp
    complete_at: _timestamp_pb2.Timestamp
    logs_url: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., namespace: _Optional[str] = ..., status: _Optional[_Union[Job.Status, str]] = ..., progress: _Optional[int] = ..., total: _Optional[int] = ..., inputs: _Optional[_Mapping[str, str]] = ..., outputs: _Optional[_Mapping[str, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., progress_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., logs_url: _Optional[str] = ...) -> None: ...
