from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Penalty(_message.Message):
    __slots__ = ["cancelled_at", "created_at", "description", "expires_at", "id", "scope", "summary"]
    CANCELLED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    cancelled_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    description: str
    expires_at: _timestamp_pb2.Timestamp
    id: str
    scope: _containers.RepeatedScalarFieldContainer[str]
    summary: str
    def __init__(self, id: _Optional[str] = ..., summary: _Optional[str] = ..., description: _Optional[str] = ..., scope: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancelled_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
