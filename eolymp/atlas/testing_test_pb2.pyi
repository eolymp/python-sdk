from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Test(_message.Message):
    __slots__ = ("id", "version_id", "testset_id", "index", "status", "status_message", "example", "inactive", "secret", "score", "scripted", "generated_input_url", "generated_answer_url", "input_url", "input_content", "input_generator", "answer_url", "answer_content", "answer_generator", "example_input_url", "example_input_content", "example_answer_url", "example_answer_content")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Test.Status]
        PENDING: _ClassVar[Test.Status]
        READY: _ClassVar[Test.Status]
        INVALID: _ClassVar[Test.Status]
    UNKNOWN_STATUS: Test.Status
    PENDING: Test.Status
    READY: Test.Status
    INVALID: Test.Status
    class Patch(_message.Message):
        __slots__ = ("testset_id", "index", "example", "score", "secret", "input_url", "input_generator", "input_content", "answer_url", "answer_generator", "answer_content", "example_input_url", "example_input_content", "example_answer_url", "example_answer_content", "unset_example_input", "unset_example_answer")
        TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        EXAMPLE_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        SECRET_FIELD_NUMBER: _ClassVar[int]
        INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        INPUT_GENERATOR_FIELD_NUMBER: _ClassVar[int]
        INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
        ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        ANSWER_GENERATOR_FIELD_NUMBER: _ClassVar[int]
        ANSWER_CONTENT_FIELD_NUMBER: _ClassVar[int]
        EXAMPLE_INPUT_URL_FIELD_NUMBER: _ClassVar[int]
        EXAMPLE_INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
        EXAMPLE_ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
        EXAMPLE_ANSWER_CONTENT_FIELD_NUMBER: _ClassVar[int]
        UNSET_EXAMPLE_INPUT_FIELD_NUMBER: _ClassVar[int]
        UNSET_EXAMPLE_ANSWER_FIELD_NUMBER: _ClassVar[int]
        testset_id: str
        index: int
        example: bool
        score: float
        secret: bool
        input_url: str
        input_generator: Test.Generator
        input_content: str
        answer_url: str
        answer_generator: Test.Generator
        answer_content: str
        example_input_url: str
        example_input_content: str
        example_answer_url: str
        example_answer_content: str
        unset_example_input: bool
        unset_example_answer: bool
        def __init__(self, testset_id: _Optional[str] = ..., index: _Optional[int] = ..., example: _Optional[bool] = ..., score: _Optional[float] = ..., secret: _Optional[bool] = ..., input_url: _Optional[str] = ..., input_generator: _Optional[_Union[Test.Generator, _Mapping]] = ..., input_content: _Optional[str] = ..., answer_url: _Optional[str] = ..., answer_generator: _Optional[_Union[Test.Generator, _Mapping]] = ..., answer_content: _Optional[str] = ..., example_input_url: _Optional[str] = ..., example_input_content: _Optional[str] = ..., example_answer_url: _Optional[str] = ..., example_answer_content: _Optional[str] = ..., unset_example_input: _Optional[bool] = ..., unset_example_answer: _Optional[bool] = ...) -> None: ...
    class Generator(_message.Message):
        __slots__ = ("script_name", "arguments")
        SCRIPT_NAME_FIELD_NUMBER: _ClassVar[int]
        ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
        script_name: str
        arguments: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, script_name: _Optional[str] = ..., arguments: _Optional[_Iterable[str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    SCRIPTED_FIELD_NUMBER: _ClassVar[int]
    GENERATED_INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    GENERATED_ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
    INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    INPUT_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
    ANSWER_CONTENT_FIELD_NUMBER: _ClassVar[int]
    ANSWER_GENERATOR_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_INPUT_CONTENT_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_ANSWER_URL_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_ANSWER_CONTENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    version_id: str
    testset_id: str
    index: int
    status: Test.Status
    status_message: str
    example: bool
    inactive: bool
    secret: bool
    score: float
    scripted: bool
    generated_input_url: str
    generated_answer_url: str
    input_url: str
    input_content: str
    input_generator: Test.Generator
    answer_url: str
    answer_content: str
    answer_generator: Test.Generator
    example_input_url: str
    example_input_content: str
    example_answer_url: str
    example_answer_content: str
    def __init__(self, id: _Optional[str] = ..., version_id: _Optional[str] = ..., testset_id: _Optional[str] = ..., index: _Optional[int] = ..., status: _Optional[_Union[Test.Status, str]] = ..., status_message: _Optional[str] = ..., example: _Optional[bool] = ..., inactive: _Optional[bool] = ..., secret: _Optional[bool] = ..., score: _Optional[float] = ..., scripted: _Optional[bool] = ..., generated_input_url: _Optional[str] = ..., generated_answer_url: _Optional[str] = ..., input_url: _Optional[str] = ..., input_content: _Optional[str] = ..., input_generator: _Optional[_Union[Test.Generator, _Mapping]] = ..., answer_url: _Optional[str] = ..., answer_content: _Optional[str] = ..., answer_generator: _Optional[_Union[Test.Generator, _Mapping]] = ..., example_input_url: _Optional[str] = ..., example_input_content: _Optional[str] = ..., example_answer_url: _Optional[str] = ..., example_answer_content: _Optional[str] = ...) -> None: ...
