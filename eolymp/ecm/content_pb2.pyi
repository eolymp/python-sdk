from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.ecm import node_pb2 as _node_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Content(_message.Message):
    __slots__ = ("html", "latex", "markdown", "render")
    HTML_FIELD_NUMBER: _ClassVar[int]
    LATEX_FIELD_NUMBER: _ClassVar[int]
    MARKDOWN_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    html: str
    latex: str
    markdown: str
    render: _node_pb2.Node
    def __init__(self, html: _Optional[str] = ..., latex: _Optional[str] = ..., markdown: _Optional[str] = ..., render: _Optional[_Union[_node_pb2.Node, _Mapping]] = ...) -> None: ...
