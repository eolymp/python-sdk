from eolymp.executor import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Checker(_message.Message):
    __slots__ = ("type", "runtime", "source_url", "precision", "case_sensitive", "order_sensitive", "files")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Checker.Type]
        TOKENS: _ClassVar[Checker.Type]
        LINES: _ClassVar[Checker.Type]
        PROGRAM: _ClassVar[Checker.Type]
        LEGACY_PROGRAM: _ClassVar[Checker.Type]
        QUERY_RESULTS: _ClassVar[Checker.Type]
    NONE: Checker.Type
    TOKENS: Checker.Type
    LINES: Checker.Type
    PROGRAM: Checker.Type
    LEGACY_PROGRAM: Checker.Type
    QUERY_RESULTS: Checker.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    ORDER_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    type: Checker.Type
    runtime: str
    source_url: str
    precision: int
    case_sensitive: bool
    order_sensitive: bool
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    def __init__(self, type: _Optional[_Union[Checker.Type, str]] = ..., runtime: _Optional[str] = ..., source_url: _Optional[str] = ..., precision: _Optional[int] = ..., case_sensitive: bool = ..., order_sensitive: bool = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...
