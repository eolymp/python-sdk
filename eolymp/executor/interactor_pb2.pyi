from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Interactor(_message.Message):
    __slots__ = ["files", "lang", "source", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class File(_message.Message):
        __slots__ = ["path", "source_ern"]
        PATH_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ERN_FIELD_NUMBER: _ClassVar[int]
        path: str
        source_ern: str
        def __init__(self, path: _Optional[str] = ..., source_ern: _Optional[str] = ...) -> None: ...
    FILES_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    NONE: Interactor.Type
    PROGRAM: Interactor.Type
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[Interactor.File]
    lang: str
    source: str
    type: Interactor.Type
    def __init__(self, type: _Optional[_Union[Interactor.Type, str]] = ..., lang: _Optional[str] = ..., source: _Optional[str] = ..., files: _Optional[_Iterable[_Union[Interactor.File, _Mapping]]] = ...) -> None: ...
