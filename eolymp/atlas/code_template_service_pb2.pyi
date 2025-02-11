from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import code_template_pb2 as _code_template_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCodeTemplateInput(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _code_template_pb2.Template
    def __init__(self, template: _Optional[_Union[_code_template_pb2.Template, _Mapping]] = ...) -> None: ...

class CreateCodeTemplateOutput(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class UpdateCodeTemplateInput(_message.Message):
    __slots__ = ("template_id", "template")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateCodeTemplateInput.Patch]
        RUNTIME: _ClassVar[UpdateCodeTemplateInput.Patch]
        SOURCE: _ClassVar[UpdateCodeTemplateInput.Patch]
        HEADER: _ClassVar[UpdateCodeTemplateInput.Patch]
        FOOTER: _ClassVar[UpdateCodeTemplateInput.Patch]
        SECRET: _ClassVar[UpdateCodeTemplateInput.Patch]
        FILES: _ClassVar[UpdateCodeTemplateInput.Patch]
    ALL: UpdateCodeTemplateInput.Patch
    RUNTIME: UpdateCodeTemplateInput.Patch
    SOURCE: UpdateCodeTemplateInput.Patch
    HEADER: UpdateCodeTemplateInput.Patch
    FOOTER: UpdateCodeTemplateInput.Patch
    SECRET: UpdateCodeTemplateInput.Patch
    FILES: UpdateCodeTemplateInput.Patch
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    template: _code_template_pb2.Template
    def __init__(self, template_id: _Optional[str] = ..., template: _Optional[_Union[_code_template_pb2.Template, _Mapping]] = ...) -> None: ...

class UpdateCodeTemplateOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteCodeTemplateInput(_message.Message):
    __slots__ = ("template_id",)
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    def __init__(self, template_id: _Optional[str] = ...) -> None: ...

class DeleteCodeTemplateOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCodeTemplatesInput(_message.Message):
    __slots__ = ("offset", "size", "version")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    version: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...

class ListCodeTemplatesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_code_template_pb2.Template]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_code_template_pb2.Template, _Mapping]]] = ...) -> None: ...

class DescribeCodeTemplateInput(_message.Message):
    __slots__ = ("template_id", "version")
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    version: int
    def __init__(self, template_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DescribeCodeTemplateOutput(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _code_template_pb2.Template
    def __init__(self, template: _Optional[_Union[_code_template_pb2.Template, _Mapping]] = ...) -> None: ...

class LookupCodeTemplateInput(_message.Message):
    __slots__ = ("runtime",)
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    runtime: str
    def __init__(self, runtime: _Optional[str] = ...) -> None: ...

class LookupCodeTemplateOutput(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _code_template_pb2.Template
    def __init__(self, template: _Optional[_Union[_code_template_pb2.Template, _Mapping]] = ...) -> None: ...
