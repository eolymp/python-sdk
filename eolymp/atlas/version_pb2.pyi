from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Version(_message.Message):
    __slots__ = ("id", "number", "created_at", "created_by", "change_op", "change_path", "cursor")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CHANGE_OP_FIELD_NUMBER: _ClassVar[int]
    CHANGE_PATH_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    number: int
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    change_op: str
    change_path: str
    cursor: str
    def __init__(self, id: _Optional[str] = ..., number: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., change_op: _Optional[str] = ..., change_path: _Optional[str] = ..., cursor: _Optional[str] = ...) -> None: ...
