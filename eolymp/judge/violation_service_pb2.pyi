from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import violation_pb2 as _violation_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateViolationInput(_message.Message):
    __slots__ = ("violation", "dont_notify")
    VIOLATION_FIELD_NUMBER: _ClassVar[int]
    DONT_NOTIFY_FIELD_NUMBER: _ClassVar[int]
    violation: _violation_pb2.Violation
    dont_notify: bool
    def __init__(self, violation: _Optional[_Union[_violation_pb2.Violation, _Mapping]] = ..., dont_notify: bool = ...) -> None: ...

class CreateViolationOutput(_message.Message):
    __slots__ = ("violation_id",)
    VIOLATION_ID_FIELD_NUMBER: _ClassVar[int]
    violation_id: str
    def __init__(self, violation_id: _Optional[str] = ...) -> None: ...

class UpdateViolationInput(_message.Message):
    __slots__ = ("patch", "violation_id", "violation")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_ID_FIELD_NUMBER: _ClassVar[int]
    VIOLATION_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_violation_pb2.Violation.Patch.Field]
    violation_id: str
    violation: _violation_pb2.Violation
    def __init__(self, patch: _Optional[_Iterable[_Union[_violation_pb2.Violation.Patch.Field, str]]] = ..., violation_id: _Optional[str] = ..., violation: _Optional[_Union[_violation_pb2.Violation, _Mapping]] = ...) -> None: ...

class UpdateViolationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteViolationInput(_message.Message):
    __slots__ = ("violation_id",)
    VIOLATION_ID_FIELD_NUMBER: _ClassVar[int]
    violation_id: str
    def __init__(self, violation_id: _Optional[str] = ...) -> None: ...

class DeleteViolationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeViolationInput(_message.Message):
    __slots__ = ("violation_id",)
    VIOLATION_ID_FIELD_NUMBER: _ClassVar[int]
    violation_id: str
    def __init__(self, violation_id: _Optional[str] = ...) -> None: ...

class DescribeViolationOutput(_message.Message):
    __slots__ = ("violation",)
    VIOLATION_FIELD_NUMBER: _ClassVar[int]
    violation: _violation_pb2.Violation
    def __init__(self, violation: _Optional[_Union[_violation_pb2.Violation, _Mapping]] = ...) -> None: ...

class ListViolationsInput(_message.Message):
    __slots__ = ("offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "status", "type", "summary", "automatic", "participant_id", "submission_id", "created_by", "confirmed_by")
        ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
        SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
        CREATED_BY_FIELD_NUMBER: _ClassVar[int]
        CONFIRMED_BY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        status: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        summary: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        automatic: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        participant_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        submission_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        created_by: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        confirmed_by: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., status: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., summary: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., automatic: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., participant_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., submission_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., created_by: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., confirmed_by: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListViolationsInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListViolationsInput.Filter, _Mapping]] = ...) -> None: ...

class ListViolationsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_violation_pb2.Violation]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_violation_pb2.Violation, _Mapping]]] = ...) -> None: ...
