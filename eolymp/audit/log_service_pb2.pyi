from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.audit import log_pb2 as _log_pb2
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
    __slots__ = ("offset", "size", "filters", "sort", "order", "extra")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListLogsInput.Sortable]
        TIMESTAMP: _ClassVar[ListLogsInput.Sortable]
    DEFAULT: ListLogsInput.Sortable
    TIMESTAMP: ListLogsInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("timestamp", "actor", "method", "scope", "ip_address", "user_agent", "mutation")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        ACTOR_FIELD_NUMBER: _ClassVar[int]
        METHOD_FIELD_NUMBER: _ClassVar[int]
        SCOPE_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        USER_AGENT_FIELD_NUMBER: _ClassVar[int]
        MUTATION_FIELD_NUMBER: _ClassVar[int]
        timestamp: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        actor: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        method: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        scope: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        ip_address: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        user_agent: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        mutation: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, timestamp: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., actor: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., method: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., scope: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., ip_address: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., user_agent: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., mutation: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListLogsInput.Filter
    sort: ListLogsInput.Sortable
    order: _direction_pb2.Direction
    extra: _containers.RepeatedScalarFieldContainer[_log_pb2.Log.Extra.Field]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListLogsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListLogsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_log_pb2.Log.Extra.Field, str]]] = ...) -> None: ...

class ListLogsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_log_pb2.Log]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_log_pb2.Log, _Mapping]]] = ...) -> None: ...

class DescribeLogInput(_message.Message):
    __slots__ = ("log_id", "extra")
    LOG_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    log_id: str
    extra: _containers.RepeatedScalarFieldContainer[_log_pb2.Log.Extra.Field]
    def __init__(self, log_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_log_pb2.Log.Extra.Field, str]]] = ...) -> None: ...

class DescribeLogOutput(_message.Message):
    __slots__ = ("log",)
    LOG_FIELD_NUMBER: _ClassVar[int]
    log: _log_pb2.Log
    def __init__(self, log: _Optional[_Union[_log_pb2.Log, _Mapping]] = ...) -> None: ...

class ExportLogsInput(_message.Message):
    __slots__ = ("filters", "sort", "order", "extra")
    class Filter(_message.Message):
        __slots__ = ("timestamp", "actor", "method", "scope", "ip_address", "user_agent", "mutation")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        ACTOR_FIELD_NUMBER: _ClassVar[int]
        METHOD_FIELD_NUMBER: _ClassVar[int]
        SCOPE_FIELD_NUMBER: _ClassVar[int]
        IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        USER_AGENT_FIELD_NUMBER: _ClassVar[int]
        MUTATION_FIELD_NUMBER: _ClassVar[int]
        timestamp: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        actor: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        method: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        scope: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        ip_address: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        user_agent: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        mutation: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, timestamp: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., actor: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., method: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., scope: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., ip_address: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., user_agent: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., mutation: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    filters: ExportLogsInput.Filter
    sort: ListLogsInput.Sortable
    order: _direction_pb2.Direction
    extra: _containers.RepeatedScalarFieldContainer[_log_pb2.Log.Extra.Field]
    def __init__(self, filters: _Optional[_Union[ExportLogsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListLogsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_log_pb2.Log.Extra.Field, str]]] = ...) -> None: ...

class ExportLogsOutput(_message.Message):
    __slots__ = ("export_url", "total", "truncated")
    EXPORT_URL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    export_url: str
    total: int
    truncated: bool
    def __init__(self, export_url: _Optional[str] = ..., total: _Optional[int] = ..., truncated: _Optional[bool] = ...) -> None: ...
