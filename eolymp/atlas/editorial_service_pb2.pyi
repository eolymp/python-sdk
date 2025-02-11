from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import editorial_pb2 as _editorial_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListEditorialsInput(_message.Message):
    __slots__ = ("offset", "size", "version", "render", "extra")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    version: int
    render: bool
    extra: _containers.RepeatedScalarFieldContainer[_editorial_pb2.Editorial.Extra]
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., version: _Optional[int] = ..., render: bool = ..., extra: _Optional[_Iterable[_Union[_editorial_pb2.Editorial.Extra, str]]] = ...) -> None: ...

class ListEditorialsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_editorial_pb2.Editorial]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_editorial_pb2.Editorial, _Mapping]]] = ...) -> None: ...

class DescribeEditorialInput(_message.Message):
    __slots__ = ("editorial_id", "version", "render", "extra")
    EDITORIAL_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    editorial_id: str
    version: int
    render: bool
    extra: _containers.RepeatedScalarFieldContainer[_editorial_pb2.Editorial.Extra]
    def __init__(self, editorial_id: _Optional[str] = ..., version: _Optional[int] = ..., render: bool = ..., extra: _Optional[_Iterable[_Union[_editorial_pb2.Editorial.Extra, str]]] = ...) -> None: ...

class DescribeEditorialOutput(_message.Message):
    __slots__ = ("editorial",)
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    editorial: _editorial_pb2.Editorial
    def __init__(self, editorial: _Optional[_Union[_editorial_pb2.Editorial, _Mapping]] = ...) -> None: ...

class LookupEditorialInput(_message.Message):
    __slots__ = ("locale", "version", "render", "extra")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    locale: str
    version: int
    render: bool
    extra: _containers.RepeatedScalarFieldContainer[_editorial_pb2.Editorial.Extra]
    def __init__(self, locale: _Optional[str] = ..., version: _Optional[int] = ..., render: bool = ..., extra: _Optional[_Iterable[_Union[_editorial_pb2.Editorial.Extra, str]]] = ...) -> None: ...

class LookupEditorialOutput(_message.Message):
    __slots__ = ("editorial",)
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    editorial: _editorial_pb2.Editorial
    def __init__(self, editorial: _Optional[_Union[_editorial_pb2.Editorial, _Mapping]] = ...) -> None: ...

class PreviewEditorialInput(_message.Message):
    __slots__ = ("editorial",)
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    editorial: _editorial_pb2.Editorial
    def __init__(self, editorial: _Optional[_Union[_editorial_pb2.Editorial, _Mapping]] = ...) -> None: ...

class PreviewEditorialOutput(_message.Message):
    __slots__ = ("editorial",)
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    editorial: _editorial_pb2.Editorial
    def __init__(self, editorial: _Optional[_Union[_editorial_pb2.Editorial, _Mapping]] = ...) -> None: ...

class CreateEditorialInput(_message.Message):
    __slots__ = ("editorial",)
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    editorial: _editorial_pb2.Editorial
    def __init__(self, editorial: _Optional[_Union[_editorial_pb2.Editorial, _Mapping]] = ...) -> None: ...

class CreateEditorialOutput(_message.Message):
    __slots__ = ("editorial_id",)
    EDITORIAL_ID_FIELD_NUMBER: _ClassVar[int]
    editorial_id: str
    def __init__(self, editorial_id: _Optional[str] = ...) -> None: ...

class UpdateEditorialInput(_message.Message):
    __slots__ = ("patch", "editorial_id", "editorial")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    EDITORIAL_ID_FIELD_NUMBER: _ClassVar[int]
    EDITORIAL_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_editorial_pb2.Editorial.Patch]
    editorial_id: str
    editorial: _editorial_pb2.Editorial
    def __init__(self, patch: _Optional[_Iterable[_Union[_editorial_pb2.Editorial.Patch, str]]] = ..., editorial_id: _Optional[str] = ..., editorial: _Optional[_Union[_editorial_pb2.Editorial, _Mapping]] = ...) -> None: ...

class UpdateEditorialOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteEditorialInput(_message.Message):
    __slots__ = ("editorial_id",)
    EDITORIAL_ID_FIELD_NUMBER: _ClassVar[int]
    editorial_id: str
    def __init__(self, editorial_id: _Optional[str] = ...) -> None: ...

class DeleteEditorialOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TranslateEditorialsInput(_message.Message):
    __slots__ = ("source", "target", "target_automatic", "override_manual")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    TARGET_AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_MANUAL_FIELD_NUMBER: _ClassVar[int]
    source: str
    target: _containers.RepeatedScalarFieldContainer[str]
    target_automatic: bool
    override_manual: bool
    def __init__(self, source: _Optional[str] = ..., target: _Optional[_Iterable[str]] = ..., target_automatic: bool = ..., override_manual: bool = ...) -> None: ...

class TranslateEditorialsOutput(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...
