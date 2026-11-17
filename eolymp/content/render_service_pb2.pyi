from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.ecm import node_pb2 as _node_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RenderContentInput(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: _content_pb2.Content
    def __init__(self, content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class RenderContentOutput(_message.Message):
    __slots__ = ("render",)
    RENDER_FIELD_NUMBER: _ClassVar[int]
    render: _node_pb2.Node
    def __init__(self, render: _Optional[_Union[_node_pb2.Node, _Mapping]] = ...) -> None: ...

class RenderFigureInput(_message.Message):
    __slots__ = ("typst", "format", "offset", "size")
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_FORMAT: _ClassVar[RenderFigureInput.Format]
        SVG: _ClassVar[RenderFigureInput.Format]
        PNG: _ClassVar[RenderFigureInput.Format]
    UNKNOWN_FORMAT: RenderFigureInput.Format
    SVG: RenderFigureInput.Format
    PNG: RenderFigureInput.Format
    TYPST_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    typst: str
    format: RenderFigureInput.Format
    offset: int
    size: int
    def __init__(self, typst: _Optional[str] = ..., format: _Optional[_Union[RenderFigureInput.Format, str]] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class RenderFigureOutput(_message.Message):
    __slots__ = ("pages", "diagnostics", "total")
    class Page(_message.Message):
        __slots__ = ("data", "width", "height")
        DATA_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        width: int
        height: int
        def __init__(self, data: _Optional[bytes] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    class Diagnostic(_message.Message):
        __slots__ = ("severity", "line", "column", "message", "hints")
        class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_SEVERITY: _ClassVar[RenderFigureOutput.Diagnostic.Severity]
            ERROR: _ClassVar[RenderFigureOutput.Diagnostic.Severity]
            WARNING: _ClassVar[RenderFigureOutput.Diagnostic.Severity]
        UNKNOWN_SEVERITY: RenderFigureOutput.Diagnostic.Severity
        ERROR: RenderFigureOutput.Diagnostic.Severity
        WARNING: RenderFigureOutput.Diagnostic.Severity
        SEVERITY_FIELD_NUMBER: _ClassVar[int]
        LINE_FIELD_NUMBER: _ClassVar[int]
        COLUMN_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        HINTS_FIELD_NUMBER: _ClassVar[int]
        severity: RenderFigureOutput.Diagnostic.Severity
        line: int
        column: int
        message: str
        hints: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, severity: _Optional[_Union[RenderFigureOutput.Diagnostic.Severity, str]] = ..., line: _Optional[int] = ..., column: _Optional[int] = ..., message: _Optional[str] = ..., hints: _Optional[_Iterable[str]] = ...) -> None: ...
    PAGES_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    pages: _containers.RepeatedCompositeFieldContainer[RenderFigureOutput.Page]
    diagnostics: _containers.RepeatedCompositeFieldContainer[RenderFigureOutput.Diagnostic]
    total: int
    def __init__(self, pages: _Optional[_Iterable[_Union[RenderFigureOutput.Page, _Mapping]]] = ..., diagnostics: _Optional[_Iterable[_Union[RenderFigureOutput.Diagnostic, _Mapping]]] = ..., total: _Optional[int] = ...) -> None: ...
