from eolymp.executor import checker_pb2 as _checker_pb2
from eolymp.executor import evaluation_report_pb2 as _evaluation_report_pb2
from eolymp.executor import script_pb2 as _script_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StressTask(_message.Message):
    __slots__ = ("task_id", "reference", "origin", "metadata", "wall_time_limit", "cpu_time_limit", "memory_limit", "interactor_time_limit", "iterations", "deadline", "continue_on_failure", "run_count", "interactive_followup", "checker", "interactor", "validator", "generator", "arguments", "reference_solution", "compared_solutions")
    class Solution(_message.Message):
        __slots__ = ("script", "expected")
        SCRIPT_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_FIELD_NUMBER: _ClassVar[int]
        script: _script_pb2.Script
        expected: _containers.RepeatedScalarFieldContainer[_evaluation_report_pb2.EvaluationReport.Run.Status]
        def __init__(self, script: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., expected: _Optional[_Iterable[_Union[_evaluation_report_pb2.EvaluationReport.Run.Status, str]]] = ...) -> None: ...
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
    INTERACTOR_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ITERATIONS_FIELD_NUMBER: _ClassVar[int]
    DEADLINE_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVE_FOLLOWUP_FIELD_NUMBER: _ClassVar[int]
    CHECKER_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    GENERATOR_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SOLUTION_FIELD_NUMBER: _ClassVar[int]
    COMPARED_SOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    reference: str
    origin: str
    metadata: _containers.ScalarMap[str, str]
    wall_time_limit: int
    cpu_time_limit: int
    memory_limit: int
    interactor_time_limit: int
    iterations: int
    deadline: int
    continue_on_failure: bool
    run_count: int
    interactive_followup: bool
    checker: _checker_pb2.Checker
    interactor: _script_pb2.Script
    validator: _script_pb2.Script
    generator: _script_pb2.Script
    arguments: _containers.RepeatedScalarFieldContainer[str]
    reference_solution: _script_pb2.Script
    compared_solutions: _containers.RepeatedCompositeFieldContainer[StressTask.Solution]
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., wall_time_limit: _Optional[int] = ..., cpu_time_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ..., interactor_time_limit: _Optional[int] = ..., iterations: _Optional[int] = ..., deadline: _Optional[int] = ..., continue_on_failure: _Optional[bool] = ..., run_count: _Optional[int] = ..., interactive_followup: _Optional[bool] = ..., checker: _Optional[_Union[_checker_pb2.Checker, _Mapping]] = ..., interactor: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., validator: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., generator: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., arguments: _Optional[_Iterable[str]] = ..., reference_solution: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., compared_solutions: _Optional[_Iterable[_Union[StressTask.Solution, _Mapping]]] = ...) -> None: ...
