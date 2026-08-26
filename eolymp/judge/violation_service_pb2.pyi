from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import evidence_pb2 as _evidence_pb2
from eolymp.judge import violation_pb2 as _violation_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateViolationInput(_message.Message):
    __slots__ = ("contest_id", "violation", "dont_notify")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_FIELD_NUMBER: _ClassVar[int]
    DONT_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    violation: _violation_pb2.Violation
    dont_notify: bool
    def __init__(self, contest_id: _Optional[str] = ..., violation: _Optional[_Union[_violation_pb2.Violation, _Mapping]] = ..., dont_notify: _Optional[bool] = ...) -> None: ...

class CreateViolationOutput(_message.Message):
    __slots__ = ("violation_id",)
    VIOLATION_ID_FIELD_NUMBER: _ClassVar[int]
    violation_id: str
    def __init__(self, violation_id: _Optional[str] = ...) -> None: ...

class UpdateViolationInput(_message.Message):
    __slots__ = ("patch", "contest_id", "violation_id", "violation")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_ID_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_violation_pb2.Violation.Patch.Field]
    contest_id: str
    violation_id: str
    violation: _violation_pb2.Violation
    def __init__(self, patch: _Optional[_Iterable[_Union[_violation_pb2.Violation.Patch.Field, str]]] = ..., contest_id: _Optional[str] = ..., violation_id: _Optional[str] = ..., violation: _Optional[_Union[_violation_pb2.Violation, _Mapping]] = ...) -> None: ...

class UpdateViolationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteViolationInput(_message.Message):
    __slots__ = ("contest_id", "violation_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    violation_id: str
    def __init__(self, contest_id: _Optional[str] = ..., violation_id: _Optional[str] = ...) -> None: ...

class DeleteViolationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeViolationInput(_message.Message):
    __slots__ = ("contest_id", "violation_id")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    violation_id: str
    def __init__(self, contest_id: _Optional[str] = ..., violation_id: _Optional[str] = ...) -> None: ...

class DescribeViolationOutput(_message.Message):
    __slots__ = ("violation",)
    VIOLATION_FIELD_NUMBER: _ClassVar[int]
    violation: _violation_pb2.Violation
    def __init__(self, violation: _Optional[_Union[_violation_pb2.Violation, _Mapping]] = ...) -> None: ...

class ListViolationEvidenceInput(_message.Message):
    __slots__ = ("contest_id", "violation_id", "offset", "size")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    violation_id: str
    offset: int
    size: int
    def __init__(self, contest_id: _Optional[str] = ..., violation_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListViolationEvidenceOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_evidence_pb2.Evidence]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_evidence_pb2.Evidence, _Mapping]]] = ...) -> None: ...

class ListViolationsInput(_message.Message):
    __slots__ = ("contest_id", "offset", "size", "filters", "sort", "order")
    class Sort(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListViolationsInput.Sort]
        CREATED_AT: _ClassVar[ListViolationsInput.Sort]
        CONFIDENCE: _ClassVar[ListViolationsInput.Sort]
    DEFAULT: ListViolationsInput.Sort
    CREATED_AT: ListViolationsInput.Sort
    CONFIDENCE: ListViolationsInput.Sort
    class Filter(_message.Message):
        __slots__ = ("id", "status", "type", "summary", "automatic", "confidence", "case_ref", "problem_id", "participant_id", "created_by", "confirmed_by")
        ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
        CASE_REF_FIELD_NUMBER: _ClassVar[int]
        PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
        PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
        CREATED_BY_FIELD_NUMBER: _ClassVar[int]
        CONFIRMED_BY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        summary: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        automatic: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        confidence: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        case_ref: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        problem_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        participant_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        created_by: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        confirmed_by: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., summary: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., automatic: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., confidence: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., case_ref: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., problem_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., participant_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., created_by: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., confirmed_by: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    offset: int
    size: int
    filters: ListViolationsInput.Filter
    sort: ListViolationsInput.Sort
    order: _direction_pb2.Direction
    def __init__(self, contest_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListViolationsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListViolationsInput.Sort, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListViolationsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_violation_pb2.Violation]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_violation_pb2.Violation, _Mapping]]] = ...) -> None: ...
