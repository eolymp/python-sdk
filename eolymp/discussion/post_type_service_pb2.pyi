from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.discussion import post_type_pb2 as _post_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreatePostTypeInput(_message.Message):
    __slots__ = ["type"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _post_type_pb2.PostType
    def __init__(self, type: _Optional[_Union[_post_type_pb2.PostType, _Mapping]] = ...) -> None: ...

class CreatePostTypeOutput(_message.Message):
    __slots__ = ["type_id"]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    type_id: str
    def __init__(self, type_id: _Optional[str] = ...) -> None: ...

class DeletePostTypeInput(_message.Message):
    __slots__ = ["type_id"]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    type_id: str
    def __init__(self, type_id: _Optional[str] = ...) -> None: ...

class DeletePostTypeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribePostTypeInput(_message.Message):
    __slots__ = ["extra", "locale", "type_id"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_post_type_pb2.PostType.Extra]
    locale: str
    type_id: str
    def __init__(self, type_id: _Optional[str] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_post_type_pb2.PostType.Extra, str]]] = ...) -> None: ...

class DescribePostTypeOutput(_message.Message):
    __slots__ = ["type"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _post_type_pb2.PostType
    def __init__(self, type: _Optional[_Union[_post_type_pb2.PostType, _Mapping]] = ...) -> None: ...

class ListPostTypesInput(_message.Message):
    __slots__ = ["extra", "locale", "offset", "size"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_post_type_pb2.PostType.Extra]
    locale: str
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., locale: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_post_type_pb2.PostType.Extra, str]]] = ...) -> None: ...

class ListPostTypesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_post_type_pb2.PostType]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_post_type_pb2.PostType, _Mapping]]] = ...) -> None: ...

class UpdatePostTypeInput(_message.Message):
    __slots__ = ["type", "type_id"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    type: _post_type_pb2.PostType
    type_id: str
    def __init__(self, type_id: _Optional[str] = ..., type: _Optional[_Union[_post_type_pb2.PostType, _Mapping]] = ...) -> None: ...

class UpdatePostTypeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
