from eolymp.executor import checker_pb2 as _checker_pb2
from eolymp.executor import script_pb2 as _script_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvaluationTask(_message.Message):
    __slots__ = ("task_id", "reference", "origin", "metadata", "priority", "redirect_stderr_to_stdout", "time_coefficient_deviation", "run_count", "preconditions", "constraints", "submission", "interactor", "checker", "scripts", "runs")
    class DependencyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_DEPENDENCY_MODE: _ClassVar[EvaluationTask.DependencyMode]
        FULLY_ACCEPTED: _ClassVar[EvaluationTask.DependencyMode]
        FIRST_POINT: _ClassVar[EvaluationTask.DependencyMode]
    UNKNOWN_DEPENDENCY_MODE: EvaluationTask.DependencyMode
    FULLY_ACCEPTED: EvaluationTask.DependencyMode
    FIRST_POINT: EvaluationTask.DependencyMode
    class Generator(_message.Message):
        __slots__ = ("script_name", "arguments")
        SCRIPT_NAME_FIELD_NUMBER: _ClassVar[int]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        script_name: str
        arguments: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, script_name: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ("reference", "index", "debug", "cost", "env", "labels", "input_url", "input_content", "input_generator", "answer_url", "answer_content", "answer_generator")
        class EnvEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        DEBUG_FIELD_NUMBER: _ClassVar[int]
        COST_FIELD_NUMBER: _ClassVar[int]
        ENV_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
        INPUT_GENERATOR_FIELD_NUMBER: _ClassVar[int]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        ANSWER_CONTENT_FIELD_NUMBER: _ClassVar[int]
        ANSWER_GENERATOR_FIELD_NUMBER: _ClassVar[int]
        reference: str
        index: int
        debug: bool
        cost: float
        env: _containers.ScalarMap[str, str]
        labels: _containers.RepeatedScalarFieldContainer[str]
        input_url: str
        input_content: str
        input_generator: EvaluationTask.Generator
        answer_url: str
        answer_content: str
        answer_generator: EvaluationTask.Generator
        def __init__(self, reference: _Optional[str] = ..., index: _Optional[int] = ..., debug: bool = ..., cost: _Optional[float] = ..., env: _Optional[_Mapping[str, str]] = ..., labels: _Optional[_Iterable[str]] = ..., input_url: _Optional[str] = ..., input_content: _Optional[str] = ..., input_generator: _Optional[_Union[EvaluationTask.Generator, _Mapping]] = ..., answer_url: _Optional[str] = ..., answer_content: _Optional[str] = ..., answer_generator: _Optional[_Union[EvaluationTask.Generator, _Mapping]] = ...) -> None: ...
    class Precondition(_message.Message):
        __slots__ = ("selector", "depends_on", "dependency_mode", "stop_on_failure", "max_execution_time")
        SELECTOR_FIELD_NUMBER: _ClassVar[int]
        DEPENDS_ON_FIELD_NUMBER: _ClassVar[int]
        DEPENDENCY_MODE_FIELD_NUMBER: _ClassVar[int]
        STOP_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
        MAX_EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
        selector: _containers.RepeatedScalarFieldContainer[str]
        depends_on: _containers.RepeatedScalarFieldContainer[str]
        dependency_mode: EvaluationTask.DependencyMode
        stop_on_failure: bool
        max_execution_time: int
        def __init__(self, selector: _Optional[_Iterable[str]] = ..., depends_on: _Optional[_Iterable[str]] = ..., dependency_mode: _Optional[_Union[EvaluationTask.DependencyMode, str]] = ..., stop_on_failure: bool = ..., max_execution_time: _Optional[int] = ...) -> None: ...
    class Constraint(_message.Message):
        __slots__ = ("selector", "actor", "wall_time_limit", "cpu_time_limit", "memory_limit", "file_size_limit")
        SELECTOR_FIELD_NUMBER: _ClassVar[int]
        ACTOR_FIELD_NUMBER: _ClassVar[int]
        WALL_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
        CPU_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
        MEMORY_LIMIT_FIELD_NUMBER: _ClassVar[int]
        FILE_SIZE_LIMIT_FIELD_NUMBER: _ClassVar[int]
        selector: _containers.RepeatedScalarFieldContainer[str]
        actor: str
        wall_time_limit: int
        cpu_time_limit: int
        memory_limit: int
        file_size_limit: int
        def __init__(self, selector: _Optional[_Iterable[str]] = ..., actor: _Optional[str] = ..., wall_time_limit: _Optional[int] = ..., cpu_time_limit: _Optional[int] = ..., memory_limit: _Optional[int] = ..., file_size_limit: _Optional[int] = ...) -> None: ...
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
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_STDERR_TO_STDOUT_FIELD_NUMBER: _ClassVar[int]
    TIME_COEFFICIENT_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    CHECKER_FIELD_NUMBER: _ClassVar[int]
    SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    reference: str
    origin: str
    metadata: _containers.ScalarMap[str, str]
    priority: int
    redirect_stderr_to_stdout: bool
    time_coefficient_deviation: float
    run_count: int
    preconditions: _containers.RepeatedCompositeFieldContainer[EvaluationTask.Precondition]
    constraints: _containers.RepeatedCompositeFieldContainer[EvaluationTask.Constraint]
    submission: _script_pb2.Script
    interactor: _script_pb2.Script
    checker: _checker_pb2.Checker
    scripts: _containers.RepeatedCompositeFieldContainer[_script_pb2.Script]
    runs: _containers.RepeatedCompositeFieldContainer[EvaluationTask.Run]
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., priority: _Optional[int] = ..., redirect_stderr_to_stdout: bool = ..., time_coefficient_deviation: _Optional[float] = ..., run_count: _Optional[int] = ..., preconditions: _Optional[_Iterable[_Union[EvaluationTask.Precondition, _Mapping]]] = ..., constraints: _Optional[_Iterable[_Union[EvaluationTask.Constraint, _Mapping]]] = ..., submission: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., interactor: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., checker: _Optional[_Union[_checker_pb2.Checker, _Mapping]] = ..., scripts: _Optional[_Iterable[_Union[_script_pb2.Script, _Mapping]]] = ..., runs: _Optional[_Iterable[_Union[EvaluationTask.Run, _Mapping]]] = ...) -> None: ...
