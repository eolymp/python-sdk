from eolymp.atlas import attachment_pb2 as _attachment_pb2
from eolymp.atlas import code_template_pb2 as _code_template_pb2
from eolymp.atlas import editorial_pb2 as _editorial_pb2
from eolymp.atlas import problem_pb2 as _problem_pb2
from eolymp.atlas import solution_pb2 as _solution_pb2
from eolymp.atlas import statement_pb2 as _statement_pb2
from eolymp.atlas import testing_config_pb2 as _testing_config_pb2
from eolymp.atlas import testing_test_pb2 as _testing_test_pb2
from eolymp.atlas import testing_testset_pb2 as _testing_testset_pb2
from eolymp.executor import checker_pb2 as _checker_pb2
from eolymp.executor import interactor_pb2 as _interactor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Snapshot(_message.Message):
    __slots__ = ["attachments", "checker", "editorials", "interactor", "problem", "solutions", "statements", "templates", "testing", "tests", "testsets"]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    CHECKER_FIELD_NUMBER: _ClassVar[int]
    EDITORIALS_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_FIELD_NUMBER: _ClassVar[int]
    SOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    TESTING_FIELD_NUMBER: _ClassVar[int]
    TESTSETS_FIELD_NUMBER: _ClassVar[int]
    TESTS_FIELD_NUMBER: _ClassVar[int]
    attachments: _containers.RepeatedCompositeFieldContainer[_attachment_pb2.Attachment]
    checker: _checker_pb2.Checker
    editorials: _containers.RepeatedCompositeFieldContainer[_editorial_pb2.Editorial]
    interactor: _interactor_pb2.Interactor
    problem: _problem_pb2.Problem
    solutions: _containers.RepeatedCompositeFieldContainer[_solution_pb2.Solution]
    statements: _containers.RepeatedCompositeFieldContainer[_statement_pb2.Statement]
    templates: _containers.RepeatedCompositeFieldContainer[_code_template_pb2.Template]
    testing: _testing_config_pb2.TestingConfig
    tests: _containers.RepeatedCompositeFieldContainer[_testing_test_pb2.Test]
    testsets: _containers.RepeatedCompositeFieldContainer[_testing_testset_pb2.Testset]
    def __init__(self, problem: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ..., testing: _Optional[_Union[_testing_config_pb2.TestingConfig, _Mapping]] = ..., checker: _Optional[_Union[_checker_pb2.Checker, _Mapping]] = ..., interactor: _Optional[_Union[_interactor_pb2.Interactor, _Mapping]] = ..., statements: _Optional[_Iterable[_Union[_statement_pb2.Statement, _Mapping]]] = ..., templates: _Optional[_Iterable[_Union[_code_template_pb2.Template, _Mapping]]] = ..., attachments: _Optional[_Iterable[_Union[_attachment_pb2.Attachment, _Mapping]]] = ..., testsets: _Optional[_Iterable[_Union[_testing_testset_pb2.Testset, _Mapping]]] = ..., tests: _Optional[_Iterable[_Union[_testing_test_pb2.Test, _Mapping]]] = ..., editorials: _Optional[_Iterable[_Union[_editorial_pb2.Editorial, _Mapping]]] = ..., solutions: _Optional[_Iterable[_Union[_solution_pb2.Solution, _Mapping]]] = ...) -> None: ...
