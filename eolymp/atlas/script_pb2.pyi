from eolymp.executor import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Script(_message.Message):
    __slots__ = ["files", "id", "name", "runtime", "secret", "source"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    FILES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NO_EXTRA: Script.Extra
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    SOURCE: Script.Extra
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    id: str
    name: str
    runtime: str
    secret: bool
    source: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., secret: bool = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...
