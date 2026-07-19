from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.automation import log_pb2 as _log_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListLogsInput(_message.Message):
    __slots__ = ("offset", "size", "filters", "sort", "order")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListLogsInput.Sortable]
        CREATED_AT: _ClassVar[ListLogsInput.Sortable]
    DEFAULT: ListLogsInput.Sortable
    CREATED_AT: ListLogsInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "rule_id", "trigger", "dry_run", "created_at")
        ID_FIELD_NUMBER: _ClassVar[int]
        RULE_ID_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        DRY_RUN_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        rule_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        trigger: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        dry_run: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        created_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., rule_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., trigger: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., dry_run: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., created_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListLogsInput.Filter
    sort: ListLogsInput.Sortable
    order: _direction_pb2.Direction
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListLogsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListLogsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListLogsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_log_pb2.Log]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_log_pb2.Log, _Mapping]]] = ...) -> None: ...

class DescribeLogInput(_message.Message):
    __slots__ = ("log_id",)
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    log_id: str
    def __init__(self, log_id: _Optional[str] = ...) -> None: ...

class DescribeLogOutput(_message.Message):
    __slots__ = ("log",)
    LOG_FIELD_NUMBER: _ClassVar[int]
    log: _log_pb2.Log
    def __init__(self, log: _Optional[_Union[_log_pb2.Log, _Mapping]] = ...) -> None: ...
