from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Translation(_message.Message):
    __slots__ = ["approved_at", "created_at", "created_by", "id", "locale", "message", "needs_review", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: Translation.Status
    APPROVED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    NEEDS_REVIEW_FIELD_NUMBER: _ClassVar[int]
    NONE: Translation.Status
    PENDING: Translation.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNUSED: Translation.Status
    approved_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    created_by: str
    id: str
    locale: str
    message: str
    needs_review: bool
    status: Translation.Status
    def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., message: _Optional[str] = ..., status: _Optional[_Union[Translation.Status, str]] = ..., needs_review: bool = ..., created_by: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., approved_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
