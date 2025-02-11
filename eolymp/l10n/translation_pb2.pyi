from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Translation(_message.Message):
    __slots__ = ("id", "locale", "message", "status", "needs_review", "created_by", "created_at", "approved_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Translation.Status]
        PENDING: _ClassVar[Translation.Status]
        ACTIVE: _ClassVar[Translation.Status]
        UNUSED: _ClassVar[Translation.Status]
    NONE: Translation.Status
    PENDING: Translation.Status
    ACTIVE: Translation.Status
    UNUSED: Translation.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NEEDS_REVIEW_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    APPROVED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    locale: str
    message: str
    status: Translation.Status
    needs_review: bool
    created_by: str
    created_at: _timestamp_pb2.Timestamp
    approved_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., message: _Optional[str] = ..., status: _Optional[_Union[Translation.Status, str]] = ..., needs_review: bool = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., approved_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
