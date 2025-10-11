from eolymp.executor import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Script(_message.Message):
    __slots__ = ("id", "name", "secret", "runtime", "source", "files")
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_EXTRA: _ClassVar[Script.Extra.Field]
            SOURCE: _ClassVar[Script.Extra.Field]
        UNKNOWN_EXTRA: Script.Extra.Field
        SOURCE: Script.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_PATCH: _ClassVar[Script.Patch.Field]
            NAME: _ClassVar[Script.Patch.Field]
            SECRET: _ClassVar[Script.Patch.Field]
            RUNTIME: _ClassVar[Script.Patch.Field]
            SOURCE_URL: _ClassVar[Script.Patch.Field]
            FILES: _ClassVar[Script.Patch.Field]
        UNKNOWN_PATCH: Script.Patch.Field
        NAME: Script.Patch.Field
        SECRET: Script.Patch.Field
        RUNTIME: Script.Patch.Field
        SOURCE_URL: Script.Patch.Field
        FILES: Script.Patch.Field
        def __init__(self) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    secret: bool
    runtime: str
    source: str
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., secret: bool = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...
