from eolymp.ecm import node_pb2 as _node_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Editorial(_message.Message):
    __slots__ = ["content_ecm", "content_html", "content_latex", "content_markdown", "download_link", "id", "locale", "problem_id"]
    CONTENT_ECM_FIELD_NUMBER: _ClassVar[int]
    CONTENT_HTML_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LATEX_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MARKDOWN_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    content_ecm: _node_pb2.Node
    content_html: str
    content_latex: str
    content_markdown: str
    download_link: str
    id: str
    locale: str
    problem_id: str
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., locale: _Optional[str] = ..., content_html: _Optional[str] = ..., content_latex: _Optional[str] = ..., content_markdown: _Optional[str] = ..., content_ecm: _Optional[_Union[_node_pb2.Node, _Mapping]] = ..., download_link: _Optional[str] = ...) -> None: ...
