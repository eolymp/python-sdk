from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Language(_message.Message):
    __slots__ = ("id", "name", "type", "deprecated")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TYPE: _ClassVar[Language.Type]
        PROGRAMMING: _ClassVar[Language.Type]
        SQL: _ClassVar[Language.Type]
        ML: _ClassVar[Language.Type]
        OTHER: _ClassVar[Language.Type]
    UNKNOWN_TYPE: Language.Type
    PROGRAMMING: Language.Type
    SQL: Language.Type
    ML: Language.Type
    OTHER: Language.Type
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEPRECATED_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: Language.Type
    deprecated: bool
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[Language.Type, str]] = ..., deprecated: bool = ...) -> None: ...
