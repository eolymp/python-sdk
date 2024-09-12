from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Test(_message.Message):
    __slots__ = ["answer_generator", "answer_url", "example", "example_answer_url", "example_input_url", "generated_answer_url", "generated_input_url", "id", "inactive", "index", "input_generator", "input_url", "score", "secret", "testset_id"]
    class Generator(_message.Message):
        __slots__ = ["arguments", "script_name"]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        SCRIPT_NAME_FIELD_NUMBER: _ClassVar[int]
        arguments: _containers.RepeatedScalarFieldContainer[str]
        script_name: str
        def __init__(self, script_name: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ...) -> None: ...
    ANSWER_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    GENERATED_ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
    GENERATED_INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    INPUT_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    answer_generator: Test.Generator
    answer_url: str
    example: bool
    example_answer_url: str
    example_input_url: str
    generated_answer_url: str
    generated_input_url: str
    id: str
    inactive: bool
    index: int
    input_generator: Test.Generator
    input_url: str
    score: float
    secret: bool
    testset_id: str
    def __init__(self, id: _Optional[str] = ..., testset_id: _Optional[str] = ..., index: _Optional[int] = ..., example: bool = ..., inactive: bool = ..., secret: bool = ..., score: _Optional[float] = ..., example_input_url: _Optional[str] = ..., example_answer_url: _Optional[str] = ..., generated_input_url: _Optional[str] = ..., generated_answer_url: _Optional[str] = ..., input_url: _Optional[str] = ..., input_generator: _Optional[_Union[Test.Generator, _Mapping]] = ..., answer_url: _Optional[str] = ..., answer_generator: _Optional[_Union[Test.Generator, _Mapping]] = ...) -> None: ...
