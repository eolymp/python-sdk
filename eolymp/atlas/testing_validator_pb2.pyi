from eolymp.executor import file_pb2 as _file_pb2
from eolymp.executor import interactor_pb2 as _interactor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Validator(_message.Message):
    __slots__ = ("runtime", "source", "secret", "files")
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    runtime: str
    source: str
    secret: bool
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    def __init__(self, runtime: _Optional[str] = ..., source: _Optional[str] = ..., secret: bool = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...
