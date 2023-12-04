from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import editorial_pb2 as _editorial_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEditorialInput(_message.Message):
    __slots__ = ["editorial"]
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    editorial: _editorial_pb2.Editorial
    def __init__(self, editorial: _Optional[_Union[_editorial_pb2.Editorial, _Mapping]] = ...) -> None: ...

class CreateEditorialOutput(_message.Message):
    __slots__ = ["editorial_id"]
    EDITORIAL_ID_FIELD_NUMBER: _ClassVar[int]
    editorial_id: str
    def __init__(self, editorial_id: _Optional[str] = ...) -> None: ...

class DeleteEditorialInput(_message.Message):
    __slots__ = ["editorial_id"]
    EDITORIAL_ID_FIELD_NUMBER: _ClassVar[int]
    editorial_id: str
    def __init__(self, editorial_id: _Optional[str] = ...) -> None: ...

class DeleteEditorialOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeEditorialInput(_message.Message):
    __slots__ = ["editorial_id", "render", "version"]
    EDITORIAL_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    editorial_id: str
    render: bool
    version: int
    def __init__(self, editorial_id: _Optional[str] = ..., render: bool = ..., version: _Optional[int] = ...) -> None: ...

class DescribeEditorialOutput(_message.Message):
    __slots__ = ["editorial"]
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    editorial: _editorial_pb2.Editorial
    def __init__(self, editorial: _Optional[_Union[_editorial_pb2.Editorial, _Mapping]] = ...) -> None: ...

class ListEditorialsInput(_message.Message):
    __slots__ = ["render", "version"]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    render: bool
    version: int
    def __init__(self, render: bool = ..., version: _Optional[int] = ...) -> None: ...

class ListEditorialsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_editorial_pb2.Editorial]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_editorial_pb2.Editorial, _Mapping]]] = ...) -> None: ...

class LookupEditorialInput(_message.Message):
    __slots__ = ["locale", "render", "version"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    locale: str
    render: bool
    version: int
    def __init__(self, locale: _Optional[str] = ..., render: bool = ..., version: _Optional[int] = ...) -> None: ...

class LookupEditorialOutput(_message.Message):
    __slots__ = ["editorial"]
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    editorial: _editorial_pb2.Editorial
    def __init__(self, editorial: _Optional[_Union[_editorial_pb2.Editorial, _Mapping]] = ...) -> None: ...

class PreviewEditorialInput(_message.Message):
    __slots__ = ["editorial"]
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    editorial: _editorial_pb2.Editorial
    def __init__(self, editorial: _Optional[_Union[_editorial_pb2.Editorial, _Mapping]] = ...) -> None: ...

class PreviewEditorialOutput(_message.Message):
    __slots__ = ["editorial"]
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    editorial: _editorial_pb2.Editorial
    def __init__(self, editorial: _Optional[_Union[_editorial_pb2.Editorial, _Mapping]] = ...) -> None: ...

class UpdateEditorialInput(_message.Message):
    __slots__ = ["editorial", "editorial_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateEditorialInput.Patch
    CONTENT: UpdateEditorialInput.Patch
    DOWNLOAD_LINK: UpdateEditorialInput.Patch
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    EDITORIAL_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE: UpdateEditorialInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    editorial: _editorial_pb2.Editorial
    editorial_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateEditorialInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateEditorialInput.Patch, str]]] = ..., editorial_id: _Optional[str] = ..., editorial: _Optional[_Union[_editorial_pb2.Editorial, _Mapping]] = ...) -> None: ...

class UpdateEditorialOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
