from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppendStreamInput(_message.Message):
    __slots__ = ["data", "offset", "stream_id"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    offset: int
    stream_id: str
    def __init__(self, stream_id: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class AppendStreamOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CloseStreamInput(_message.Message):
    __slots__ = ["stream_id"]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    def __init__(self, stream_id: _Optional[str] = ...) -> None: ...

class CloseStreamOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CompleteMultipartUploadInput(_message.Message):
    __slots__ = ["parts", "upload_id"]
    class Part(_message.Message):
        __slots__ = ["checksum_md5", "checksum_sha1", "checksum_sha256", "number", "token"]
        CHECKSUM_MD5_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_SHA1_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_SHA256_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        checksum_md5: str
        checksum_sha1: str
        checksum_sha256: str
        number: int
        token: str
        def __init__(self, number: _Optional[int] = ..., token: _Optional[str] = ..., checksum_md5: _Optional[str] = ..., checksum_sha1: _Optional[str] = ..., checksum_sha256: _Optional[str] = ...) -> None: ...
    PARTS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    parts: _containers.RepeatedCompositeFieldContainer[CompleteMultipartUploadInput.Part]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ..., parts: _Optional[_Iterable[_Union[CompleteMultipartUploadInput.Part, _Mapping]]] = ...) -> None: ...

class CompleteMultipartUploadOutput(_message.Message):
    __slots__ = ["asset_url"]
    ASSET_URL_FIELD_NUMBER: _ClassVar[int]
    asset_url: str
    def __init__(self, asset_url: _Optional[str] = ...) -> None: ...

class LookupAssetInput(_message.Message):
    __slots__ = ["key"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class LookupAssetOutput(_message.Message):
    __slots__ = ["asset_url"]
    ASSET_URL_FIELD_NUMBER: _ClassVar[int]
    asset_url: str
    def __init__(self, asset_url: _Optional[str] = ...) -> None: ...

class StartMultipartUploadInput(_message.Message):
    __slots__ = ["keys", "name", "ttl", "type"]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedScalarFieldContainer[str]
    name: str
    ttl: int
    type: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., keys: _Optional[_Iterable[str]] = ..., ttl: _Optional[int] = ...) -> None: ...

class StartMultipartUploadOutput(_message.Message):
    __slots__ = ["upload_id"]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ...) -> None: ...

class StartStreamInput(_message.Message):
    __slots__ = ["name", "ttl", "type"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    ttl: int
    type: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., ttl: _Optional[int] = ...) -> None: ...

class StartStreamOutput(_message.Message):
    __slots__ = ["stream_id", "stream_url"]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    stream_url: str
    def __init__(self, stream_id: _Optional[str] = ..., stream_url: _Optional[str] = ...) -> None: ...

class UploadAssetInput(_message.Message):
    __slots__ = ["data", "keys", "name", "ttl", "type"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    keys: _containers.RepeatedScalarFieldContainer[str]
    name: str
    ttl: int
    type: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., keys: _Optional[_Iterable[str]] = ..., ttl: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadAssetOutput(_message.Message):
    __slots__ = ["asset_url"]
    ASSET_URL_FIELD_NUMBER: _ClassVar[int]
    asset_url: str
    def __init__(self, asset_url: _Optional[str] = ...) -> None: ...

class UploadFileInput(_message.Message):
    __slots__ = ["data", "name", "type"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    name: str
    type: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadFileOutput(_message.Message):
    __slots__ = ["file_url"]
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    file_url: str
    def __init__(self, file_url: _Optional[str] = ...) -> None: ...

class UploadImageInput(_message.Message):
    __slots__ = ["crop", "data", "name", "size", "type", "variants"]
    class Crop(_message.Message):
        __slots__ = ["bottom", "left", "right", "top"]
        BOTTOM_FIELD_NUMBER: _ClassVar[int]
        LEFT_FIELD_NUMBER: _ClassVar[int]
        RIGHT_FIELD_NUMBER: _ClassVar[int]
        TOP_FIELD_NUMBER: _ClassVar[int]
        bottom: int
        left: int
        right: int
        top: int
        def __init__(self, top: _Optional[int] = ..., right: _Optional[int] = ..., bottom: _Optional[int] = ..., left: _Optional[int] = ...) -> None: ...
    class Size(_message.Message):
        __slots__ = ["height", "width"]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        height: int
        width: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    CROP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    crop: UploadImageInput.Crop
    data: bytes
    name: str
    size: UploadImageInput.Size
    type: str
    variants: _containers.RepeatedCompositeFieldContainer[UploadImageInput.Size]
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., crop: _Optional[_Union[UploadImageInput.Crop, _Mapping]] = ..., size: _Optional[_Union[UploadImageInput.Size, _Mapping]] = ..., variants: _Optional[_Iterable[_Union[UploadImageInput.Size, _Mapping]]] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadImageOutput(_message.Message):
    __slots__ = ["image_url"]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    image_url: str
    def __init__(self, image_url: _Optional[str] = ...) -> None: ...

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
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...
