from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.ecm import node_pb2 as _node_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RenderContentInput(_message.Message):
    __slots__ = ["content"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: _content_pb2.Content
    def __init__(self, content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...

class RenderContentOutput(_message.Message):
    __slots__ = ["render"]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    render: _node_pb2.Node
    def __init__(self, render: _Optional[_Union[_node_pb2.Node, _Mapping]] = ...) -> None: ...
