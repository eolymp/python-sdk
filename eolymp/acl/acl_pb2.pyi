from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeInput(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class DescribeOutput(_message.Message):
    __slots__ = ["grant"]
    GRANT_FIELD_NUMBER: _ClassVar[int]
    grant: Grant
    def __init__(self, grant: _Optional[_Union[Grant, _Mapping]] = ...) -> None: ...

class Grant(_message.Message):
    __slots__ = ["entitlements", "id", "role", "user_id"]
    ENTITLEMENTS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    entitlements: _containers.RepeatedScalarFieldContainer[str]
    id: str
    role: str
    user_id: str
    def __init__(self, id: _Optional[str] = ..., role: _Optional[str] = ..., user_id: _Optional[str] = ..., entitlements: _Optional[_Iterable[str]] = ...) -> None: ...

class GrantInput(_message.Message):
    __slots__ = ["entitlements", "role", "user_id"]
    ENTITLEMENTS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    entitlements: _containers.RepeatedScalarFieldContainer[str]
    role: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., role: _Optional[str] = ..., entitlements: _Optional[_Iterable[str]] = ...) -> None: ...

class GrantOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IntrospectInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IntrospectOutput(_message.Message):
    __slots__ = ["grant"]
    GRANT_FIELD_NUMBER: _ClassVar[int]
    grant: Grant
    def __init__(self, grant: _Optional[_Union[Grant, _Mapping]] = ...) -> None: ...

class ListInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "role", "user_id"]
        ID_FIELD_NUMBER: _ClassVar[int]
        ROLE_FIELD_NUMBER: _ClassVar[int]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        role: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        user_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., user_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., role: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListInput.Filter, _Mapping]] = ...) -> None: ...

class ListOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Grant]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[Grant, _Mapping]]] = ...) -> None: ...

class RevokeInput(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class RevokeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
