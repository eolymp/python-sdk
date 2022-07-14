from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Interactor(_message.Message):
    __slots__ = ["lang", "source", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    LANG_FIELD_NUMBER: _ClassVar[int]
    NONE: Interactor.Type
    PROGRAM: Interactor.Type
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    lang: str
    source: str
    type: Interactor.Type
    def __init__(self, type: _Optional[_Union[Interactor.Type, str]] = ..., lang: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...
