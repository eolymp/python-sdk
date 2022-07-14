from eolymp.annotations import resource_pb2 as _resource_pb2
from eolymp.atlas import attachment_pb2 as _attachment_pb2
from eolymp.atlas import permission_pb2 as _permission_pb2
from eolymp.atlas import problem_pb2 as _problem_pb2
from eolymp.atlas import statement_pb2 as _statement_pb2
from eolymp.atlas import template_pb2 as _template_pb2
from eolymp.atlas import test_pb2 as _test_pb2
from eolymp.atlas import testset_pb2 as _testset_pb2
from eolymp.executor import interactor_pb2 as _interactor_pb2
from eolymp.executor import verifier_pb2 as _verifier_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Change(_message.Message):
    __slots__ = ["create_attachment", "create_problem", "create_statement", "create_template", "create_test", "create_testset", "delete_attachment", "delete_problem", "delete_statement", "delete_template", "delete_test", "delete_testset", "grant_permission", "id", "ip_address", "problem_id", "revoke_permission", "timestamp", "update_attachment", "update_interactor", "update_problem", "update_statement", "update_template", "update_test", "update_testset", "update_verifier", "user_id"]
    class CreateAttachment(_message.Message):
        __slots__ = ["after"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        after: _attachment_pb2.Attachment
        def __init__(self, after: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]] = ...) -> None: ...
    class CreateProblem(_message.Message):
        __slots__ = ["after"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        after: _problem_pb2.Problem
        def __init__(self, after: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ...) -> None: ...
    class CreateStatement(_message.Message):
        __slots__ = ["after"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        after: _statement_pb2.Statement
        def __init__(self, after: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...
    class CreateTemplate(_message.Message):
        __slots__ = ["after"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        after: _template_pb2.Template
        def __init__(self, after: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...
    class CreateTest(_message.Message):
        __slots__ = ["after"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        after: _test_pb2.Test
        def __init__(self, after: _Optional[_Union[_test_pb2.Test, _Mapping]] = ...) -> None: ...
    class CreateTestset(_message.Message):
        __slots__ = ["after"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        after: _testset_pb2.Testset
        def __init__(self, after: _Optional[_Union[_testset_pb2.Testset, _Mapping]] = ...) -> None: ...
    class DeleteAttachment(_message.Message):
        __slots__ = ["before"]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        before: _attachment_pb2.Attachment
        def __init__(self, before: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]] = ...) -> None: ...
    class DeleteProblem(_message.Message):
        __slots__ = ["before"]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        before: _problem_pb2.Problem
        def __init__(self, before: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ...) -> None: ...
    class DeleteStatement(_message.Message):
        __slots__ = ["before"]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        before: _statement_pb2.Statement
        def __init__(self, before: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...
    class DeleteTemplate(_message.Message):
        __slots__ = ["before"]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        before: _template_pb2.Template
        def __init__(self, before: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...
    class DeleteTest(_message.Message):
        __slots__ = ["before"]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        before: _test_pb2.Test
        def __init__(self, before: _Optional[_Union[_test_pb2.Test, _Mapping]] = ...) -> None: ...
    class DeleteTestset(_message.Message):
        __slots__ = ["before"]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        before: _testset_pb2.Testset
        def __init__(self, before: _Optional[_Union[_testset_pb2.Testset, _Mapping]] = ...) -> None: ...
    class GrantPermission(_message.Message):
        __slots__ = ["after"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        after: _permission_pb2.Permission
        def __init__(self, after: _Optional[_Union[_permission_pb2.Permission, _Mapping]] = ...) -> None: ...
    class RevokePermission(_message.Message):
        __slots__ = ["before"]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        before: _permission_pb2.Permission
        def __init__(self, before: _Optional[_Union[_permission_pb2.Permission, _Mapping]] = ...) -> None: ...
    class UpdateAttachment(_message.Message):
        __slots__ = ["after", "before"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        after: _attachment_pb2.Attachment
        before: _attachment_pb2.Attachment
        def __init__(self, before: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]] = ..., after: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]] = ...) -> None: ...
    class UpdateInteractor(_message.Message):
        __slots__ = ["after", "before"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        after: _interactor_pb2.Interactor
        before: _interactor_pb2.Interactor
        def __init__(self, before: _Optional[_Union[_interactor_pb2.Interactor, _Mapping]] = ..., after: _Optional[_Union[_interactor_pb2.Interactor, _Mapping]] = ...) -> None: ...
    class UpdateProblem(_message.Message):
        __slots__ = ["after", "before"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        after: _problem_pb2.Problem
        before: _problem_pb2.Problem
        def __init__(self, before: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ..., after: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ...) -> None: ...
    class UpdateStatement(_message.Message):
        __slots__ = ["after", "before"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        after: _statement_pb2.Statement
        before: _statement_pb2.Statement
        def __init__(self, before: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ..., after: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...
    class UpdateTemplate(_message.Message):
        __slots__ = ["after", "before"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        after: _template_pb2.Template
        before: _template_pb2.Template
        def __init__(self, before: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., after: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...
    class UpdateTest(_message.Message):
        __slots__ = ["after", "before"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        after: _test_pb2.Test
        before: _test_pb2.Test
        def __init__(self, before: _Optional[_Union[_test_pb2.Test, _Mapping]] = ..., after: _Optional[_Union[_test_pb2.Test, _Mapping]] = ...) -> None: ...
    class UpdateTestset(_message.Message):
        __slots__ = ["after", "before"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        after: _testset_pb2.Testset
        before: _testset_pb2.Testset
        def __init__(self, before: _Optional[_Union[_testset_pb2.Testset, _Mapping]] = ..., after: _Optional[_Union[_testset_pb2.Testset, _Mapping]] = ...) -> None: ...
    class UpdateVerifier(_message.Message):
        __slots__ = ["after", "before"]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        after: _verifier_pb2.Verifier
        before: _verifier_pb2.Verifier
        def __init__(self, before: _Optional[_Union[_verifier_pb2.Verifier, _Mapping]] = ..., after: _Optional[_Union[_verifier_pb2.Verifier, _Mapping]] = ...) -> None: ...
    CREATE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    CREATE_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TESTSET_FIELD_NUMBER: _ClassVar[int]
    CREATE_TEST_FIELD_NUMBER: _ClassVar[int]
    DELETE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    DELETE_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    DELETE_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    DELETE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DELETE_TESTSET_FIELD_NUMBER: _ClassVar[int]
    DELETE_TEST_FIELD_NUMBER: _ClassVar[int]
    GRANT_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    REVOKE_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    UPDATE_PROBLEM_FIELD_NUMBER: _ClassVar[int]
    UPDATE_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TESTSET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TEST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    create_attachment: Change.CreateAttachment
    create_problem: Change.CreateProblem
    create_statement: Change.CreateStatement
    create_template: Change.CreateTemplate
    create_test: Change.CreateTest
    create_testset: Change.CreateTestset
    delete_attachment: Change.DeleteAttachment
    delete_problem: Change.DeleteProblem
    delete_statement: Change.DeleteStatement
    delete_template: Change.DeleteTemplate
    delete_test: Change.DeleteTest
    delete_testset: Change.DeleteTestset
    grant_permission: Change.GrantPermission
    id: str
    ip_address: str
    problem_id: str
    revoke_permission: Change.RevokePermission
    timestamp: _timestamp_pb2.Timestamp
    update_attachment: Change.UpdateAttachment
    update_interactor: Change.UpdateInteractor
    update_problem: Change.UpdateProblem
    update_statement: Change.UpdateStatement
    update_template: Change.UpdateTemplate
    update_test: Change.UpdateTest
    update_testset: Change.UpdateTestset
    update_verifier: Change.UpdateVerifier
    user_id: str
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ip_address: _Optional[str] = ..., user_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., create_problem: _Optional[_Union[Change.CreateProblem, _Mapping]] = ..., update_problem: _Optional[_Union[Change.UpdateProblem, _Mapping]] = ..., update_verifier: _Optional[_Union[Change.UpdateVerifier, _Mapping]] = ..., update_interactor: _Optional[_Union[Change.UpdateInteractor, _Mapping]] = ..., delete_problem: _Optional[_Union[Change.DeleteProblem, _Mapping]] = ..., create_statement: _Optional[_Union[Change.CreateStatement, _Mapping]] = ..., update_statement: _Optional[_Union[Change.UpdateStatement, _Mapping]] = ..., delete_statement: _Optional[_Union[Change.DeleteStatement, _Mapping]] = ..., create_testset: _Optional[_Union[Change.CreateTestset, _Mapping]] = ..., update_testset: _Optional[_Union[Change.UpdateTestset, _Mapping]] = ..., delete_testset: _Optional[_Union[Change.DeleteTestset, _Mapping]] = ..., create_test: _Optional[_Union[Change.CreateTest, _Mapping]] = ..., update_test: _Optional[_Union[Change.UpdateTest, _Mapping]] = ..., delete_test: _Optional[_Union[Change.DeleteTest, _Mapping]] = ..., create_template: _Optional[_Union[Change.CreateTemplate, _Mapping]] = ..., update_template: _Optional[_Union[Change.UpdateTemplate, _Mapping]] = ..., delete_template: _Optional[_Union[Change.DeleteTemplate, _Mapping]] = ..., create_attachment: _Optional[_Union[Change.CreateAttachment, _Mapping]] = ..., update_attachment: _Optional[_Union[Change.UpdateAttachment, _Mapping]] = ..., delete_attachment: _Optional[_Union[Change.DeleteAttachment, _Mapping]] = ..., grant_permission: _Optional[_Union[Change.GrantPermission, _Mapping]] = ..., revoke_permission: _Optional[_Union[Change.RevokePermission, _Mapping]] = ...) -> None: ...
