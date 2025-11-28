import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Recipient(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "sent_at", "delivered_at", "member_id", "status", "status_reason", "parameters")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Recipient.Status]
        CREATED: _ClassVar[Recipient.Status]
        PENDING: _ClassVar[Recipient.Status]
        SENT: _ClassVar[Recipient.Status]
        DELIVERED: _ClassVar[Recipient.Status]
        BOUNCED: _ClassVar[Recipient.Status]
        SKIPPED: _ClassVar[Recipient.Status]
        ERROR: _ClassVar[Recipient.Status]
    UNKNOWN_STATUS: Recipient.Status
    CREATED: Recipient.Status
    PENDING: Recipient.Status
    SENT: Recipient.Status
    DELIVERED: Recipient.Status
    BOUNCED: Recipient.Status
    SKIPPED: Recipient.Status
    ERROR: Recipient.Status
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    SENT_AT_FIELD_NUMBER: _ClassVar[int]
    DELIVERED_AT_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_REASON_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    sent_at: _timestamp_pb2.Timestamp
    delivered_at: _timestamp_pb2.Timestamp
    member_id: str
    status: Recipient.Status
    status_reason: str
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., sent_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., delivered_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., member_id: _Optional[str] = ..., status: _Optional[_Union[Recipient.Status, str]] = ..., status_reason: _Optional[str] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...
