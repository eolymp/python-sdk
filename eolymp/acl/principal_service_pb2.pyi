from eolymp.acl import principal_pb2 as _principal_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreatePrincipalInput(_message.Message):
    __slots__ = ("principal",)
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    principal: _principal_pb2.Principal
    def __init__(self, principal: _Optional[_Union[_principal_pb2.Principal, _Mapping]] = ...) -> None: ...

class CreatePrincipalOutput(_message.Message):
    __slots__ = ("principal_id",)
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    principal_id: str
    def __init__(self, principal_id: _Optional[str] = ...) -> None: ...

class UpdatePrincipalInput(_message.Message):
    __slots__ = ("patch", "principal_id", "principal")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_principal_pb2.Principal.Patch.Field]
    principal_id: str
    principal: _principal_pb2.Principal
    def __init__(self, patch: _Optional[_Iterable[_Union[_principal_pb2.Principal.Patch.Field, str]]] = ..., principal_id: _Optional[str] = ..., principal: _Optional[_Union[_principal_pb2.Principal, _Mapping]] = ...) -> None: ...

class UpdatePrincipalOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeletePrincipalInput(_message.Message):
    __slots__ = ("principal_id",)
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    principal_id: str
    def __init__(self, principal_id: _Optional[str] = ...) -> None: ...

class DeletePrincipalOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribePrincipalInput(_message.Message):
    __slots__ = ("principal_id",)
    PRINCIPAL_ID_FIELD_NUMBER: _ClassVar[int]
    principal_id: str
    def __init__(self, principal_id: _Optional[str] = ...) -> None: ...

class DescribePrincipalOutput(_message.Message):
    __slots__ = ("principal",)
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    principal: _principal_pb2.Principal
    def __init__(self, principal: _Optional[_Union[_principal_pb2.Principal, _Mapping]] = ...) -> None: ...

class ListPrincipalsInput(_message.Message):
    __slots__ = ("offset", "size", "filters", "sort", "order")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ListPrincipalsInput.Sortable]
        NAME: _ClassVar[ListPrincipalsInput.Sortable]
    DEFAULT: ListPrincipalsInput.Sortable
    NAME: ListPrincipalsInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("query", "id", "user_id", "name")
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        query: str
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListPrincipalsInput.Filter
    sort: ListPrincipalsInput.Sortable
    order: _direction_pb2.Direction
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListPrincipalsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListPrincipalsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ...) -> None: ...

class ListPrincipalsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_principal_pb2.Principal]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_principal_pb2.Principal, _Mapping]]] = ...) -> None: ...
