import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Version(_message.Message):
    __slots__ = ("id", "number", "created_at", "created_by", "summary", "changes", "cursor")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_OPERATION: _ClassVar[Version.Operation]
        ADD: _ClassVar[Version.Operation]
        UPDATE: _ClassVar[Version.Operation]
        DELETE: _ClassVar[Version.Operation]
    UNKNOWN_OPERATION: Version.Operation
    ADD: Version.Operation
    UPDATE: Version.Operation
    DELETE: Version.Operation
    class Change(_message.Message):
        __slots__ = ("op", "path")
        OP_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        op: Version.Operation
        path: str
        def __init__(self, op: _Optional[_Union[Version.Operation, str]] = ..., path: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    number: int
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    summary: str
    changes: _containers.RepeatedCompositeFieldContainer[Version.Change]
    cursor: str
    def __init__(self, id: _Optional[str] = ..., number: _Optional[int] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., summary: _Optional[str] = ..., changes: _Optional[_Iterable[_Union[Version.Change, _Mapping]]] = ..., cursor: _Optional[str] = ...) -> None: ...
