from eolymp.executor import script_pb2 as _script_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenerationTask(_message.Message):
    __slots__ = ["task_id", "reference", "origin", "runs", "scripts"]
    class Generator(_message.Message):
        __slots__ = ["script_name", "arguments"]
        SCRIPT_NAME_FIELD_NUMBER: _ClassVar[int]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        script_name: str
        arguments: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, script_name: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ...) -> None: ...
    class Run(_message.Message):
        __slots__ = ["reference", "input_url", "input_content", "input_generator", "answer_url", "answer_content", "answer_generator"]
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
        INPUT_GENERATOR_FIELD_NUMBER: _ClassVar[int]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        ANSWER_CONTENT_FIELD_NUMBER: _ClassVar[int]
        ANSWER_GENERATOR_FIELD_NUMBER: _ClassVar[int]
        reference: str
        input_url: str
        input_content: str
        input_generator: GenerationTask.Generator
        answer_url: str
        answer_content: str
        answer_generator: GenerationTask.Generator
        def __init__(self, reference: _Optional[str] = ..., input_url: _Optional[str] = ..., input_content: _Optional[str] = ..., input_generator: _Optional[_Union[GenerationTask.Generator, _Mapping]] = ..., answer_url: _Optional[str] = ..., answer_content: _Optional[str] = ..., answer_generator: _Optional[_Union[GenerationTask.Generator, _Mapping]] = ...) -> None: ...
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    task_id: str
    reference: str
    origin: str
    runs: _containers.RepeatedCompositeFieldContainer[GenerationTask.Run]
    scripts: _containers.RepeatedCompositeFieldContainer[_script_pb2.Script]
    def __init__(self, task_id: _Optional[str] = ..., reference: _Optional[str] = ..., origin: _Optional[str] = ..., runs: _Optional[_Iterable[_Union[GenerationTask.Run, _Mapping]]] = ..., scripts: _Optional[_Iterable[_Union[_script_pb2.Script, _Mapping]]] = ...) -> None: ...
