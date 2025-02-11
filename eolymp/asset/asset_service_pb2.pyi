from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadImageInput(_message.Message):
    __slots__ = ("name", "type", "crop", "size", "variants", "data")
    class Size(_message.Message):
        __slots__ = ("width", "height")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    class Crop(_message.Message):
        __slots__ = ("top", "right", "bottom", "left")
        TOP_FIELD_NUMBER: _ClassVar[int]
        RIGHT_FIELD_NUMBER: _ClassVar[int]
        BOTTOM_FIELD_NUMBER: _ClassVar[int]
        LEFT_FIELD_NUMBER: _ClassVar[int]
        top: int
        right: int
        bottom: int
        left: int
        def __init__(self, top: _Optional[int] = ..., right: _Optional[int] = ..., bottom: _Optional[int] = ..., left: _Optional[int] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CROP_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    crop: UploadImageInput.Crop
    size: UploadImageInput.Size
    variants: _containers.RepeatedCompositeFieldContainer[UploadImageInput.Size]
    data: bytes
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., crop: _Optional[_Union[UploadImageInput.Crop, _Mapping]] = ..., size: _Optional[_Union[UploadImageInput.Size, _Mapping]] = ..., variants: _Optional[_Iterable[_Union[UploadImageInput.Size, _Mapping]]] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadImageOutput(_message.Message):
    __slots__ = ("image_url",)
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    image_url: str
    def __init__(self, image_url: _Optional[str] = ...) -> None: ...

class UploadFileInput(_message.Message):
    __slots__ = ("name", "type", "data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    data: bytes
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadFileOutput(_message.Message):
    __slots__ = ("file_url",)
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    file_url: str
    def __init__(self, file_url: _Optional[str] = ...) -> None: ...

class UploadAssetInput(_message.Message):
    __slots__ = ("name", "type", "keys", "ttl", "data")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    keys: _containers.RepeatedScalarFieldContainer[str]
    ttl: int
    data: bytes
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., keys: _Optional[_Iterable[str]] = ..., ttl: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadAssetOutput(_message.Message):
    __slots__ = ("asset_url",)
    ASSET_URL_FIELD_NUMBER: _ClassVar[int]
    asset_url: str
    def __init__(self, asset_url: _Optional[str] = ...) -> None: ...

class LookupAssetInput(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class LookupAssetOutput(_message.Message):
    __slots__ = ("asset_url",)
    ASSET_URL_FIELD_NUMBER: _ClassVar[int]
    asset_url: str
    def __init__(self, asset_url: _Optional[str] = ...) -> None: ...

class StartMultipartUploadInput(_message.Message):
    __slots__ = ("name", "type", "keys", "ttl")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KEYS_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    keys: _containers.RepeatedScalarFieldContainer[str]
    ttl: int
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., keys: _Optional[_Iterable[str]] = ..., ttl: _Optional[int] = ...) -> None: ...

class StartMultipartUploadOutput(_message.Message):
    __slots__ = ("upload_id",)
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ...) -> None: ...

class UploadPartInput(_message.Message):
    __slots__ = ("upload_id", "part_number", "data")
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    part_number: int
    data: bytes
    def __init__(self, upload_id: _Optional[str] = ..., part_number: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadPartOutput(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class CompleteMultipartUploadInput(_message.Message):
    __slots__ = ("upload_id", "parts")
    class Part(_message.Message):
        __slots__ = ("number", "token", "checksum_md5", "checksum_sha1", "checksum_sha256")
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_MD5_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_SHA1_FIELD_NUMBER: _ClassVar[int]
        CHECKSUM_SHA256_FIELD_NUMBER: _ClassVar[int]
        number: int
        token: str
        checksum_md5: str
        checksum_sha1: str
        checksum_sha256: str
        def __init__(self, number: _Optional[int] = ..., token: _Optional[str] = ..., checksum_md5: _Optional[str] = ..., checksum_sha1: _Optional[str] = ..., checksum_sha256: _Optional[str] = ...) -> None: ...
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    PARTS_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    parts: _containers.RepeatedCompositeFieldContainer[CompleteMultipartUploadInput.Part]
    def __init__(self, upload_id: _Optional[str] = ..., parts: _Optional[_Iterable[_Union[CompleteMultipartUploadInput.Part, _Mapping]]] = ...) -> None: ...

class CompleteMultipartUploadOutput(_message.Message):
    __slots__ = ("asset_url",)
    ASSET_URL_FIELD_NUMBER: _ClassVar[int]
    asset_url: str
    def __init__(self, asset_url: _Optional[str] = ...) -> None: ...

class StartStreamInput(_message.Message):
    __slots__ = ("name", "type", "ttl")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    ttl: int
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., ttl: _Optional[int] = ...) -> None: ...

class StartStreamOutput(_message.Message):
    __slots__ = ("stream_id", "stream_url")
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_URL_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    stream_url: str
    def __init__(self, stream_id: _Optional[str] = ..., stream_url: _Optional[str] = ...) -> None: ...

class AppendStreamInput(_message.Message):
    __slots__ = ("stream_id", "offset", "data")
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    offset: int
    data: bytes
    def __init__(self, stream_id: _Optional[str] = ..., offset: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class AppendStreamOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CloseStreamInput(_message.Message):
    __slots__ = ("stream_id",)
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    def __init__(self, stream_id: _Optional[str] = ...) -> None: ...

class CloseStreamOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
