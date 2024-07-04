from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.taxonomy import institution_pb2 as _institution_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeInstitutionInput(_message.Message):
    __slots__ = ["institution_id"]
    INSTITUTION_ID_FIELD_NUMBER: _ClassVar[int]
    institution_id: str
    def __init__(self, institution_id: _Optional[str] = ...) -> None: ...

class DescribeInstitutionOutput(_message.Message):
    __slots__ = ["institution"]
    INSTITUTION_FIELD_NUMBER: _ClassVar[int]
    institution: _institution_pb2.Institution
    def __init__(self, institution: _Optional[_Union[_institution_pb2.Institution, _Mapping]] = ...) -> None: ...

class ListInstitutionsInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["acronym", "country_id", "governance", "id", "level", "name", "query", "region_id", "type"]
        ACRONYM_FIELD_NUMBER: _ClassVar[int]
        COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
        GOVERNANCE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        LEVEL_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        REGION_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        acronym: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        country_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        governance: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        level: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        region_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., acronym: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., country_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., region_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., level: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., governance: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListInstitutionsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListInstitutionsInput.Filter, _Mapping]] = ...) -> None: ...

class ListInstitutionsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_institution_pb2.Institution]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_institution_pb2.Institution, _Mapping]]] = ...) -> None: ...
