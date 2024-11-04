from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Language(_message.Message):
    __slots__ = ["deprecated", "id", "name", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OTHER: Language.Type
    PROGRAMMING: Language.Type
    SQL: Language.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_TYPE: Language.Type
    deprecated: bool
    id: str
    name: str
    type: Language.Type
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[Language.Type, str]] = ..., deprecated: bool = ...) -> None: ...
