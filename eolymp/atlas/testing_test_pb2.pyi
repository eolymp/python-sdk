from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Test(_message.Message):
    __slots__ = ["id", "testset_id", "index", "example", "inactive", "secret", "score", "example_input_url", "example_answer_url", "generated_input_url", "generated_answer_url", "input_url", "input_generator", "answer_url", "answer_generator"]
    class Generator(_message.Message):
        __slots__ = ["script_name", "arguments"]
        SCRIPT_NAME_FIELD_NUMBER: _ClassVar[int]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        script_name: str
        arguments: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, script_name: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
    GENERATED_INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    GENERATED_ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
    INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    INPUT_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
    ANSWER_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    testset_id: str
    index: int
    example: bool
    inactive: bool
    secret: bool
    score: float
    example_input_url: str
    example_answer_url: str
    generated_input_url: str
    generated_answer_url: str
    input_url: str
    input_generator: Test.Generator
    answer_url: str
    answer_generator: Test.Generator
    def __init__(self, id: _Optional[str] = ..., testset_id: _Optional[str] = ..., index: _Optional[int] = ..., example: bool = ..., inactive: bool = ..., secret: bool = ..., score: _Optional[float] = ..., example_input_url: _Optional[str] = ..., example_answer_url: _Optional[str] = ..., generated_input_url: _Optional[str] = ..., generated_answer_url: _Optional[str] = ..., input_url: _Optional[str] = ..., input_generator: _Optional[_Union[Test.Generator, _Mapping]] = ..., answer_url: _Optional[str] = ..., answer_generator: _Optional[_Union[Test.Generator, _Mapping]] = ...) -> None: ...
