from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Penalty(_message.Message):
    __slots__ = ("id", "summary", "description", "scope", "created_at", "expires_at", "cancelled_at")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTRA: _ClassVar[Penalty.Extra]
        DESCRIPTION_VALUE: _ClassVar[Penalty.Extra]
        DESCRIPTION_RENDER: _ClassVar[Penalty.Extra]
    NO_EXTRA: Penalty.Extra
    DESCRIPTION_VALUE: Penalty.Extra
    DESCRIPTION_RENDER: Penalty.Extra
    ID_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    summary: str
    description: _content_pb2.Content
    scope: _containers.RepeatedScalarFieldContainer[str]
    created_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    cancelled_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., summary: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., scope: _Optional[_Iterable[str]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancelled_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
