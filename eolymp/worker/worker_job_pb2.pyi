from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Job(_message.Message):
    __slots__ = ["complete_at", "created_at", "id", "inputs", "logs_url", "namespace", "outputs", "progress", "progress_at", "started_at", "status", "total", "type"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class InputsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class OutputsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    COMPLETE: Job.Status
    COMPLETE_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED: Job.Status
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR: Job.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    LOGS_URL_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    PATCH_ALL: Job.Patch
    PATCH_LOGS_URL: Job.Patch
    PATCH_OUTPUTS: Job.Patch
    PATCH_PROGRESS: Job.Patch
    PATCH_STATUS: Job.Patch
    PROGRESS_AT_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    STARTED: Job.Status
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: Job.Status
    UNKNOWN_PATCH: Job.Patch
    complete_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    id: str
    inputs: _containers.ScalarMap[str, str]
    logs_url: str
    namespace: str
    outputs: _containers.ScalarMap[str, str]
    progress: int
    progress_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    status: Job.Status
    total: int
    type: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[str] = ..., namespace: _Optional[str] = ..., status: _Optional[_Union[Job.Status, str]] = ..., progress: _Optional[int] = ..., total: _Optional[int] = ..., inputs: _Optional[_Mapping[str, str]] = ..., outputs: _Optional[_Mapping[str, str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., progress_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., logs_url: _Optional[str] = ...) -> None: ...
