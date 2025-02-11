from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.universe import quota_pb2 as _quota_pb2
from eolymp.universe import space_pb2 as _space_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSpaceInput(_message.Message):
    __slots__ = ("space",)
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: _space_pb2.Space
    def __init__(self, space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ...) -> None: ...

class CreateSpaceOutput(_message.Message):
    __slots__ = ("space_id",)
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    def __init__(self, space_id: _Optional[str] = ...) -> None: ...

class UpdateSpaceInput(_message.Message):
    __slots__ = ("patch", "space_id", "space")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateSpaceInput.Patch]
        KEY: _ClassVar[UpdateSpaceInput.Patch]
        NAME: _ClassVar[UpdateSpaceInput.Patch]
        IMAGE: _ClassVar[UpdateSpaceInput.Patch]
        TYPE: _ClassVar[UpdateSpaceInput.Patch]
        VISIBILITY: _ClassVar[UpdateSpaceInput.Patch]
    ALL: UpdateSpaceInput.Patch
    KEY: UpdateSpaceInput.Patch
    NAME: UpdateSpaceInput.Patch
    IMAGE: UpdateSpaceInput.Patch
    TYPE: UpdateSpaceInput.Patch
    VISIBILITY: UpdateSpaceInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateSpaceInput.Patch]
    space_id: str
    space: _space_pb2.Space
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateSpaceInput.Patch, str]]] = ..., space_id: _Optional[str] = ..., space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ...) -> None: ...

class UpdateSpaceOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteSpaceInput(_message.Message):
    __slots__ = ("space_id",)
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    def __init__(self, space_id: _Optional[str] = ...) -> None: ...

class DeleteSpaceOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LookupSpaceInput(_message.Message):
    __slots__ = ("key", "extra")
    KEY_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    key: str
    extra: _containers.RepeatedScalarFieldContainer[_space_pb2.Space.Extra]
    def __init__(self, key: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_space_pb2.Space.Extra, str]]] = ...) -> None: ...

class LookupSpaceOutput(_message.Message):
    __slots__ = ("space",)
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: _space_pb2.Space
    def __init__(self, space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ...) -> None: ...

class DescribeSpaceInput(_message.Message):
    __slots__ = ("space_id", "extra")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    extra: _containers.RepeatedScalarFieldContainer[_space_pb2.Space.Extra]
    def __init__(self, space_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_space_pb2.Space.Extra, str]]] = ...) -> None: ...

class DescribeSpaceOutput(_message.Message):
    __slots__ = ("space",)
    SPACE_FIELD_NUMBER: _ClassVar[int]
    space: _space_pb2.Space
    def __init__(self, space: _Optional[_Union[_space_pb2.Space, _Mapping]] = ...) -> None: ...

class DescribeQuotaInput(_message.Message):
    __slots__ = ("space_id",)
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    def __init__(self, space_id: _Optional[str] = ...) -> None: ...

class DescribeQuotaOutput(_message.Message):
    __slots__ = ("quota",)
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    quota: _quota_pb2.Quota
    def __init__(self, quota: _Optional[_Union[_quota_pb2.Quota, _Mapping]] = ...) -> None: ...

class UpdateQuotaInput(_message.Message):
    __slots__ = ("space_id", "quota")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    quota: _quota_pb2.Quota
    def __init__(self, space_id: _Optional[str] = ..., quota: _Optional[_Union[_quota_pb2.Quota, _Mapping]] = ...) -> None: ...

class UpdateQuotaOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSpacesInput(_message.Message):
    __slots__ = ("offset", "size", "filters", "extra")
    class Filter(_message.Message):
        __slots__ = ("query", "id", "key", "name", "own")
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        OWN_FIELD_NUMBER: _ClassVar[int]
        query: str
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        key: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        own: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., key: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., own: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListSpacesInput.Filter
    extra: _containers.RepeatedScalarFieldContainer[_space_pb2.Space.Extra]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListSpacesInput.Filter, _Mapping]] = ..., extra: _Optional[_Iterable[_Union[_space_pb2.Space.Extra, str]]] = ...) -> None: ...

class ListSpacesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_space_pb2.Space]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_space_pb2.Space, _Mapping]]] = ...) -> None: ...
