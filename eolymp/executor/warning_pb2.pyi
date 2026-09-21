from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Warning(_message.Message):
    __slots__ = ("source", "file", "line", "column", "message", "severity")
    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_SEVERITY: _ClassVar[Warning.Severity]
        INFO: _ClassVar[Warning.Severity]
        WARNING: _ClassVar[Warning.Severity]
    UNKNOWN_SEVERITY: Warning.Severity
    INFO: Warning.Severity
    WARNING: Warning.Severity
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    source: str
    file: str
    line: int
    column: int
    message: str
    severity: Warning.Severity
    def __init__(self, source: _Optional[str] = ..., file: _Optional[str] = ..., line: _Optional[int] = ..., column: _Optional[int] = ..., message: _Optional[str] = ..., severity: _Optional[_Union[Warning.Severity, str]] = ...) -> None: ...
