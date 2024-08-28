from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.executor import evaluation_task_pb2 as _evaluation_task_pb2
from eolymp.executor import generation_task_pb2 as _generation_task_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTaskInput(_message.Message):
    __slots__ = ["evaluation", "generation"]
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    evaluation: _evaluation_task_pb2.EvaluationTask
    generation: _generation_task_pb2.GenerationTask
    def __init__(self, evaluation: _Optional[_Union[_evaluation_task_pb2.EvaluationTask, _Mapping]] = ..., generation: _Optional[_Union[_generation_task_pb2.GenerationTask, _Mapping]] = ...) -> None: ...

class CreateTaskOutput(_message.Message):
    __slots__ = ["task_id"]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...
