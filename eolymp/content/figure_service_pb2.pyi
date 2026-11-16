from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.content import figure_pb2 as _figure_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestFiguresInput(_message.Message):
    __slots__ = ("request", "context", "figures", "thread_id")
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FIGURES_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    request: str
    context: str
    figures: _containers.RepeatedCompositeFieldContainer[_figure_pb2.Figure]
    thread_id: str
    def __init__(self, request: _Optional[str] = ..., context: _Optional[str] = ..., figures: _Optional[_Iterable[_Union[_figure_pb2.Figure, _Mapping]]] = ..., thread_id: _Optional[str] = ...) -> None: ...

class RequestFiguresOutput(_message.Message):
    __slots__ = ("reply", "figures", "thread_id")
    REPLY_FIELD_NUMBER: _ClassVar[int]
    FIGURES_FIELD_NUMBER: _ClassVar[int]
    THREAD_ID_FIELD_NUMBER: _ClassVar[int]
    reply: str
    figures: _containers.RepeatedCompositeFieldContainer[_figure_pb2.Figure]
    thread_id: str
    def __init__(self, reply: _Optional[str] = ..., figures: _Optional[_Iterable[_Union[_figure_pb2.Figure, _Mapping]]] = ..., thread_id: _Optional[str] = ...) -> None: ...
