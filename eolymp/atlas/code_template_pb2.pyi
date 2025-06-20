from eolymp.executor import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Template(_message.Message):
    __slots__ = ("id", "runtime", "secret", "source", "header", "footer", "files")
    ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FOOTER_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    id: str
    runtime: str
    secret: bool
    source: str
    header: str
    footer: str
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    def __init__(self, id: _Optional[str] = ..., runtime: _Optional[str] = ..., secret: bool = ..., source: _Optional[str] = ..., header: _Optional[str] = ..., footer: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...
