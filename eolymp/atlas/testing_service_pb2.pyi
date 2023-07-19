from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import testing_config_pb2 as _testing_config_pb2
from eolymp.atlas import testing_test_pb2 as _testing_test_pb2
from eolymp.atlas import testing_testset_pb2 as _testing_testset_pb2
from eolymp.executor import interactor_pb2 as _interactor_pb2
from eolymp.executor import verifier_pb2 as _verifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTestInput(_message.Message):
    __slots__ = ["problem_id", "test", "testset_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    test: _testing_test_pb2.Test
    testset_id: str
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ..., test: _Optional[_Union[_testing_test_pb2.Test, _Mapping]] = ...) -> None: ...

class CreateTestOutput(_message.Message):
    __slots__ = ["test_id"]
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    test_id: str
    def __init__(self, test_id: _Optional[str] = ...) -> None: ...

class CreateTestsetInput(_message.Message):
    __slots__ = ["problem_id", "testset"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    testset: _testing_testset_pb2.Testset
    def __init__(self, problem_id: _Optional[str] = ..., testset: _Optional[_Union[_testing_testset_pb2.Testset, _Mapping]] = ...) -> None: ...

class CreateTestsetOutput(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteTestInput(_message.Message):
    __slots__ = ["problem_id", "test_id", "testset_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    test_id: str
    testset_id: str
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ..., test_id: _Optional[str] = ...) -> None: ...

class DeleteTestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteTestsetInput(_message.Message):
    __slots__ = ["problem_id", "testset_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    testset_id: str
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ...) -> None: ...

class DeleteTestsetOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeInteractorInput(_message.Message):
    __slots__ = ["problem_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DescribeInteractorOutput(_message.Message):
    __slots__ = ["interactor"]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    interactor: _interactor_pb2.Interactor
    def __init__(self, interactor: _Optional[_Union[_interactor_pb2.Interactor, _Mapping]] = ...) -> None: ...

class DescribeTestInput(_message.Message):
    __slots__ = ["problem_id", "test_id", "testset_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    test_id: str
    testset_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ..., test_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DescribeTestOutput(_message.Message):
    __slots__ = ["test"]
    TEST_FIELD_NUMBER: _ClassVar[int]
    test: _testing_test_pb2.Test
    def __init__(self, test: _Optional[_Union[_testing_test_pb2.Test, _Mapping]] = ...) -> None: ...

class DescribeTestingConfigInput(_message.Message):
    __slots__ = ["problem_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DescribeTestingConfigOutput(_message.Message):
    __slots__ = ["config"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: _testing_config_pb2.TestingConfig
    def __init__(self, config: _Optional[_Union[_testing_config_pb2.TestingConfig, _Mapping]] = ...) -> None: ...

class DescribeTestsetInput(_message.Message):
    __slots__ = ["problem_id", "testset_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    testset_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DescribeTestsetOutput(_message.Message):
    __slots__ = ["testset"]
    TESTSET_FIELD_NUMBER: _ClassVar[int]
    testset: _testing_testset_pb2.Testset
    def __init__(self, testset: _Optional[_Union[_testing_testset_pb2.Testset, _Mapping]] = ...) -> None: ...

class DescribeVerifierInput(_message.Message):
    __slots__ = ["problem_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DescribeVerifierOutput(_message.Message):
    __slots__ = ["verifier"]
    VERIFIER_FIELD_NUMBER: _ClassVar[int]
    verifier: _verifier_pb2.Verifier
    def __init__(self, verifier: _Optional[_Union[_verifier_pb2.Verifier, _Mapping]] = ...) -> None: ...

class ListExamplesInput(_message.Message):
    __slots__ = ["problem_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ListExamplesOutput(_message.Message):
    __slots__ = ["examples"]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    examples: _containers.RepeatedCompositeFieldContainer[_testing_test_pb2.Test]
    def __init__(self, examples: _Optional[_Iterable[_Union[_testing_test_pb2.Test, _Mapping]]] = ...) -> None: ...

class ListTestsInput(_message.Message):
    __slots__ = ["problem_id", "testset_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    testset_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ListTestsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_testing_test_pb2.Test]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_testing_test_pb2.Test, _Mapping]]] = ...) -> None: ...

class ListTestsetsInput(_message.Message):
    __slots__ = ["problem_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ListTestsetsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_testing_testset_pb2.Testset]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_testing_testset_pb2.Testset, _Mapping]]] = ...) -> None: ...

class UpdateInteractorInput(_message.Message):
    __slots__ = ["interactor", "problem_id"]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    interactor: _interactor_pb2.Interactor
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., interactor: _Optional[_Union[_interactor_pb2.Interactor, _Mapping]] = ...) -> None: ...

class UpdateInteractorOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateTestInput(_message.Message):
    __slots__ = ["problem_id", "test", "test_id", "testset_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_FIELD_NUMBER: _ClassVar[int]
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    test: _testing_test_pb2.Test
    test_id: str
    testset_id: str
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ..., test_id: _Optional[str] = ..., test: _Optional[_Union[_testing_test_pb2.Test, _Mapping]] = ...) -> None: ...

class UpdateTestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateTestingConfigInput(_message.Message):
    __slots__ = ["config", "problem_id"]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    config: _testing_config_pb2.TestingConfig
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., config: _Optional[_Union[_testing_config_pb2.TestingConfig, _Mapping]] = ...) -> None: ...

class UpdateTestingConfigOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateTestsetInput(_message.Message):
    __slots__ = ["problem_id", "testset", "testset_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    testset: _testing_testset_pb2.Testset
    testset_id: str
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ..., testset: _Optional[_Union[_testing_testset_pb2.Testset, _Mapping]] = ...) -> None: ...

class UpdateTestsetOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateVerifierInput(_message.Message):
    __slots__ = ["problem_id", "verifier"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERIFIER_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    verifier: _verifier_pb2.Verifier
    def __init__(self, problem_id: _Optional[str] = ..., verifier: _Optional[_Union[_verifier_pb2.Verifier, _Mapping]] = ...) -> None: ...

class UpdateVerifierOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
