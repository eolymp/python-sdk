from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateObjectInput(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class CreateObjectOutput(_message.Message):
    __slots__ = ["blob_ern", "blob_hash", "key"]
    BLOB_ERN_FIELD_NUMBER: _ClassVar[int]
    BLOB_HASH_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    blob_ern: str
    blob_hash: str
    key: str
    def __init__(self, key: _Optional[str] = ..., blob_ern: _Optional[str] = ..., blob_hash: _Optional[str] = ...) -> None: ...

class DescribeObjectInput(_message.Message):
    __slots__ = ["key"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class DescribeObjectOutput(_message.Message):
    __slots__ = ["size"]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    size: int
    def __init__(self, size: _Optional[int] = ...) -> None: ...

class DownloadObjectInput(_message.Message):
    __slots__ = ["key", "offset", "size"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    key: str
    offset: int
    size: int
    def __init__(self, key: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class DownloadObjectOutput(_message.Message):
    __slots__ = ["data", "size"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    size: int
    def __init__(self, data: _Optional[bytes] = ..., size: _Optional[int] = ...) -> None: ...
