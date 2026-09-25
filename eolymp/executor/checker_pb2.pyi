from eolymp.executor import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Checker(_message.Message):
    __slots__ = ("type", "runtime", "source_url", "precision", "case_sensitive", "order_sensitive", "files", "tokens", "lines", "program", "query_results")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Checker.Type]
        TOKENS: _ClassVar[Checker.Type]
        LINES: _ClassVar[Checker.Type]
        PROGRAM: _ClassVar[Checker.Type]
        QUERY_RESULTS: _ClassVar[Checker.Type]
    NONE: Checker.Type
    TOKENS: Checker.Type
    LINES: Checker.Type
    PROGRAM: Checker.Type
    QUERY_RESULTS: Checker.Type
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
        __slots__ = ("mode", "runtime", "source_url", "files")
        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_MODE: _ClassVar[Checker.Program.Mode]
            EOLYMP: _ClassVar[Checker.Program.Mode]
            TESTLIB: _ClassVar[Checker.Program.Mode]
            CMS: _ClassVar[Checker.Program.Mode]
            KATTIS: _ClassVar[Checker.Program.Mode]
        UNKNOWN_MODE: Checker.Program.Mode
        EOLYMP: Checker.Program.Mode
        TESTLIB: Checker.Program.Mode
        CMS: Checker.Program.Mode
        KATTIS: Checker.Program.Mode
        MODE_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
        FILES_FIELD_NUMBER: _ClassVar[int]
        mode: Checker.Program.Mode
        runtime: str
        source_url: str
        files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
        def __init__(self, mode: _Optional[_Union[Checker.Program.Mode, str]] = ..., runtime: _Optional[str] = ..., source_url: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...
    class QueryResults(_message.Message):
        __slots__ = ("order_sensitive",)
        ORDER_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        order_sensitive: bool
        def __init__(self, order_sensitive: _Optional[bool] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    PRECISION_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    ORDER_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    PROGRAM_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    type: Checker.Type
    runtime: str
    source_url: str
    precision: int
    case_sensitive: bool
    order_sensitive: bool
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    tokens: Checker.Tokens
    lines: Checker.Lines
    program: Checker.Program
    query_results: Checker.QueryResults
    def __init__(self, type: _Optional[_Union[Checker.Type, str]] = ..., runtime: _Optional[str] = ..., source_url: _Optional[str] = ..., precision: _Optional[int] = ..., case_sensitive: _Optional[bool] = ..., order_sensitive: _Optional[bool] = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ..., tokens: _Optional[_Union[Checker.Tokens, _Mapping]] = ..., lines: _Optional[_Union[Checker.Lines, _Mapping]] = ..., program: _Optional[_Union[Checker.Program, _Mapping]] = ..., query_results: _Optional[_Union[Checker.QueryResults, _Mapping]] = ...) -> None: ...
