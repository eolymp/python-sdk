from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LinkedAccount(_message.Message):
    __slots__ = ("id", "type", "issuer", "subject")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TYPE: _ClassVar[LinkedAccount.Type]
        GOOGLE: _ClassVar[LinkedAccount.Type]
    UNKNOWN_TYPE: LinkedAccount.Type
    GOOGLE: LinkedAccount.Type
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: LinkedAccount.Type
    issuer: str
    subject: str
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[LinkedAccount.Type, str]] = ..., issuer: _Optional[str] = ..., subject: _Optional[str] = ...) -> None: ...
