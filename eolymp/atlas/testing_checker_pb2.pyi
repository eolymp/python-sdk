from eolymp.executor import checker_pb2 as _checker_pb2
from eolymp.executor import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Checker(_message.Message):
    __slots__ = ("version_id", "secret", "type", "runtime", "source", "files", "precision", "case_sensitive", "order_sensitive")
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    ORDER_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    secret: bool
    type: _checker_pb2.Checker.Type
    runtime: str
    source: str
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    precision: int
    case_sensitive: bool
    order_sensitive: bool
    def __init__(self, version_id: _Optional[str] = ..., secret: bool = ..., type: _Optional[_Union[_checker_pb2.Checker.Type, str]] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ..., precision: _Optional[int] = ..., case_sensitive: bool = ..., order_sensitive: bool = ...) -> None: ...
