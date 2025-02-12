from eolymp.atlas import attachment_pb2 as _attachment_pb2
from eolymp.atlas import code_template_pb2 as _code_template_pb2
from eolymp.atlas import editorial_pb2 as _editorial_pb2
from eolymp.atlas import problem_pb2 as _problem_pb2
from eolymp.atlas import script_pb2 as _script_pb2
from eolymp.atlas import solution_pb2 as _solution_pb2
from eolymp.atlas import statement_pb2 as _statement_pb2
from eolymp.atlas import testing_checker_pb2 as _testing_checker_pb2
from eolymp.atlas import testing_config_pb2 as _testing_config_pb2
from eolymp.atlas import testing_interactor_pb2 as _testing_interactor_pb2
from eolymp.atlas import testing_test_pb2 as _testing_test_pb2
from eolymp.atlas import testing_testset_pb2 as _testing_testset_pb2
from eolymp.atlas import testing_validator_pb2 as _testing_validator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Snapshot(_message.Message):
    __slots__ = ("problem", "testing", "checker", "interactor", "validator", "statements", "templates", "attachments", "testsets", "tests", "editorials", "solutions", "scripts")
    PROBLEM_FIELD_NUMBER: _ClassVar[int]
    TESTING_FIELD_NUMBER: _ClassVar[int]
    CHECKER_FIELD_NUMBER: _ClassVar[int]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_FIELD_NUMBER: _ClassVar[int]
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    TESTSETS_FIELD_NUMBER: _ClassVar[int]
    TESTS_FIELD_NUMBER: _ClassVar[int]
    EDITORIALS_FIELD_NUMBER: _ClassVar[int]
    SOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    SCRIPTS_FIELD_NUMBER: _ClassVar[int]
    problem: _problem_pb2.Problem
    testing: _testing_config_pb2.TestingConfig
    checker: _testing_checker_pb2.Checker
    interactor: _testing_interactor_pb2.Interactor
    validator: _testing_validator_pb2.Validator
    statements: _containers.RepeatedCompositeFieldContainer[_statement_pb2.Statement]
    templates: _containers.RepeatedCompositeFieldContainer[_code_template_pb2.Template]
    attachments: _containers.RepeatedCompositeFieldContainer[_attachment_pb2.Attachment]
    testsets: _containers.RepeatedCompositeFieldContainer[_testing_testset_pb2.Testset]
    tests: _containers.RepeatedCompositeFieldContainer[_testing_test_pb2.Test]
    editorials: _containers.RepeatedCompositeFieldContainer[_editorial_pb2.Editorial]
    solutions: _containers.RepeatedCompositeFieldContainer[_solution_pb2.Solution]
    scripts: _containers.RepeatedCompositeFieldContainer[_script_pb2.Script]
    def __init__(self, problem: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ..., testing: _Optional[_Union[_testing_config_pb2.TestingConfig, _Mapping]] = ..., checker: _Optional[_Union[_testing_checker_pb2.Checker, _Mapping]] = ..., interactor: _Optional[_Union[_testing_interactor_pb2.Interactor, _Mapping]] = ..., validator: _Optional[_Union[_testing_validator_pb2.Validator, _Mapping]] = ..., statements: _Optional[_Iterable[_Union[_statement_pb2.Statement, _Mapping]]] = ..., templates: _Optional[_Iterable[_Union[_code_template_pb2.Template, _Mapping]]] = ..., attachments: _Optional[_Iterable[_Union[_attachment_pb2.Attachment, _Mapping]]] = ..., testsets: _Optional[_Iterable[_Union[_testing_testset_pb2.Testset, _Mapping]]] = ..., tests: _Optional[_Iterable[_Union[_testing_test_pb2.Test, _Mapping]]] = ..., editorials: _Optional[_Iterable[_Union[_editorial_pb2.Editorial, _Mapping]]] = ..., solutions: _Optional[_Iterable[_Union[_solution_pb2.Solution, _Mapping]]] = ..., scripts: _Optional[_Iterable[_Union[_script_pb2.Script, _Mapping]]] = ...) -> None: ...
