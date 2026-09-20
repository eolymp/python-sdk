import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Client(_message.Message):
    __slots__ = ("id", "secret", "name", "redirect_uri", "created_at", "updated_at")
    class Patch(_message.Message):
        __slots__ = ("name", "redirect_uri")
        NAME_FIELD_NUMBER: _ClassVar[int]
        REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
        name: str
        redirect_uri: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, name: _Optional[str] = ..., redirect_uri: _Optional[_Iterable[str]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    secret: str
    name: str
    redirect_uri: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., secret: _Optional[str] = ..., name: _Optional[str] = ..., redirect_uri: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
