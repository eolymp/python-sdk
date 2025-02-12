from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import testing_checker_pb2 as _testing_checker_pb2
from eolymp.atlas import testing_config_pb2 as _testing_config_pb2
from eolymp.atlas import testing_interactor_pb2 as _testing_interactor_pb2
from eolymp.atlas import testing_test_pb2 as _testing_test_pb2
from eolymp.atlas import testing_testset_pb2 as _testing_testset_pb2
from eolymp.atlas import testing_validator_pb2 as _testing_validator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestingConfigChangedEvent(_message.Message):
    __slots__ = ("problem_id", "before", "after")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    before: _testing_config_pb2.TestingConfig
    after: _testing_config_pb2.TestingConfig
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Union[_testing_config_pb2.TestingConfig, _Mapping]] = ..., after: _Optional[_Union[_testing_config_pb2.TestingConfig, _Mapping]] = ...) -> None: ...

class InteractorChangedEvent(_message.Message):
    __slots__ = ("problem_id", "before", "after")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    before: _testing_interactor_pb2.Interactor
    after: _testing_interactor_pb2.Interactor
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Union[_testing_interactor_pb2.Interactor, _Mapping]] = ..., after: _Optional[_Union[_testing_interactor_pb2.Interactor, _Mapping]] = ...) -> None: ...

class CheckerChangedEvent(_message.Message):
    __slots__ = ("problem_id", "before", "after")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    before: _testing_checker_pb2.Checker
    after: _testing_checker_pb2.Checker
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Union[_testing_checker_pb2.Checker, _Mapping]] = ..., after: _Optional[_Union[_testing_checker_pb2.Checker, _Mapping]] = ...) -> None: ...

class ValidatorChangedEvent(_message.Message):
    __slots__ = ("problem_id", "before", "after")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    before: _testing_validator_pb2.Validator
    after: _testing_validator_pb2.Validator
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Union[_testing_validator_pb2.Validator, _Mapping]] = ..., after: _Optional[_Union[_testing_validator_pb2.Validator, _Mapping]] = ...) -> None: ...

class TestsetChangedEvent(_message.Message):
    __slots__ = ("problem_id", "before", "after")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    before: _testing_testset_pb2.Testset
    after: _testing_testset_pb2.Testset
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Union[_testing_testset_pb2.Testset, _Mapping]] = ..., after: _Optional[_Union[_testing_testset_pb2.Testset, _Mapping]] = ...) -> None: ...

class TestChangedEvent(_message.Message):
    __slots__ = ("problem_id", "before", "after")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    before: _testing_test_pb2.Test
    after: _testing_test_pb2.Test
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Union[_testing_test_pb2.Test, _Mapping]] = ..., after: _Optional[_Union[_testing_test_pb2.Test, _Mapping]] = ...) -> None: ...

class TestBatchChangedEvent(_message.Message):
    __slots__ = ("problem_id", "before", "after")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    before: _containers.RepeatedCompositeFieldContainer[_testing_test_pb2.Test]
    after: _containers.RepeatedCompositeFieldContainer[_testing_test_pb2.Test]
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Iterable[_Union[_testing_test_pb2.Test, _Mapping]]] = ..., after: _Optional[_Iterable[_Union[_testing_test_pb2.Test, _Mapping]]] = ...) -> None: ...

class UpdateTestingConfigInput(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _testing_config_pb2.TestingConfig
    def __init__(self, config: _Optional[_Union[_testing_config_pb2.TestingConfig, _Mapping]] = ...) -> None: ...

class UpdateTestingConfigOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeTestingConfigInput(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class DescribeTestingConfigOutput(_message.Message):
    __slots__ = ("config",)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _testing_config_pb2.TestingConfig
    def __init__(self, config: _Optional[_Union[_testing_config_pb2.TestingConfig, _Mapping]] = ...) -> None: ...

class UpdateCheckerInput(_message.Message):
    __slots__ = ("checker",)
    CHECKER_FIELD_NUMBER: _ClassVar[int]
    checker: _testing_checker_pb2.Checker
    def __init__(self, checker: _Optional[_Union[_testing_checker_pb2.Checker, _Mapping]] = ...) -> None: ...

class UpdateCheckerOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeCheckerInput(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class DescribeCheckerOutput(_message.Message):
    __slots__ = ("checker",)
    CHECKER_FIELD_NUMBER: _ClassVar[int]
    checker: _testing_checker_pb2.Checker
    def __init__(self, checker: _Optional[_Union[_testing_checker_pb2.Checker, _Mapping]] = ...) -> None: ...

class UpdateInteractorInput(_message.Message):
    __slots__ = ("interactor",)
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    interactor: _testing_interactor_pb2.Interactor
    def __init__(self, interactor: _Optional[_Union[_testing_interactor_pb2.Interactor, _Mapping]] = ...) -> None: ...

class UpdateInteractorOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeInteractorInput(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class DescribeInteractorOutput(_message.Message):
    __slots__ = ("interactor",)
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    interactor: _testing_interactor_pb2.Interactor
    def __init__(self, interactor: _Optional[_Union[_testing_interactor_pb2.Interactor, _Mapping]] = ...) -> None: ...

class UpdateValidatorInput(_message.Message):
    __slots__ = ("validator",)
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    validator: _testing_validator_pb2.Validator
    def __init__(self, validator: _Optional[_Union[_testing_validator_pb2.Validator, _Mapping]] = ...) -> None: ...

class UpdateValidatorOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeValidatorInput(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class DescribeValidatorOutput(_message.Message):
    __slots__ = ("validator",)
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    validator: _testing_validator_pb2.Validator
    def __init__(self, validator: _Optional[_Union[_testing_validator_pb2.Validator, _Mapping]] = ...) -> None: ...

class ListTestsetsInput(_message.Message):
    __slots__ = ("offset", "size", "version")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    version: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...

class ListTestsetsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_testing_testset_pb2.Testset]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_testing_testset_pb2.Testset, _Mapping]]] = ...) -> None: ...

class DescribeTestsetInput(_message.Message):
    __slots__ = ("testset_id", "version")
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    testset_id: str
    version: int
    def __init__(self, testset_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DescribeTestsetOutput(_message.Message):
    __slots__ = ("testset",)
    TESTSET_FIELD_NUMBER: _ClassVar[int]
    testset: _testing_testset_pb2.Testset
    def __init__(self, testset: _Optional[_Union[_testing_testset_pb2.Testset, _Mapping]] = ...) -> None: ...

class CreateTestsetInput(_message.Message):
    __slots__ = ("testset",)
    TESTSET_FIELD_NUMBER: _ClassVar[int]
    testset: _testing_testset_pb2.Testset
    def __init__(self, testset: _Optional[_Union[_testing_testset_pb2.Testset, _Mapping]] = ...) -> None: ...

class CreateTestsetOutput(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class UpdateTestsetInput(_message.Message):
    __slots__ = ("testset_id", "testset")
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_FIELD_NUMBER: _ClassVar[int]
    testset_id: str
    testset: _testing_testset_pb2.Testset
    def __init__(self, testset_id: _Optional[str] = ..., testset: _Optional[_Union[_testing_testset_pb2.Testset, _Mapping]] = ...) -> None: ...

class UpdateTestsetOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteTestsetInput(_message.Message):
    __slots__ = ("testset_id",)
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    testset_id: str
    def __init__(self, testset_id: _Optional[str] = ...) -> None: ...

class DeleteTestsetOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListExamplesInput(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class ListExamplesOutput(_message.Message):
    __slots__ = ("examples",)
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    examples: _containers.RepeatedCompositeFieldContainer[_testing_test_pb2.Test]
    def __init__(self, examples: _Optional[_Iterable[_Union[_testing_test_pb2.Test, _Mapping]]] = ...) -> None: ...

class ListTestsInput(_message.Message):
    __slots__ = ("testset_id", "version")
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    testset_id: str
    version: int
    def __init__(self, testset_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ListTestsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_testing_test_pb2.Test]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_testing_test_pb2.Test, _Mapping]]] = ...) -> None: ...

class DescribeTestInput(_message.Message):
    __slots__ = ("testset_id", "test_id", "version")
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    testset_id: str
    test_id: str
    version: int
    def __init__(self, testset_id: _Optional[str] = ..., test_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DescribeTestOutput(_message.Message):
    __slots__ = ("test",)
    TEST_FIELD_NUMBER: _ClassVar[int]
    test: _testing_test_pb2.Test
    def __init__(self, test: _Optional[_Union[_testing_test_pb2.Test, _Mapping]] = ...) -> None: ...

class CreateTestInput(_message.Message):
    __slots__ = ("testset_id", "test")
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_FIELD_NUMBER: _ClassVar[int]
    testset_id: str
    test: _testing_test_pb2.Test
    def __init__(self, testset_id: _Optional[str] = ..., test: _Optional[_Union[_testing_test_pb2.Test, _Mapping]] = ...) -> None: ...

class CreateTestOutput(_message.Message):
    __slots__ = ("test_id",)
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    test_id: str
    def __init__(self, test_id: _Optional[str] = ...) -> None: ...

class UpdateTestInput(_message.Message):
    __slots__ = ("patch", "testset_id", "test_id", "test")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateTestInput.Patch]
        EXAMPLE: _ClassVar[UpdateTestInput.Patch]
        INACTIVE: _ClassVar[UpdateTestInput.Patch]
        SCORE: _ClassVar[UpdateTestInput.Patch]
        INPUT: _ClassVar[UpdateTestInput.Patch]
        ANSWER: _ClassVar[UpdateTestInput.Patch]
        INDEX: _ClassVar[UpdateTestInput.Patch]
        SECRET: _ClassVar[UpdateTestInput.Patch]
        EXAMPLE_INPUT: _ClassVar[UpdateTestInput.Patch]
        EXAMPLE_ANSWER: _ClassVar[UpdateTestInput.Patch]
    ALL: UpdateTestInput.Patch
    EXAMPLE: UpdateTestInput.Patch
    INACTIVE: UpdateTestInput.Patch
    SCORE: UpdateTestInput.Patch
    INPUT: UpdateTestInput.Patch
    ANSWER: UpdateTestInput.Patch
    INDEX: UpdateTestInput.Patch
    SECRET: UpdateTestInput.Patch
    EXAMPLE_INPUT: UpdateTestInput.Patch
    EXAMPLE_ANSWER: UpdateTestInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateTestInput.Patch]
    testset_id: str
    test_id: str
    test: _testing_test_pb2.Test
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateTestInput.Patch, str]]] = ..., testset_id: _Optional[str] = ..., test_id: _Optional[str] = ..., test: _Optional[_Union[_testing_test_pb2.Test, _Mapping]] = ...) -> None: ...

class UpdateTestOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteTestInput(_message.Message):
    __slots__ = ("testset_id", "test_id")
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    testset_id: str
    test_id: str
    def __init__(self, testset_id: _Optional[str] = ..., test_id: _Optional[str] = ...) -> None: ...

class DeleteTestOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
