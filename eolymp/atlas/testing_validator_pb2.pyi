from eolymp.executor import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Validator(_message.Message):
    __slots__ = ("version_id", "secret", "runtime", "source", "files")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    secret: bool
    runtime: str
    source: str
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    def __init__(self, version_id: _Optional[str] = ..., secret: bool = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...
