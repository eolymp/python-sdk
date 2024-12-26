from eolymp.executor import checker_pb2 as _checker_pb2
from eolymp.executor import file_pb2 as _file_pb2
from eolymp.executor import interactor_pb2 as _interactor_pb2
from eolymp.executor import script_pb2 as _script_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvaluationTask(_message.Message):
    __slots__ = ["task_id", "reference", "origin", "priority", "runtime", "source", "source_url", "header_url", "footer_url", "redirect_stderr_to_stdout", "run_count", "preconditions", "constraints", "checker", "interactor", "runs", "files", "scripts"]
    class Generator(_message.Message):
        __slots__ = ["script_name", "arguments"]
        SCRIPT_NAME_FIELD_NUMBER: _ClassVar[int]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        script_name: str
        arguments: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, script_name: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ["reference", "index", "debug", "cost", "env", "labels", "input_url", "input_content", "input_generator", "answer_url", "answer_content", "answer_generator"]
        class EnvEntry(_message.Message):
            __slots__ = ["key", "value"]
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
        __slots__ = ["selector", "depends_on", "stop_on_failure", "max_execution_time"]
        SELECTOR_FIELD_NUMBER: _ClassVar[int]
        DEPENDS_ON_FIELD_NUMBER: _ClassVar[int]
        STOP_ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
        MAX_EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
        selector: _containers.RepeatedScalarFieldContainer[str]
        depends_on: _containers.RepeatedScalarFieldContainer[str]
        stop_on_failure: bool
        max_execution_time: int
        def __init__(self, selector: _Optional[_Iterable[str]] = ..., depends_on: _Optional[_Iterable[str]] = ..., stop_on_failure: bool = ..., max_execution_time: _Optional[int] = ...) -> None: ...
    class Constraint(_message.Message):
        __slots__ = ["selector", "actor", "wall_time_limit", "cpu_time_limit", "memory_limit", "file_size_limit"]
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
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    HEADER_URL_FIELD_NUMBER: _ClassVar[int]
    FOOTER_URL_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_STDERR_TO_STDOUT_FIELD_NUMBER: _ClassVar[int]
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    CHECKER_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    reference: str
    origin: str
    priority: int
    runtime: str
    source: str
    source_url: str
    header_url: str
    footer_url: str
    redirect_stderr_to_stdout: bool
    run_count: int
    preconditions: _containers.RepeatedCompositeFieldContainer[EvaluationTask.Precondition]
    constraints: _containers.RepeatedCompositeFieldContainer[EvaluationTask.Constraint]
    checker: _checker_pb2.Checker
    interactor: _interactor_pb2.Interactor
    runs: _containers.RepeatedCompositeFieldContainer[EvaluationTask.Run]
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    scripts: _containers.RepeatedCompositeFieldContainer[_script_pb2.Script]
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., priority: _Optional[int] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., source_url: _Optional[str] = ..., header_url: _Optional[str] = ..., footer_url: _Optional[str] = ..., redirect_stderr_to_stdout: bool = ..., run_count: _Optional[int] = ..., preconditions: _Optional[_Iterable[_Union[EvaluationTask.Precondition, _Mapping]]] = ..., constraints: _Optional[_Iterable[_Union[EvaluationTask.Constraint, _Mapping]]] = ..., checker: _Optional[_Union[_checker_pb2.Checker, _Mapping]] = ..., interactor: _Optional[_Union[_interactor_pb2.Interactor, _Mapping]] = ..., runs: _Optional[_Iterable[_Union[EvaluationTask.Run, _Mapping]]] = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ..., scripts: _Optional[_Iterable[_Union[_script_pb2.Script, _Mapping]]] = ...) -> None: ...
