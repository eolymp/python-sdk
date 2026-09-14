from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.commerce import store_pb2 as _store_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeStoreInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeStoreOutput(_message.Message):
    __slots__ = ("store",)
    STORE_FIELD_NUMBER: _ClassVar[int]
    store: _store_pb2.Store
    def __init__(self, store: _Optional[_Union[_store_pb2.Store, _Mapping]] = ...) -> None: ...

class UpdateStoreInput(_message.Message):
    __slots__ = ("store",)
    STORE_FIELD_NUMBER: _ClassVar[int]
    store: _store_pb2.Store.Patch
    def __init__(self, store: _Optional[_Union[_store_pb2.Store.Patch, _Mapping]] = ...) -> None: ...

class UpdateStoreOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SyncCatalogInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SyncCatalogOutput(_message.Message):
    __slots__ = ("synced",)
    SYNCED_FIELD_NUMBER: _ClassVar[int]
    synced: int
    def __init__(self, synced: _Optional[int] = ...) -> None: ...
