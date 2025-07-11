from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AutoReply(_message.Message):
    __slots__ = ("id", "locale", "name", "message", "labels")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    id: str
    locale: str
    name: str
    message: _content_pb2.Content
    labels: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., name: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...
