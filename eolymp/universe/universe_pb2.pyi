from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.universe import permission_pb2 as _permission_pb2
from eolymp.universe import space_pb2 as _space_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSpaceInput(_message.Message):
    __slots__ = ["space"]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: _space_pb2.Space
    def __init__(self, space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ...) -> None: ...

class CreateSpaceOutput(_message.Message):
    __slots__ = ["space_id"]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    def __init__(self, space_id: _Optional[str] = ...) -> None: ...

class DeleteSpaceInput(_message.Message):
    __slots__ = ["space_id"]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    def __init__(self, space_id: _Optional[str] = ...) -> None: ...

class DeleteSpaceOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribePermissionInput(_message.Message):
    __slots__ = ["space_id", "user_id"]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    user_id: str
    def __init__(self, space_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class DescribePermissionOutput(_message.Message):
    __slots__ = ["permission"]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    permission: _permission_pb2.Permission
    def __init__(self, permission: _Optional[_Union[_permission_pb2.Permission, _Mapping]] = ...) -> None: ...

class DescribeQuotaInput(_message.Message):
    __slots__ = ["space_id"]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    def __init__(self, space_id: _Optional[str] = ...) -> None: ...

class DescribeQuotaOutput(_message.Message):
    __slots__ = ["quota"]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    quota: _space_pb2.Space.Quota
    def __init__(self, quota: _Optional[_Union[_space_pb2.Space.Quota, _Mapping]] = ...) -> None: ...

class DescribeSpaceInput(_message.Message):
    __slots__ = ["space_id"]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    def __init__(self, space_id: _Optional[str] = ...) -> None: ...

class DescribeSpaceOutput(_message.Message):
    __slots__ = ["space"]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: _space_pb2.Space
    def __init__(self, space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ...) -> None: ...

class GrantPermissionInput(_message.Message):
    __slots__ = ["role", "space_id", "user_id"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    role: _permission_pb2.Permission.Role
    space_id: str
    user_id: str
    def __init__(self, space_id: _Optional[str] = ..., role: _Optional[_Union[_permission_pb2.Permission.Role, str]] = ..., user_id: _Optional[str] = ...) -> None: ...

class GrantPermissionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IntrospectPermissionInput(_message.Message):
    __slots__ = ["space_id"]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    def __init__(self, space_id: _Optional[str] = ...) -> None: ...

class IntrospectPermissionOutput(_message.Message):
    __slots__ = ["permission"]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    permission: _permission_pb2.Permission
    def __init__(self, permission: _Optional[_Union[_permission_pb2.Permission, _Mapping]] = ...) -> None: ...

class ListPermissionsInput(_message.Message):
    __slots__ = ["filters", "offset", "size", "space_id"]
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
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    filters: ListPermissionsInput.Filter
    offset: int
    size: int
    space_id: str
    def __init__(self, space_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListPermissionsInput.Filter, _Mapping]] = ...) -> None: ...

class ListPermissionsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_permission_pb2.Permission]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_permission_pb2.Permission, _Mapping]]] = ...) -> None: ...

class ListSpacesInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "key", "member", "name", "own", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        MEMBER_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OWN_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        key: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        member: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        own: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., key: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., own: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., member: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListSpacesInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListSpacesInput.Filter, _Mapping]] = ...) -> None: ...

class ListSpacesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_space_pb2.Space]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_space_pb2.Space, _Mapping]]] = ...) -> None: ...

class LookupSpaceInput(_message.Message):
    __slots__ = ["key"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class LookupSpaceOutput(_message.Message):
    __slots__ = ["space"]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: _space_pb2.Space
    def __init__(self, space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ...) -> None: ...

class RevokePermissionInput(_message.Message):
    __slots__ = ["space_id", "user_id"]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    user_id: str
    def __init__(self, space_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class RevokePermissionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateSpaceInput(_message.Message):
    __slots__ = ["space", "space_id"]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    space: _space_pb2.Space
    space_id: str
    def __init__(self, space_id: _Optional[str] = ..., space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ...) -> None: ...

class UpdateSpaceOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
