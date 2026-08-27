from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import submission_pb2 as _submission_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from eolymp.wellknown import watch_pb2 as _watch_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSubmissionInput(_message.Message):
    __slots__ = ("course_id", "material_id", "runtime", "source", "output")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    material_id: str
    runtime: str
    source: str
    output: _submission_pb2.Submission.Output
    def __init__(self, course_id: _Optional[str] = ..., material_id: _Optional[str] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., output: _Optional[_Union[_submission_pb2.Submission.Output, _Mapping]] = ...) -> None: ...

class CreateSubmissionOutput(_message.Message):
    __slots__ = ("submission_id",)
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    def __init__(self, submission_id: _Optional[str] = ...) -> None: ...

class ListSubmissionsInput(_message.Message):
    __slots__ = ("course_id", "after", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "member_id", "material_id", "submitted_at", "runtime", "status", "verdict", "score", "percentage")
        ID_FIELD_NUMBER: _ClassVar[int]
        MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
        MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
        SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        VERDICT_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        material_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        submitted_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        runtime: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        verdict: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        score: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        percentage: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., member_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., material_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., submitted_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., runtime: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., verdict: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., score: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ..., percentage: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ...) -> None: ...
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    after: str
    size: int
    filters: ListSubmissionsInput.Filter
    def __init__(self, course_id: _Optional[str] = ..., after: _Optional[str] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListSubmissionsInput.Filter, _Mapping]] = ...) -> None: ...

class ListSubmissionsOutput(_message.Message):
    __slots__ = ("total", "items", "next_page_cursor")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_submission_pb2.Submission]
    next_page_cursor: str
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_submission_pb2.Submission, _Mapping]]] = ..., next_page_cursor: _Optional[str] = ...) -> None: ...

class DescribeSubmissionInput(_message.Message):
    __slots__ = ("course_id", "submission_id")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    submission_id: str
    def __init__(self, course_id: _Optional[str] = ..., submission_id: _Optional[str] = ...) -> None: ...

class DescribeSubmissionOutput(_message.Message):
    __slots__ = ("submission",)
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...

class WatchSubmissionInput(_message.Message):
    __slots__ = ("course_id", "submission_id")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    submission_id: str
    def __init__(self, course_id: _Optional[str] = ..., submission_id: _Optional[str] = ...) -> None: ...

class WatchSubmissionOutput(_message.Message):
    __slots__ = ("submission", "event")
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    event: _watch_pb2.WatchEventType
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ..., event: _Optional[_Union[_watch_pb2.WatchEventType, str]] = ...) -> None: ...
