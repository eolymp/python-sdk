from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExecuteTaskInput(_message.Message):
    __slots__ = ("task_id", "task", "checkpoint", "attempt")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    task: _any_pb2.Any
    checkpoint: _any_pb2.Any
    attempt: int
    def __init__(self, task_id: _Optional[str] = ..., task: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., checkpoint: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., attempt: _Optional[int] = ...) -> None: ...

class ExecuteTaskOutput(_message.Message):
    __slots__ = ("progress", "checkpoint", "record")
    class Progress(_message.Message):
        __slots__ = ("progress", "total", "status_message")
        PROGRESS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_FIELD_NUMBER: _ClassVar[int]
        STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        progress: int
        total: int
        status_message: str
        def __init__(self, progress: _Optional[int] = ..., total: _Optional[int] = ..., status_message: _Optional[str] = ...) -> None: ...
    class Checkpoint(_message.Message):
        __slots__ = ("checkpoint",)
        CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
        checkpoint: _any_pb2.Any
        def __init__(self, checkpoint: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    class Record(_message.Message):
        __slots__ = ("line",)
        LINE_FIELD_NUMBER: _ClassVar[int]
        line: str
        def __init__(self, line: _Optional[str] = ...) -> None: ...
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    progress: ExecuteTaskOutput.Progress
    checkpoint: ExecuteTaskOutput.Checkpoint
    record: ExecuteTaskOutput.Record
    def __init__(self, progress: _Optional[_Union[ExecuteTaskOutput.Progress, _Mapping]] = ..., checkpoint: _Optional[_Union[ExecuteTaskOutput.Checkpoint, _Mapping]] = ..., record: _Optional[_Union[ExecuteTaskOutput.Record, _Mapping]] = ...) -> None: ...
