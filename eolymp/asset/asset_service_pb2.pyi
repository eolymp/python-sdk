from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
