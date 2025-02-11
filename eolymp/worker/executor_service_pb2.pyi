from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteJobInput(_message.Message):
    __slots__ = ("job_id", "namespace", "type", "inputs")
    class InputsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    namespace: str
    type: str
    inputs: _containers.ScalarMap[str, str]
    def __init__(self, job_id: _Optional[str] = ..., namespace: _Optional[str] = ..., type: _Optional[str] = ..., inputs: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ExecuteJobUpdate(_message.Message):
    __slots__ = ("progress", "outputs", "logs")
    class ProgressUpdate(_message.Message):
        __slots__ = ("progress", "total")
        PROGRESS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        progress: int
        total: int
        def __init__(self, progress: _Optional[int] = ..., total: _Optional[int] = ...) -> None: ...
    class OutputUpdate(_message.Message):
        __slots__ = ("outputs",)
        class OutputsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        OUTPUTS_FIELD_NUMBER: _ClassVar[int]
        outputs: _containers.ScalarMap[str, str]
        def __init__(self, outputs: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class LoggingUpdate(_message.Message):
        __slots__ = ("chunk",)
        CHUNK_FIELD_NUMBER: _ClassVar[int]
        chunk: bytes
        def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    progress: ExecuteJobUpdate.ProgressUpdate
    outputs: ExecuteJobUpdate.OutputUpdate
    logs: ExecuteJobUpdate.LoggingUpdate
    def __init__(self, progress: _Optional[_Union[ExecuteJobUpdate.ProgressUpdate, _Mapping]] = ..., outputs: _Optional[_Union[ExecuteJobUpdate.OutputUpdate, _Mapping]] = ..., logs: _Optional[_Union[ExecuteJobUpdate.LoggingUpdate, _Mapping]] = ...) -> None: ...
