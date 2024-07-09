from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.executor import deprecated_job_pb2 as _deprecated_job_pb2
from eolymp.executor import task_pb2 as _task_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTaskInput(_message.Message):
    __slots__ = ["job", "task"]
    JOB_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    job: _deprecated_job_pb2.Job
    task: _task_pb2.Task
    def __init__(self, task: _Optional[_Union[_task_pb2.Task, _Mapping]] = ..., job: _Optional[_Union[_deprecated_job_pb2.Job, _Mapping]] = ...) -> None: ...

class CreateTaskOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
