from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteMultipartUploadInput(_message.Message):
    __slots__ = ["object_id", "parts", "upload_id"]
    class Part(_message.Message):
        __slots__ = ["checksum_sha1", "etag", "number"]
        CHECKSUM_SHA1_FIELD_NUMBER: _ClassVar[int]
        ETAG_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        checksum_sha1: str
        etag: str
        number: int
        def __init__(self, number: _Optional[int] = ..., etag: _Optional[str] = ..., checksum_sha1: _Optional[str] = ...) -> None: ...
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    parts: _containers.RepeatedCompositeFieldContainer[CompleteMultipartUploadInput.Part]
    upload_id: str
    def __init__(self, object_id: _Optional[str] = ..., upload_id: _Optional[str] = ..., parts: _Optional[_Iterable[_Union[CompleteMultipartUploadInput.Part, _Mapping]]] = ...) -> None: ...

class CompleteMultipartUploadOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateObjectInput(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class CreateObjectOutput(_message.Message):
    __slots__ = ["blob_ern", "blob_hash", "key", "url"]
    BLOB_ERN_FIELD_NUMBER: _ClassVar[int]
    BLOB_HASH_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    blob_ern: str
    blob_hash: str
    key: str
    url: str
    def __init__(self, key: _Optional[str] = ..., blob_ern: _Optional[str] = ..., blob_hash: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

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

class StartMultipartUploadInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class StartMultipartUploadOutput(_message.Message):
    __slots__ = ["object_id", "upload_id"]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    upload_id: str
    def __init__(self, object_id: _Optional[str] = ..., upload_id: _Optional[str] = ...) -> None: ...

class UploadPartInput(_message.Message):
    __slots__ = ["data", "object_id", "part_number", "upload_id"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    object_id: str
    part_number: int
    upload_id: str
    def __init__(self, object_id: _Optional[str] = ..., upload_id: _Optional[str] = ..., part_number: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadPartOutput(_message.Message):
    __slots__ = ["etag"]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    etag: str
    def __init__(self, etag: _Optional[str] = ...) -> None: ...
