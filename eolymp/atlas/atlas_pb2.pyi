from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.annotations import service_pb2 as _service_pb2
from eolymp.atlas import attachment_pb2 as _attachment_pb2
from eolymp.atlas import category_pb2 as _category_pb2
from eolymp.atlas import change_pb2 as _change_pb2
from eolymp.atlas import permission_pb2 as _permission_pb2
from eolymp.atlas import problem_pb2 as _problem_pb2
from eolymp.atlas import score_pb2 as _score_pb2
from eolymp.atlas import solution_pb2 as _solution_pb2
from eolymp.atlas import statement_pb2 as _statement_pb2
from eolymp.atlas import submission_pb2 as _submission_pb2
from eolymp.atlas import template_pb2 as _template_pb2
from eolymp.atlas import test_pb2 as _test_pb2
from eolymp.atlas import testset_pb2 as _testset_pb2
from eolymp.executor import interactor_pb2 as _interactor_pb2
from eolymp.executor import verifier_pb2 as _verifier_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApproveSolutionInput(_message.Message):
    __slots__ = ["problem_id", "solution_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    solution_id: str
    def __init__(self, problem_id: _Optional[str] = ..., solution_id: _Optional[str] = ...) -> None: ...

class ApproveSolutionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AssignCategoryInput(_message.Message):
    __slots__ = ["category_id", "index", "problem_id"]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    category_id: str
    index: int
    problem_id: str
    def __init__(self, category_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...

class AssignCategoryOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateAttachmentInput(_message.Message):
    __slots__ = ["attachment", "problem_id"]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    attachment: _attachment_pb2.Attachment
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., attachment: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]] = ...) -> None: ...

class CreateAttachmentOutput(_message.Message):
    __slots__ = ["attachment_id"]
    ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    attachment_id: str
    def __init__(self, attachment_id: _Optional[str] = ...) -> None: ...

class CreateCategoryInput(_message.Message):
    __slots__ = ["category"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: _category_pb2.Category
    def __init__(self, category: _Optional[_Union[_category_pb2.Category, _Mapping]] = ...) -> None: ...

class CreateCategoryOutput(_message.Message):
    __slots__ = ["category_id"]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    category_id: str
    def __init__(self, category_id: _Optional[str] = ...) -> None: ...

class CreateCodeTemplateInput(_message.Message):
    __slots__ = ["problem_id", "template"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    template: _template_pb2.Template
    def __init__(self, problem_id: _Optional[str] = ..., template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...

class CreateCodeTemplateOutput(_message.Message):
    __slots__ = ["template_id"]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class CreateProblemInput(_message.Message):
    __slots__ = ["problem", "statement"]
    PROBLEM_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    problem: _problem_pb2.Problem
    statement: _statement_pb2.Statement
    def __init__(self, problem: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ..., statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class CreateProblemOutput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class CreateSolutionInput(_message.Message):
    __slots__ = ["problem_id", "solution"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    solution: _solution_pb2.Solution
    def __init__(self, problem_id: _Optional[str] = ..., solution: _Optional[_Union[_solution_pb2.Solution, _Mapping]] = ...) -> None: ...

class CreateSolutionOutput(_message.Message):
    __slots__ = ["solution_id"]
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    solution_id: str
    def __init__(self, solution_id: _Optional[str] = ...) -> None: ...

class CreateStatementInput(_message.Message):
    __slots__ = ["problem_id", "statement"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    statement: _statement_pb2.Statement
    def __init__(self, problem_id: _Optional[str] = ..., statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class CreateStatementOutput(_message.Message):
    __slots__ = ["statement_id"]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    statement_id: str
    def __init__(self, statement_id: _Optional[str] = ...) -> None: ...

class CreateSubmissionInput(_message.Message):
    __slots__ = ["lang", "problem_id", "source"]
    LANG_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    lang: str
    problem_id: str
    source: str
    def __init__(self, problem_id: _Optional[str] = ..., lang: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class CreateSubmissionOutput(_message.Message):
    __slots__ = ["submission_id"]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    def __init__(self, submission_id: _Optional[str] = ...) -> None: ...

class CreateTestInput(_message.Message):
    __slots__ = ["problem_id", "test", "testset_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    test: _test_pb2.Test
    testset_id: str
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ..., test: _Optional[_Union[_test_pb2.Test, _Mapping]] = ...) -> None: ...

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
    testset: _testset_pb2.Testset
    def __init__(self, problem_id: _Optional[str] = ..., testset: _Optional[_Union[_testset_pb2.Testset, _Mapping]] = ...) -> None: ...

class CreateTestsetOutput(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteAttachmentInput(_message.Message):
    __slots__ = ["attachment_id", "problem_id"]
    ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    attachment_id: str
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., attachment_id: _Optional[str] = ...) -> None: ...

class DeleteAttachmentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteCategoryInput(_message.Message):
    __slots__ = ["category_id"]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    category_id: str
    def __init__(self, category_id: _Optional[str] = ...) -> None: ...

class DeleteCategoryOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteCodeTemplateInput(_message.Message):
    __slots__ = ["problem_id", "template_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    template_id: str
    def __init__(self, problem_id: _Optional[str] = ..., template_id: _Optional[str] = ...) -> None: ...

class DeleteCodeTemplateOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteProblemInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class DeleteProblemOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteSolutionInput(_message.Message):
    __slots__ = ["problem_id", "solution_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    solution_id: str
    def __init__(self, problem_id: _Optional[str] = ..., solution_id: _Optional[str] = ...) -> None: ...

class DeleteSolutionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteStatementInput(_message.Message):
    __slots__ = ["problem_id", "statement_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    statement_id: str
    def __init__(self, problem_id: _Optional[str] = ..., statement_id: _Optional[str] = ...) -> None: ...

class DeleteStatementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

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

class DescribeAttachmentInput(_message.Message):
    __slots__ = ["attachment_id", "problem_id"]
    ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    attachment_id: str
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., attachment_id: _Optional[str] = ...) -> None: ...

class DescribeAttachmentOutput(_message.Message):
    __slots__ = ["attachment"]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    attachment: _attachment_pb2.Attachment
    def __init__(self, attachment: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]] = ...) -> None: ...

class DescribeCategoryInput(_message.Message):
    __slots__ = ["category_id"]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    category_id: str
    def __init__(self, category_id: _Optional[str] = ...) -> None: ...

class DescribeCategoryOutput(_message.Message):
    __slots__ = ["category"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    category: _category_pb2.Category
    def __init__(self, category: _Optional[_Union[_category_pb2.Category, _Mapping]] = ...) -> None: ...

class DescribeChangeInput(_message.Message):
    __slots__ = ["change_id", "problem_id"]
    CHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    change_id: str
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., change_id: _Optional[str] = ...) -> None: ...

class DescribeChangeOutput(_message.Message):
    __slots__ = ["change"]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    change: _change_pb2.Change
    def __init__(self, change: _Optional[_Union[_change_pb2.Change, _Mapping]] = ...) -> None: ...

class DescribeCodeTemplateInput(_message.Message):
    __slots__ = ["problem_id", "template_ern", "template_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ERN_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    template_ern: str
    template_id: str
    def __init__(self, problem_id: _Optional[str] = ..., template_id: _Optional[str] = ..., template_ern: _Optional[str] = ...) -> None: ...

class DescribeCodeTemplateOutput(_message.Message):
    __slots__ = ["template"]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...

class DescribeInteractorInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class DescribeInteractorOutput(_message.Message):
    __slots__ = ["interactor"]
    INTERACTOR_FIELD_NUMBER: _ClassVar[int]
    interactor: _interactor_pb2.Interactor
    def __init__(self, interactor: _Optional[_Union[_interactor_pb2.Interactor, _Mapping]] = ...) -> None: ...

class DescribeProblemGradingInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class DescribeProblemGradingOutput(_message.Message):
    __slots__ = ["ranges"]
    class Range(_message.Message):
        __slots__ = ["grade", "upper_bound"]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
        grade: int
        upper_bound: float
        def __init__(self, grade: _Optional[int] = ..., upper_bound: _Optional[float] = ...) -> None: ...
    RANGES_FIELD_NUMBER: _ClassVar[int]
    ranges: _containers.RepeatedCompositeFieldContainer[DescribeProblemGradingOutput.Range]
    def __init__(self, ranges: _Optional[_Iterable[_Union[DescribeProblemGradingOutput.Range, _Mapping]]] = ...) -> None: ...

class DescribeProblemInput(_message.Message):
    __slots__ = ["problem_ern", "problem_id"]
    PROBLEM_ERN_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_ern: str
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., problem_ern: _Optional[str] = ...) -> None: ...

class DescribeProblemOutput(_message.Message):
    __slots__ = ["problem"]
    PROBLEM_FIELD_NUMBER: _ClassVar[int]
    problem: _problem_pb2.Problem
    def __init__(self, problem: _Optional[_Union[_problem_pb2.Problem, _Mapping]] = ...) -> None: ...

class DescribeScoreInput(_message.Message):
    __slots__ = ["problem_id", "user_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    user_id: str
    def __init__(self, problem_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class DescribeScoreOutput(_message.Message):
    __slots__ = ["score"]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: _score_pb2.Score
    def __init__(self, score: _Optional[_Union[_score_pb2.Score, _Mapping]] = ...) -> None: ...

class DescribeSolutionInput(_message.Message):
    __slots__ = ["problem_id", "solution_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    solution_id: str
    def __init__(self, problem_id: _Optional[str] = ..., solution_id: _Optional[str] = ...) -> None: ...

class DescribeSolutionOutput(_message.Message):
    __slots__ = ["solution"]
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    solution: _solution_pb2.Solution
    def __init__(self, solution: _Optional[_Union[_solution_pb2.Solution, _Mapping]] = ...) -> None: ...

class DescribeStatementInput(_message.Message):
    __slots__ = ["problem_id", "statement_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    statement_id: str
    def __init__(self, problem_id: _Optional[str] = ..., statement_id: _Optional[str] = ...) -> None: ...

class DescribeStatementOutput(_message.Message):
    __slots__ = ["statement"]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: _statement_pb2.Statement
    def __init__(self, statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class DescribeSubmissionInput(_message.Message):
    __slots__ = ["problem_id", "submission_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    submission_id: str
    def __init__(self, problem_id: _Optional[str] = ..., submission_id: _Optional[str] = ...) -> None: ...

class DescribeSubmissionOutput(_message.Message):
    __slots__ = ["submission"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...

class DescribeTestInput(_message.Message):
    __slots__ = ["problem_id", "test_id", "testset_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    test_id: str
    testset_id: str
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ..., test_id: _Optional[str] = ...) -> None: ...

class DescribeTestOutput(_message.Message):
    __slots__ = ["test"]
    TEST_FIELD_NUMBER: _ClassVar[int]
    test: _test_pb2.Test
    def __init__(self, test: _Optional[_Union[_test_pb2.Test, _Mapping]] = ...) -> None: ...

class DescribeTestsetInput(_message.Message):
    __slots__ = ["problem_id", "testset_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    testset_id: str
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ...) -> None: ...

class DescribeTestsetOutput(_message.Message):
    __slots__ = ["testset"]
    TESTSET_FIELD_NUMBER: _ClassVar[int]
    testset: _testset_pb2.Testset
    def __init__(self, testset: _Optional[_Union[_testset_pb2.Testset, _Mapping]] = ...) -> None: ...

class DescribeVerifierInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class DescribeVerifierOutput(_message.Message):
    __slots__ = ["verifier"]
    VERIFIER_FIELD_NUMBER: _ClassVar[int]
    verifier: _verifier_pb2.Verifier
    def __init__(self, verifier: _Optional[_Union[_verifier_pb2.Verifier, _Mapping]] = ...) -> None: ...

class GrantPermissionInput(_message.Message):
    __slots__ = ["permission", "problem_id"]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    permission: _permission_pb2.Permission
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., permission: _Optional[_Union[_permission_pb2.Permission, _Mapping]] = ...) -> None: ...

class GrantPermissionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListAttachmentsInput(_message.Message):
    __slots__ = ["filters", "offset", "problem_id", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "name"]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListAttachmentsInput.Filter
    offset: int
    problem_id: str
    size: int
    def __init__(self, problem_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListAttachmentsInput.Filter, _Mapping]] = ...) -> None: ...

class ListAttachmentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_attachment_pb2.Attachment]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_attachment_pb2.Attachment, _Mapping]]] = ...) -> None: ...

class ListCategoriesInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "is_visible", "parent_id", "problem_id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        IS_VISIBLE_FIELD_NUMBER: _ClassVar[int]
        PARENT_ID_FIELD_NUMBER: _ClassVar[int]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        is_visible: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        parent_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        problem_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., parent_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., problem_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., is_visible: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListCategoriesInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListCategoriesInput.Filter, _Mapping]] = ...) -> None: ...

class ListCategoriesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_category_pb2.Category]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_category_pb2.Category, _Mapping]]] = ...) -> None: ...

class ListChangesInput(_message.Message):
    __slots__ = ["filters", "offset", "problem_id", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "ip_address", "timestamp", "type", "user_id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        ip_address: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        timestamp: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., ip_address: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., timestamp: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListChangesInput.Filter
    offset: int
    problem_id: str
    size: int
    def __init__(self, problem_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListChangesInput.Filter, _Mapping]] = ...) -> None: ...

class ListChangesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_change_pb2.Change]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_change_pb2.Change, _Mapping]]] = ...) -> None: ...

class ListCodeTemplatesInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ListCodeTemplatesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_template_pb2.Template]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_template_pb2.Template, _Mapping]]] = ...) -> None: ...

class ListExamplesInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ListExamplesOutput(_message.Message):
    __slots__ = ["examples"]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    examples: _containers.RepeatedCompositeFieldContainer[_test_pb2.Test]
    def __init__(self, examples: _Optional[_Iterable[_Union[_test_pb2.Test, _Mapping]]] = ...) -> None: ...

class ListPermissionsInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ListPermissionsOutput(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_permission_pb2.Permission]
    def __init__(self, items: _Optional[_Iterable[_Union[_permission_pb2.Permission, _Mapping]]] = ...) -> None: ...

class ListProblemTopInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ListProblemTopOutput(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_submission_pb2.Submission]
    def __init__(self, items: _Optional[_Iterable[_Union[_submission_pb2.Submission, _Mapping]]] = ...) -> None: ...

class ListProblemsInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["category_id", "id", "is_private", "is_visible", "number"]
        CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        IS_PRIVATE_FIELD_NUMBER: _ClassVar[int]
        IS_VISIBLE_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        category_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        is_private: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        is_visible: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        number: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., category_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., is_visible: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., is_private: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., number: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListProblemsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListProblemsInput.Filter, _Mapping]] = ...) -> None: ...

class ListProblemsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_problem_pb2.Problem]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_problem_pb2.Problem, _Mapping]]] = ...) -> None: ...

class ListSolutionsInput(_message.Message):
    __slots__ = ["filters", "offset", "problem_id", "size"]
    class Filter(_message.Message):
        __slots__ = ["author_id", "id", "lang", "moderation_status", "problem_id", "published"]
        AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        LANG_FIELD_NUMBER: _ClassVar[int]
        MODERATION_STATUS_FIELD_NUMBER: _ClassVar[int]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        PUBLISHED_FIELD_NUMBER: _ClassVar[int]
        author_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        lang: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        moderation_status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        problem_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        published: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., problem_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., author_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., moderation_status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., published: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., lang: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListSolutionsInput.Filter
    offset: int
    problem_id: str
    size: int
    def __init__(self, problem_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListSolutionsInput.Filter, _Mapping]] = ...) -> None: ...

class ListSolutionsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_solution_pb2.Solution]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_solution_pb2.Solution, _Mapping]]] = ...) -> None: ...

class ListStatementsInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ListStatementsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_statement_pb2.Statement]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_statement_pb2.Statement, _Mapping]]] = ...) -> None: ...

class ListTestsInput(_message.Message):
    __slots__ = ["problem_id", "testset_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    testset_id: str
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ...) -> None: ...

class ListTestsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_test_pb2.Test]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_test_pb2.Test, _Mapping]]] = ...) -> None: ...

class ListTestsetsInput(_message.Message):
    __slots__ = ["problem_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class ListTestsetsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_testset_pb2.Testset]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_testset_pb2.Testset, _Mapping]]] = ...) -> None: ...

class PublishSolutionInput(_message.Message):
    __slots__ = ["problem_id", "solution_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    solution_id: str
    def __init__(self, problem_id: _Optional[str] = ..., solution_id: _Optional[str] = ...) -> None: ...

class PublishSolutionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RefuseSolutionInput(_message.Message):
    __slots__ = ["comment", "problem_id", "solution_id"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    comment: str
    problem_id: str
    solution_id: str
    def __init__(self, problem_id: _Optional[str] = ..., solution_id: _Optional[str] = ..., comment: _Optional[str] = ...) -> None: ...

class RefuseSolutionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RetestSubmissionInput(_message.Message):
    __slots__ = ["debug", "problem_id", "submission_id"]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    debug: bool
    problem_id: str
    submission_id: str
    def __init__(self, problem_id: _Optional[str] = ..., submission_id: _Optional[str] = ..., debug: bool = ...) -> None: ...

class RetestSubmissionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RevokePermissionInput(_message.Message):
    __slots__ = ["problem_id", "user_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    user_id: str
    def __init__(self, problem_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class RevokePermissionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UnassignCategoryInput(_message.Message):
    __slots__ = ["category_id", "problem_id"]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    category_id: str
    problem_id: str
    def __init__(self, category_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class UnassignCategoryOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UnpublishSolutionInput(_message.Message):
    __slots__ = ["problem_id", "solution_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    solution_id: str
    def __init__(self, problem_id: _Optional[str] = ..., solution_id: _Optional[str] = ...) -> None: ...

class UnpublishSolutionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateAttachmentInput(_message.Message):
    __slots__ = ["attachment", "attachment_id", "problem_id"]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    attachment: _attachment_pb2.Attachment
    attachment_id: str
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., attachment_id: _Optional[str] = ..., attachment: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]] = ...) -> None: ...

class UpdateAttachmentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateCategoryInput(_message.Message):
    __slots__ = ["category", "category_id"]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    category: _category_pb2.Category
    category_id: str
    def __init__(self, category_id: _Optional[str] = ..., category: _Optional[_Union[_category_pb2.Category, _Mapping]] = ...) -> None: ...

class UpdateCategoryOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateCodeTemplateInput(_message.Message):
    __slots__ = ["problem_id", "template", "template_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    template: _template_pb2.Template
    template_id: str
    def __init__(self, problem_id: _Optional[str] = ..., template_id: _Optional[str] = ..., template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ...) -> None: ...

class UpdateCodeTemplateOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

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

class UpdatePrivacyInput(_message.Message):
    __slots__ = ["private", "problem_id"]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    private: bool
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., private: bool = ...) -> None: ...

class UpdatePrivacyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateSolutionInput(_message.Message):
    __slots__ = ["problem_id", "solution", "solution_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    solution: _solution_pb2.Solution
    solution_id: str
    def __init__(self, problem_id: _Optional[str] = ..., solution_id: _Optional[str] = ..., solution: _Optional[_Union[_solution_pb2.Solution, _Mapping]] = ...) -> None: ...

class UpdateSolutionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateStatementInput(_message.Message):
    __slots__ = ["problem_id", "statement", "statement_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    statement: _statement_pb2.Statement
    statement_id: str
    def __init__(self, problem_id: _Optional[str] = ..., statement_id: _Optional[str] = ..., statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class UpdateStatementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateTestInput(_message.Message):
    __slots__ = ["problem_id", "test", "test_id", "testset_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    TEST_FIELD_NUMBER: _ClassVar[int]
    TEST_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    test: _test_pb2.Test
    test_id: str
    testset_id: str
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ..., test_id: _Optional[str] = ..., test: _Optional[_Union[_test_pb2.Test, _Mapping]] = ...) -> None: ...

class UpdateTestOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateTestsetInput(_message.Message):
    __slots__ = ["problem_id", "testset", "testset_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    TESTSET_FIELD_NUMBER: _ClassVar[int]
    TESTSET_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    testset: _testset_pb2.Testset
    testset_id: str
    def __init__(self, problem_id: _Optional[str] = ..., testset_id: _Optional[str] = ..., testset: _Optional[_Union[_testset_pb2.Testset, _Mapping]] = ...) -> None: ...

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

class UpdateVisibilityInput(_message.Message):
    __slots__ = ["problem_id", "visible"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    visible: bool
    def __init__(self, problem_id: _Optional[str] = ..., visible: bool = ...) -> None: ...

class UpdateVisibilityOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
