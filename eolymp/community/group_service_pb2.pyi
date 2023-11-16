from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import group_pb2 as _group_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateGroupInput(_message.Message):
    __slots__ = ["group"]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: _group_pb2.Group
    def __init__(self, group: _Optional[_Union[_group_pb2.Group, _Mapping]] = ...) -> None: ...

class CreateGroupOutput(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class DeleteGroupInput(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class DeleteGroupOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeGroupInput(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class DescribeGroupOutput(_message.Message):
    __slots__ = ["group"]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: _group_pb2.Group
    def __init__(self, group: _Optional[_Union[_group_pb2.Group, _Mapping]] = ...) -> None: ...

class ListGroupsInput(_message.Message):
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
    filters: ListGroupsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListGroupsInput.Filter, _Mapping]] = ...) -> None: ...

class ListGroupsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_group_pb2.Group]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_group_pb2.Group, _Mapping]]] = ...) -> None: ...

class UpdateGroupInput(_message.Message):
    __slots__ = ["group", "group_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateGroupInput.Patch
    DESCRIPTION: UpdateGroupInput.Patch
    GROUP_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME: UpdateGroupInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    group: _group_pb2.Group
    group_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateGroupInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateGroupInput.Patch, str]]] = ..., group_id: _Optional[str] = ..., group: _Optional[_Union[_group_pb2.Group, _Mapping]] = ...) -> None: ...

class UpdateGroupOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
