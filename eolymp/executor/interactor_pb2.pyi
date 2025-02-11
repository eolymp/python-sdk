from eolymp.executor import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Interactor(_message.Message):
    __slots__ = ("type", "runtime", "source_url", "secret", "files")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Interactor.Type]
        PROGRAM: _ClassVar[Interactor.Type]
    NONE: Interactor.Type
    PROGRAM: Interactor.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    type: Interactor.Type
    runtime: str
    source_url: str
    secret: bool
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    def __init__(self, type: _Optional[_Union[Interactor.Type, str]] = ..., runtime: _Optional[str] = ..., source_url: _Optional[str] = ..., secret: bool = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...
