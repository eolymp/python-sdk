from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import submission_pb2 as _submission_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
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
    __slots__ = ["submission_id"]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    def __init__(self, submission_id: _Optional[str] = ...) -> None: ...

class DescribeSubmissionOutput(_message.Message):
    __slots__ = ["extra", "submission"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_submission_pb2.Submission.Extra]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_submission_pb2.Submission.Extra, str]]] = ...) -> None: ...

class DescribeSubmissionUsageInput(_message.Message):
    __slots__ = ["period_end", "period_start"]
    PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    PERIOD_START_FIELD_NUMBER: _ClassVar[int]
    period_end: _timestamp_pb2.Timestamp
    period_start: _timestamp_pb2.Timestamp
    def __init__(self, period_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DescribeSubmissionUsageOutput(_message.Message):
    __slots__ = ["available_evaluations", "monthly_evaluations", "monthly_submissions", "total_submissions"]
    AVAILABLE_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_SUBMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SUBMISSIONS_FIELD_NUMBER: _ClassVar[int]
    available_evaluations: int
    monthly_evaluations: int
    monthly_submissions: int
    total_submissions: int
    def __init__(self, total_submissions: _Optional[int] = ..., monthly_submissions: _Optional[int] = ..., monthly_evaluations: _Optional[int] = ..., available_evaluations: _Optional[int] = ...) -> None: ...

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

class ListSubmissionsInput(_message.Message):
    __slots__ = ["after", "extra", "filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "member_id", "percentage", "problem_id", "runtime", "score", "status", "submitted_at", "user_id", "verdict"]
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        percentage: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        problem_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        runtime: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        score: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        submitted_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        verdict: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., problem_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., submitted_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., runtime: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., verdict: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., score: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ..., percentage: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ...) -> None: ...
    AFTER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    after: str
    extra: _containers.RepeatedScalarFieldContainer[_submission_pb2.Submission.Extra]
    filters: ListSubmissionsInput.Filter
    offset: int
    size: int
    def __init__(self, after: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListSubmissionsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_submission_pb2.Submission.Extra, str]]] = ...) -> None: ...

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
    __slots__ = ["debug", "submission_id"]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    debug: bool
    submission_id: str
    def __init__(self, submission_id: _Optional[str] = ..., debug: bool = ...) -> None: ...

class RetestSubmissionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SubmissionChangedEvent(_message.Message):
    __slots__ = ["after", "before"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    after: _submission_pb2.Submission
    before: _submission_pb2.Submission
    def __init__(self, before: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ..., after: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...

class SubmissionCompleteEvent(_message.Message):
    __slots__ = ["submission", "update"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    update: bool
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ..., update: bool = ...) -> None: ...

class WatchSubmissionInput(_message.Message):
    __slots__ = ["extra", "submission_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_submission_pb2.Submission.Extra]
    submission_id: str
    def __init__(self, submission_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_submission_pb2.Submission.Extra, str]]] = ...) -> None: ...

class WatchSubmissionOutput(_message.Message):
    __slots__ = ["submission"]
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...
