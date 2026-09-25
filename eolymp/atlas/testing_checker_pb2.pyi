from eolymp.executor import checker_pb2 as _checker_pb2
from eolymp.executor import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Checker(_message.Message):
    __slots__ = ("version_id", "secret", "type", "runtime", "source", "files", "precision", "case_sensitive", "order_sensitive", "tokens", "lines", "program", "query_results")
    class Tokens(_message.Message):
        __slots__ = ("precision", "case_sensitive")
        PRECISION_FIELD_NUMBER: _ClassVar[int]
        CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        precision: int
        case_sensitive: bool
        def __init__(self, precision: _Optional[int] = ..., case_sensitive: _Optional[bool] = ...) -> None: ...
    class Lines(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Program(_message.Message):
        __slots__ = ("mode", "runtime", "source", "files")
        MODE_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        FILES_FIELD_NUMBER: _ClassVar[int]
        mode: _checker_pb2.Checker.Program.Mode
        runtime: str
        source: str
        files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
        def __init__(self, mode: _Optional[_Union[_checker_pb2.Checker.Program.Mode, str]] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...
    class QueryResults(_message.Message):
        __slots__ = ("order_sensitive",)
        ORDER_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        order_sensitive: bool
        def __init__(self, order_sensitive: _Optional[bool] = ...) -> None: ...
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    ORDER_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    version_id: str
    secret: bool
    type: _checker_pb2.Checker.Type
    runtime: str
    source: str
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    precision: int
    case_sensitive: bool
    order_sensitive: bool
    tokens: Checker.Tokens
    lines: Checker.Lines
    program: Checker.Program
    query_results: Checker.QueryResults
    def __init__(self, version_id: _Optional[str] = ..., secret: _Optional[bool] = ..., type: _Optional[_Union[_checker_pb2.Checker.Type, str]] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ..., precision: _Optional[int] = ..., case_sensitive: _Optional[bool] = ..., order_sensitive: _Optional[bool] = ..., tokens: _Optional[_Union[Checker.Tokens, _Mapping]] = ..., lines: _Optional[_Union[Checker.Lines, _Mapping]] = ..., program: _Optional[_Union[Checker.Program, _Mapping]] = ..., query_results: _Optional[_Union[Checker.QueryResults, _Mapping]] = ...) -> None: ...
