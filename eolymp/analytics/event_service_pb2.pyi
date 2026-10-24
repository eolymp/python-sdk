import datetime

from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CaptureEventInput(_message.Message):
    __slots__ = ("name", "route", "path", "referrer", "session_id", "locale", "properties")
    class PropertiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROUTE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    REFERRER_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    name: str
    route: str
    path: str
    referrer: str
    session_id: str
    locale: str
    properties: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., route: _Optional[str] = ..., path: _Optional[str] = ..., referrer: _Optional[str] = ..., session_id: _Optional[str] = ..., locale: _Optional[str] = ..., properties: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CaptureEventOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AggregateEventsInput(_message.Message):
    __slots__ = ("metric", "group_by", "range_start", "range_end", "filters")
    class Metric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_METRIC: _ClassVar[AggregateEventsInput.Metric]
        COUNT: _ClassVar[AggregateEventsInput.Metric]
        VISITORS: _ClassVar[AggregateEventsInput.Metric]
        USERS: _ClassVar[AggregateEventsInput.Metric]
        SESSIONS: _ClassVar[AggregateEventsInput.Metric]
    UNKNOWN_METRIC: AggregateEventsInput.Metric
    COUNT: AggregateEventsInput.Metric
    VISITORS: AggregateEventsInput.Metric
    USERS: AggregateEventsInput.Metric
    SESSIONS: AggregateEventsInput.Metric
    class Dimension(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_DIMENSION: _ClassVar[AggregateEventsInput.Dimension]
        OCCURRED_AT: _ClassVar[AggregateEventsInput.Dimension]
        NAME: _ClassVar[AggregateEventsInput.Dimension]
        ROUTE: _ClassVar[AggregateEventsInput.Dimension]
        REFERRER: _ClassVar[AggregateEventsInput.Dimension]
        LOCALE: _ClassVar[AggregateEventsInput.Dimension]
        DEVICE: _ClassVar[AggregateEventsInput.Dimension]
        BROWSER: _ClassVar[AggregateEventsInput.Dimension]
        OS: _ClassVar[AggregateEventsInput.Dimension]
        AUTHENTICATED: _ClassVar[AggregateEventsInput.Dimension]
    UNKNOWN_DIMENSION: AggregateEventsInput.Dimension
    OCCURRED_AT: AggregateEventsInput.Dimension
    NAME: AggregateEventsInput.Dimension
    ROUTE: AggregateEventsInput.Dimension
    REFERRER: AggregateEventsInput.Dimension
    LOCALE: AggregateEventsInput.Dimension
    DEVICE: AggregateEventsInput.Dimension
    BROWSER: AggregateEventsInput.Dimension
    OS: AggregateEventsInput.Dimension
    AUTHENTICATED: AggregateEventsInput.Dimension
    class Filter(_message.Message):
        __slots__ = ("name", "route", "path", "user_id", "referrer", "locale", "device", "browser", "os", "authenticated")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ROUTE_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        REFERRER_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_FIELD_NUMBER: _ClassVar[int]
        BROWSER_FIELD_NUMBER: _ClassVar[int]
        OS_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        route: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        path: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        referrer: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        device: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        browser: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        os: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        authenticated: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., route: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., path: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., referrer: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., device: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., browser: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., os: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., authenticated: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    METRIC_FIELD_NUMBER: _ClassVar[int]
    GROUP_BY_FIELD_NUMBER: _ClassVar[int]
    RANGE_START_FIELD_NUMBER: _ClassVar[int]
    RANGE_END_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    metric: AggregateEventsInput.Metric
    group_by: _containers.RepeatedScalarFieldContainer[AggregateEventsInput.Dimension]
    range_start: _timestamp_pb2.Timestamp
    range_end: _timestamp_pb2.Timestamp
    filters: AggregateEventsInput.Filter
    def __init__(self, metric: _Optional[_Union[AggregateEventsInput.Metric, str]] = ..., group_by: _Optional[_Iterable[_Union[AggregateEventsInput.Dimension, str]]] = ..., range_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., range_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., filters: _Optional[_Union[AggregateEventsInput.Filter, _Mapping]] = ...) -> None: ...

class AggregateEventsOutput(_message.Message):
    __slots__ = ("buckets",)
    class Bucket(_message.Message):
        __slots__ = ("dimensions", "count")
        DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        dimensions: _containers.RepeatedScalarFieldContainer[str]
        count: int
        def __init__(self, dimensions: _Optional[_Iterable[str]] = ..., count: _Optional[int] = ...) -> None: ...
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[AggregateEventsOutput.Bucket]
    def __init__(self, buckets: _Optional[_Iterable[_Union[AggregateEventsOutput.Bucket, _Mapping]]] = ...) -> None: ...
