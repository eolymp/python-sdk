from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Verifier(_message.Message):
    __slots__ = ["case_sensitive", "files", "lang", "order_sensitive", "precision", "source", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class File(_message.Message):
        __slots__ = ["path", "source_ern", "source_url"]
        PATH_FIELD_NUMBER: _ClassVar[int]
        SOURCE_ERN_FIELD_NUMBER: _ClassVar[int]
        SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
        path: str
        source_ern: str
        source_url: str
        def __init__(self, path: _Optional[str] = ..., source_ern: _Optional[str] = ..., source_url: _Optional[str] = ...) -> None: ...
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
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
    files: _containers.RepeatedCompositeFieldContainer[Verifier.File]
    lang: str
    order_sensitive: bool
    precision: int
    source: str
    type: Verifier.Type
    def __init__(self, type: _Optional[_Union[Verifier.Type, str]] = ..., lang: _Optional[str] = ..., source: _Optional[str] = ..., precision: _Optional[int] = ..., case_sensitive: bool = ..., order_sensitive: bool = ..., files: _Optional[_Iterable[_Union[Verifier.File, _Mapping]]] = ...) -> None: ...
