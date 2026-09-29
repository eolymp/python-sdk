from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.executor import evaluation_task_pb2 as _evaluation_task_pb2
from eolymp.executor import execution_task_pb2 as _execution_task_pb2
from eolymp.executor import generation_task_pb2 as _generation_task_pb2
from eolymp.executor import stress_task_pb2 as _stress_task_pb2
from eolymp.executor import validation_task_pb2 as _validation_task_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTaskInput(_message.Message):
    __slots__ = ("evaluation", "generation", "stress", "validation", "execution")
    EVALUATION_FIELD_NUMBER: _ClassVar[int]
    GENERATION_FIELD_NUMBER: _ClassVar[int]
    STRESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    evaluation: _evaluation_task_pb2.EvaluationTask
    generation: _generation_task_pb2.GenerationTask
    stress: _stress_task_pb2.StressTask
    validation: _validation_task_pb2.ValidationTask
    execution: _execution_task_pb2.ExecutionTask
    def __init__(self, evaluation: _Optional[_Union[_evaluation_task_pb2.EvaluationTask, _Mapping]] = ..., generation: _Optional[_Union[_generation_task_pb2.GenerationTask, _Mapping]] = ..., stress: _Optional[_Union[_stress_task_pb2.StressTask, _Mapping]] = ..., validation: _Optional[_Union[_validation_task_pb2.ValidationTask, _Mapping]] = ..., execution: _Optional[_Union[_execution_task_pb2.ExecutionTask, _Mapping]] = ...) -> None: ...

class CreateTaskOutput(_message.Message):
    __slots__ = ("task_id",)
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    def __init__(self, task_id: _Optional[str] = ...) -> None: ...
