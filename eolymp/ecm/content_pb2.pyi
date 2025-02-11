from eolymp.ecm import node_pb2 as _node_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Content(_message.Message):
    __slots__ = ("html", "latex", "markdown", "ecm", "render")
    HTML_FIELD_NUMBER: _ClassVar[int]
    LATEX_FIELD_NUMBER: _ClassVar[int]
    MARKDOWN_FIELD_NUMBER: _ClassVar[int]
    ECM_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    html: str
    latex: str
    markdown: str
    ecm: _node_pb2.Node
    render: _node_pb2.Node
    def __init__(self, html: _Optional[str] = ..., latex: _Optional[str] = ..., markdown: _Optional[str] = ..., ecm: _Optional[_Union[_node_pb2.Node, _Mapping]] = ..., render: _Optional[_Union[_node_pb2.Node, _Mapping]] = ...) -> None: ...
