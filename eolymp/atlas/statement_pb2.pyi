from eolymp.ecm import node_pb2 as _node_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Statement(_message.Message):
    __slots__ = ["author", "content_ecm", "content_html", "content_latex", "content_markdown", "content_raw", "content_rich", "download_link", "format", "id", "locale", "problem_id", "source", "title"]
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ECM_FIELD_NUMBER: _ClassVar[int]
    CONTENT_HTML_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LATEX_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MARKDOWN_FIELD_NUMBER: _ClassVar[int]
    CONTENT_RAW_FIELD_NUMBER: _ClassVar[int]
    CONTENT_RICH_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    HTML: Statement.Format
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MARKDOWN: Statement.Format
    NONE: Statement.Format
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RICH: Statement.Format
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TEX: Statement.Format
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    content_ecm: _node_pb2.Node
    content_html: str
    content_latex: str
    content_markdown: str
    content_raw: str
    content_rich: _node_pb2.Node
    download_link: str
    format: Statement.Format
    id: str
    locale: str
    problem_id: str
    source: str
    title: str
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., locale: _Optional[str] = ..., title: _Optional[str] = ..., content_html: _Optional[str] = ..., content_latex: _Optional[str] = ..., content_markdown: _Optional[str] = ..., content_ecm: _Optional[_Union[_node_pb2.Node, _Mapping]] = ..., content_raw: _Optional[str] = ..., content_rich: _Optional[_Union[_node_pb2.Node, _Mapping]] = ..., download_link: _Optional[str] = ..., format: _Optional[_Union[Statement.Format, str]] = ..., author: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...
