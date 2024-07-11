from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Rating(_message.Message):
    __slots__ = ["contest_id", "id", "level", "member_id", "timestamp", "value"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    id: str
    level: int
    member_id: str
    timestamp: _timestamp_pb2.Timestamp
    value: int
    def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., member_id: _Optional[str] = ..., contest_id: _Optional[str] = ..., value: _Optional[int] = ..., level: _Optional[int] = ...) -> None: ...
