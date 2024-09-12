from eolymp.executor import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Checker(_message.Message):
    __slots__ = ["case_sensitive", "files", "order_sensitive", "precision", "runtime", "source_url", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    LEGACY_PROGRAM: Checker.Type
    LINES: Checker.Type
    NONE: Checker.Type
    ORDER_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    PROGRAM: Checker.Type
    QUERY_RESULTS: Checker.Type
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    TOKENS: Checker.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    case_sensitive: bool
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    order_sensitive: bool
    precision: int
    runtime: str
    source_url: str
    type: Checker.Type
    def __init__(self, type: _Optional[_Union[Checker.Type, str]] = ..., runtime: _Optional[str] = ..., source_url: _Optional[str] = ..., precision: _Optional[int] = ..., case_sensitive: bool = ..., order_sensitive: bool = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...
