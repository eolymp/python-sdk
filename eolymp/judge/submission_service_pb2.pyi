from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import submission_pb2 as _submission_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSubmissionInput(_message.Message):
    __slots__ = ("contest_id", "problem_id", "lang", "source")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    lang: str
    source: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ..., lang: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class CreateSubmissionOutput(_message.Message):
    __slots__ = ("submission_id",)
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    submission_id: str
    def __init__(self, submission_id: _Optional[str] = ...) -> None: ...

class ListSubmissionsInput(_message.Message):
    __slots__ = ("contest_id", "offset", "size", "filters", "extra")
    class Filter(_message.Message):
        __slots__ = ("id", "participant_id", "problem_id", "status", "lang", "score", "percentage", "submitted_at", "signature")
        ID_FIELD_NUMBER: _ClassVar[int]
        PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        LANG_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        SUBMITTED_AT_FIELD_NUMBER: _ClassVar[int]
        SIGNATURE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        participant_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        problem_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        lang: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        score: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        percentage: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionFloat]
        submitted_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        signature: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., participant_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., problem_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., lang: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., score: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ..., percentage: _Optional[_Iterable[_Union[_expression_pb2.ExpressionFloat, _Mapping]]] = ..., submitted_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., signature: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    offset: int
    size: int
    filters: ListSubmissionsInput.Filter
    extra: _containers.RepeatedScalarFieldContainer[_submission_pb2.Submission.Extra]
    def __init__(self, contest_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListSubmissionsInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_submission_pb2.Submission.Extra, str]]] = ...) -> None: ...

class ListSubmissionsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_submission_pb2.Submission]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_submission_pb2.Submission, _Mapping]]] = ...) -> None: ...

class DescribeSubmissionInput(_message.Message):
    __slots__ = ("contest_id", "submission_id", "extra")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    submission_id: str
    extra: _containers.RepeatedScalarFieldContainer[_submission_pb2.Submission.Extra]
    def __init__(self, contest_id: _Optional[str] = ..., submission_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_submission_pb2.Submission.Extra, str]]] = ...) -> None: ...

class DescribeSubmissionOutput(_message.Message):
    __slots__ = ("submission",)
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...

class PrintSubmissionInput(_message.Message):
    __slots__ = ("contest_id", "submission_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    submission_id: str
    def __init__(self, contest_id: _Optional[str] = ..., submission_id: _Optional[str] = ...) -> None: ...

class PrintSubmissionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WatchSubmissionInput(_message.Message):
    __slots__ = ("contest_id", "submission_id", "extra")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    submission_id: str
    extra: _containers.RepeatedScalarFieldContainer[_submission_pb2.Submission.Extra]
    def __init__(self, contest_id: _Optional[str] = ..., submission_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_submission_pb2.Submission.Extra, str]]] = ...) -> None: ...

class WatchSubmissionOutput(_message.Message):
    __slots__ = ("submission",)
    SUBMISSION_FIELD_NUMBER: _ClassVar[int]
    submission: _submission_pb2.Submission
    def __init__(self, submission: _Optional[_Union[_submission_pb2.Submission, _Mapping]] = ...) -> None: ...

class RetestSubmissionInput(_message.Message):
    __slots__ = ("contest_id", "submission_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    submission_id: str
    def __init__(self, contest_id: _Optional[str] = ..., submission_id: _Optional[str] = ...) -> None: ...

class RetestSubmissionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteSubmissionInput(_message.Message):
    __slots__ = ("contest_id", "submission_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    submission_id: str
    def __init__(self, contest_id: _Optional[str] = ..., submission_id: _Optional[str] = ...) -> None: ...

class DeleteSubmissionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RestoreSubmissionInput(_message.Message):
    __slots__ = ("contest_id", "submission_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    submission_id: str
    def __init__(self, contest_id: _Optional[str] = ..., submission_id: _Optional[str] = ...) -> None: ...

class RestoreSubmissionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RetestProblemInput(_message.Message):
    __slots__ = ("contest_id", "problem_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    problem_id: str
    def __init__(self, contest_id: _Optional[str] = ..., problem_id: _Optional[str] = ...) -> None: ...

class RetestProblemOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
