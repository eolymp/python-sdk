from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import submission_pb2 as _submission_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class ListSubmissionsInput(_message.Message):
    __slots__ = ["after", "filters", "offset", "problem_id", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "member_id", "percentage", "problem_id", "runtime", "score", "status", "submitted_at", "user_id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        percentage: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        problem_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        runtime: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        score: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        submitted_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., problem_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., submitted_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., runtime: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., score: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ..., percentage: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    after: str
    filters: ListSubmissionsInput.Filter
    offset: int
    problem_id: str
    size: int
    def __init__(self, problem_id: _Optional[str] = ..., after: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListSubmissionsInput.Filter, _Mapping]] = ...) -> None: ...

class ListSubmissionsOutput(_message.Message):
    __slots__ = ["items", "next_page_cursor", "prev_page_cursor", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    PREV_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_submission_pb2.Submission]
    next_page_cursor: str
    prev_page_cursor: str
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_submission_pb2.Submission, _Mapping]]] = ..., next_page_cursor: _Optional[str] = ..., prev_page_cursor: _Optional[str] = ...) -> None: ...

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

class WatchSubmissionInput(_message.Message):
    __slots__ = ["problem_id", "submission_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    submission_id: str
    def __init__(self, problem_id: _Optional[str] = ..., submission_id: _Optional[str] = ...) -> None: ...

class WatchSubmissionOutput(_message.Message):
    __slots__ = ["submission"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...
