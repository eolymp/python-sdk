from eolymp.executor import script_pb2 as _script_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StressTask(_message.Message):
    __slots__ = ("task_id", "reference", "origin", "metadata", "wall_time_limit", "cpu_time_limit", "memory_limit", "iteration_count", "run_count", "interactive_followup", "interactor", "validator", "generator", "solution")
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
    WALL_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CPU_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ITERATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVE_FOLLOWUP_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    GENERATOR_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    reference: str
    origin: str
    metadata: _containers.ScalarMap[str, str]
    wall_time_limit: int
    cpu_time_limit: int
    memory_limit: int
    iteration_count: int
    run_count: int
    interactive_followup: bool
    interactor: _script_pb2.Script
    validator: _script_pb2.Script
    generator: _script_pb2.Script
    solution: _script_pb2.Script
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., wall_time_limit: _Optional[int] = ..., cpu_time_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ..., iteration_count: _Optional[int] = ..., run_count: _Optional[int] = ..., interactive_followup: bool = ..., interactor: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., validator: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., generator: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., solution: _Optional[_Union[_script_pb2.Script, _Mapping]] = ...) -> None: ...
