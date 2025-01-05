from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.ecm import node_pb2 as _node_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrintContentInput(_message.Message):
    __slots__ = ["single_page", "header_path", "footer_path", "print_background", "paper_width", "paper_height", "margins", "landscape", "content"]
    SINGLE_PAGE_FIELD_NUMBER: _ClassVar[int]
    HEADER_PATH_FIELD_NUMBER: _ClassVar[int]
    FOOTER_PATH_FIELD_NUMBER: _ClassVar[int]
    PRINT_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    PAPER_WIDTH_FIELD_NUMBER: _ClassVar[int]
    PAPER_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MARGINS_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    single_page: bool
    header_path: str
    footer_path: str
    print_background: bool
    paper_width: int
    paper_height: int
    margins: _containers.RepeatedScalarFieldContainer[int]
    landscape: bool
    content: _content_pb2.Content
    def __init__(self, single_page: bool = ..., header_path: _Optional[str] = ..., footer_path: _Optional[str] = ..., print_background: bool = ..., paper_width: _Optional[int] = ..., paper_height: _Optional[int] = ..., margins: _Optional[_Iterable[int]] = ..., landscape: bool = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class PrintContentOutput(_message.Message):
    __slots__ = ["document_url"]
    DOCUMENT_URL_FIELD_NUMBER: _ClassVar[int]
    document_url: str
    def __init__(self, document_url: _Optional[str] = ...) -> None: ...
