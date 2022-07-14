from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Verifier(_message.Message):
    __slots__ = ["case_sensitive", "lang", "order_sensitive", "precision", "source", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    LANG_FIELD_NUMBER: _ClassVar[int]
    LEGACY_PROGRAM: Verifier.Type
    LINES: Verifier.Type
    NONE: Verifier.Type
    ORDER_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    PROGRAM: Verifier.Type
    QUERY_RESULTS: Verifier.Type
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TOKENS: Verifier.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    case_sensitive: bool
    lang: str
    order_sensitive: bool
    precision: int
    source: str
    type: Verifier.Type
    def __init__(self, type: _Optional[_Union[Verifier.Type, str]] = ..., lang: _Optional[str] = ..., source: _Optional[str] = ..., precision: _Optional[int] = ..., case_sensitive: bool = ..., order_sensitive: bool = ...) -> None: ...
