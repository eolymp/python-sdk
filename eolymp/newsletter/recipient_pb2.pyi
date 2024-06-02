from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Recipient(_message.Message):
    __slots__ = ["created_at", "delivered_at", "id", "member_id", "sent_at", "status", "updated_at"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BOUNCED: Recipient.Status
    CREATED: Recipient.Status
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DELIVERED: Recipient.Status
    DELIVERED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PENDING: Recipient.Status
    SENT: Recipient.Status
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STATUS: Recipient.Status
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    delivered_at: _timestamp_pb2.Timestamp
    id: str
    member_id: str
    sent_at: _timestamp_pb2.Timestamp
    status: Recipient.Status
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., sent_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., delivered_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., member_id: _Optional[str] = ..., status: _Optional[_Union[Recipient.Status, str]] = ...) -> None: ...
