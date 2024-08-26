from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Script(_message.Message):
    __slots__ = ["files", "name", "runtime", "source_url"]
    class File(_message.Message):
        __slots__ = ["path", "source_url"]
        PATH_FIELD_NUMBER: _ClassVar[int]
        SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
        path: str
        source_url: str
        def __init__(self, path: _Optional[str] = ..., source_url: _Optional[str] = ...) -> None: ...
    FILES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[Script.File]
    name: str
    runtime: str
    source_url: str
    def __init__(self, name: _Optional[str] = ..., runtime: _Optional[str] = ..., source_url: _Optional[str] = ..., files: _Optional[_Iterable[_Union[Script.File, _Mapping]]] = ...) -> None: ...
