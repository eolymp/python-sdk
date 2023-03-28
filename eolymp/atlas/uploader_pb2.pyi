from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteMultipartUploadInput(_message.Message):
    __slots__ = ["parts", "upload_id"]
    class Part(_message.Message):
        __slots__ = ["checksum_md5", "checksum_sha1", "checksum_sha256", "etag", "number"]
        CHECKSUM_MD5_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_SHA1_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_SHA256_FIELD_NUMBER: _ClassVar[int]
        ETAG_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        checksum_md5: str
        checksum_sha1: str
        checksum_sha256: str
        etag: str
        number: int
        def __init__(self, number: _Optional[int] = ..., etag: _Optional[str] = ..., checksum_md5: _Optional[str] = ..., checksum_sha1: _Optional[str] = ..., checksum_sha256: _Optional[str] = ...) -> None: ...
    PARTS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    parts: _containers.RepeatedCompositeFieldContainer[CompleteMultipartUploadInput.Part]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ..., parts: _Optional[_Iterable[_Union[CompleteMultipartUploadInput.Part, _Mapping]]] = ...) -> None: ...

class CompleteMultipartUploadOutput(_message.Message):
    __slots__ = ["file_id"]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    def __init__(self, file_id: _Optional[str] = ...) -> None: ...

class StartMultipartUploadInput(_message.Message):
    __slots__ = ["name", "type"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    def __init__(self, type: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class StartMultipartUploadOutput(_message.Message):
    __slots__ = ["upload_id"]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ...) -> None: ...

class UploadFileInput(_message.Message):
    __slots__ = ["checksum_md5", "checksum_sha1", "checksum_sha256", "data", "name", "type"]
    CHECKSUM_MD5_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_SHA1_FIELD_NUMBER: _ClassVar[int]
    CHECKSUM_SHA256_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    checksum_md5: str
    checksum_sha1: str
    checksum_sha256: str
    data: bytes
    name: str
    type: str
    def __init__(self, type: _Optional[str] = ..., name: _Optional[str] = ..., checksum_md5: _Optional[str] = ..., checksum_sha1: _Optional[str] = ..., checksum_sha256: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadFileOutput(_message.Message):
    __slots__ = ["file_id"]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    def __init__(self, file_id: _Optional[str] = ...) -> None: ...

class UploadPartInput(_message.Message):
    __slots__ = ["data", "part_number", "upload_id"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    part_number: int
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ..., part_number: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadPartOutput(_message.Message):
    __slots__ = ["etag"]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    etag: str
    def __init__(self, etag: _Optional[str] = ...) -> None: ...
