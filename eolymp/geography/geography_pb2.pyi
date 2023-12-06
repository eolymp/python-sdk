from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.geography import country_pb2 as _country_pb2
from eolymp.geography import region_pb2 as _region_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeCountryInput(_message.Message):
    __slots__ = ["country_id"]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    country_id: str
    def __init__(self, country_id: _Optional[str] = ...) -> None: ...

class DescribeCountryOutput(_message.Message):
    __slots__ = ["country"]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    country: _country_pb2.Country
    def __init__(self, country: _Optional[_Union[_country_pb2.Country, _Mapping]] = ...) -> None: ...

class DescribeRegionInput(_message.Message):
    __slots__ = ["region_id"]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    region_id: str
    def __init__(self, region_id: _Optional[str] = ...) -> None: ...

class DescribeRegionOutput(_message.Message):
    __slots__ = ["region"]
    REGION_FIELD_NUMBER: _ClassVar[int]
    region: _region_pb2.Region
    def __init__(self, region: _Optional[_Union[_region_pb2.Region, _Mapping]] = ...) -> None: ...

class ListCountriesInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "name", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListCountriesInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListCountriesInput.Filter, _Mapping]] = ...) -> None: ...

class ListCountriesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_country_pb2.Country]
    total: int
    def __init__(self, items: _Optional[_Iterable[_Union[_country_pb2.Country, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...

class ListRegionsInput(_message.Message):
    __slots__ = ["country_id", "filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["country_id", "id", "name", "query"]
        COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        country_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., country_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    country_id: str
    filters: ListRegionsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListRegionsInput.Filter, _Mapping]] = ..., country_id: _Optional[str] = ...) -> None: ...

class ListRegionsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_region_pb2.Region]
    total: int
    def __init__(self, items: _Optional[_Iterable[_Union[_region_pb2.Region, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...
