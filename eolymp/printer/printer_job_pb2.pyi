from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Job(_message.Message):
    __slots__ = ("id", "status", "user_id", "member_id", "document_url", "created_at", "updated_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Job.Status]
        PENDING: _ClassVar[Job.Status]
        PRINTING: _ClassVar[Job.Status]
        COMPLETE: _ClassVar[Job.Status]
        ERROR: _ClassVar[Job.Status]
        CANCELLED: _ClassVar[Job.Status]
    UNKNOWN_STATUS: Job.Status
    PENDING: Job.Status
    PRINTING: Job.Status
    COMPLETE: Job.Status
    ERROR: Job.Status
    CANCELLED: Job.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: Job.Status
    user_id: str
    member_id: str
    document_url: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[Job.Status, str]] = ..., user_id: _Optional[str] = ..., member_id: _Optional[str] = ..., document_url: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
