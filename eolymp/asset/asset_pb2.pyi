from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UploadImageInput(_message.Message):
    __slots__ = ["crop", "data", "mime", "name", "sizes"]
    class Crop(_message.Message):
        __slots__ = ["height", "left", "top", "width"]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        LEFT_FIELD_NUMBER: _ClassVar[int]
        TOP_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        height: int
        left: int
        top: int
        width: int
        def __init__(self, top: _Optional[int] = ..., left: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    class Size(_message.Message):
        __slots__ = ["height", "width"]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        height: int
        width: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    CROP_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    MIME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZES_FIELD_NUMBER: _ClassVar[int]
    crop: UploadImageInput.Crop
    data: bytes
    mime: str
    name: str
    sizes: _containers.RepeatedCompositeFieldContainer[UploadImageInput.Size]
    def __init__(self, name: _Optional[str] = ..., mime: _Optional[str] = ..., crop: _Optional[_Union[UploadImageInput.Crop, _Mapping]] = ..., sizes: _Optional[_Iterable[_Union[UploadImageInput.Size, _Mapping]]] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadImageOutput(_message.Message):
    __slots__ = ["image_url"]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    image_url: str
    def __init__(self, image_url: _Optional[str] = ...) -> None: ...
