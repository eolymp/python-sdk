from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import access_key_pb2 as _access_key_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAccessKeyInput(_message.Message):
    __slots__ = ["expires_in", "name", "scope"]
    EXPIRES_IN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    expires_in: int
    name: str
    scope: str
    def __init__(self, name: _Optional[str] = ..., scope: _Optional[str] = ..., expires_in: _Optional[int] = ...) -> None: ...

class CreateAccessKeyOutput(_message.Message):
    __slots__ = ["key_id", "secret"]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    secret: str
    def __init__(self, key_id: _Optional[str] = ..., secret: _Optional[str] = ...) -> None: ...

class DeleteAccessKeyInput(_message.Message):
    __slots__ = ["key_id"]
    KEY_ID_FIELD_NUMBER: _ClassVar[int]
    key_id: str
    def __init__(self, key_id: _Optional[str] = ...) -> None: ...

class DeleteAccessKeyOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListAccessKeysInput(_message.Message):
    __slots__ = ["offset", "size"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListAccessKeysOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_access_key_pb2.AccessKey]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_access_key_pb2.AccessKey, _Mapping]]] = ...) -> None: ...
