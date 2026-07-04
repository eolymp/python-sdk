from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import contest_series_pb2 as _contest_series_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeContestSeriesInput(_message.Message):
    __slots__ = ("series_id", "locale", "extra")
    SERIES_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    series_id: str
    locale: str
    extra: _containers.RepeatedScalarFieldContainer[_contest_series_pb2.ContestSeries.Extra]
    def __init__(self, series_id: _Optional[str] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_contest_series_pb2.ContestSeries.Extra, str]]] = ...) -> None: ...

class DescribeContestSeriesOutput(_message.Message):
    __slots__ = ("series",)
    SERIES_FIELD_NUMBER: _ClassVar[int]
    series: _contest_series_pb2.ContestSeries
    def __init__(self, series: _Optional[_Union[_contest_series_pb2.ContestSeries, _Mapping]] = ...) -> None: ...

class ListContestSeriesInput(_message.Message):
    __slots__ = ("offset", "size", "locale", "search", "extra")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    locale: str
    search: str
    extra: _containers.RepeatedScalarFieldContainer[_contest_series_pb2.ContestSeries.Extra]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., locale: _Optional[str] = ..., search: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_contest_series_pb2.ContestSeries.Extra, str]]] = ...) -> None: ...

class ListContestSeriesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_contest_series_pb2.ContestSeries]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_contest_series_pb2.ContestSeries, _Mapping]]] = ...) -> None: ...

class CreateContestSeriesInput(_message.Message):
    __slots__ = ("series",)
    SERIES_FIELD_NUMBER: _ClassVar[int]
    series: _contest_series_pb2.ContestSeries
    def __init__(self, series: _Optional[_Union[_contest_series_pb2.ContestSeries, _Mapping]] = ...) -> None: ...

class CreateContestSeriesOutput(_message.Message):
    __slots__ = ("series_id",)
    SERIES_ID_FIELD_NUMBER: _ClassVar[int]
    series_id: str
    def __init__(self, series_id: _Optional[str] = ...) -> None: ...

class UpdateContestSeriesInput(_message.Message):
    __slots__ = ("series_id", "series")
    SERIES_ID_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    series_id: str
    series: _contest_series_pb2.ContestSeries
    def __init__(self, series_id: _Optional[str] = ..., series: _Optional[_Union[_contest_series_pb2.ContestSeries, _Mapping]] = ...) -> None: ...

class UpdateContestSeriesOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteContestSeriesInput(_message.Message):
    __slots__ = ("series_id",)
    SERIES_ID_FIELD_NUMBER: _ClassVar[int]
    series_id: str
    def __init__(self, series_id: _Optional[str] = ...) -> None: ...

class DeleteContestSeriesOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
