from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Subscription(_message.Message):
    __slots__ = ["amount", "cancelled_at", "created_at", "currency", "id", "member_id", "paused_at", "payment_method", "recurrence", "renewed_at", "renews_at", "started_at", "tax_amount", "tax_name", "tax_percentage", "tier_id"]
    class Recurrence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIVE: Subscription.Status
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CANCELLED: Subscription.Status
    CANCELLED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MONTHLY: Subscription.Recurrence
    PAUSED: Subscription.Status
    PAUSED_AT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    PENDING: Subscription.Status
    RECURRENCE_FIELD_NUMBER: _ClassVar[int]
    RENEWED_AT_FIELD_NUMBER: _ClassVar[int]
    RENEWS_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    TAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TAX_NAME_FIELD_NUMBER: _ClassVar[int]
    TAX_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    TIER_ID_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_RECURRENCE: Subscription.Recurrence
    UNKNOWN_STATUS: Subscription.Status
    YEARLY: Subscription.Recurrence
    amount: int
    cancelled_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    currency: str
    id: str
    member_id: str
    paused_at: _timestamp_pb2.Timestamp
    payment_method: str
    recurrence: Subscription.Recurrence
    renewed_at: _timestamp_pb2.Timestamp
    renews_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    tax_amount: int
    tax_name: str
    tax_percentage: int
    tier_id: str
    def __init__(self, id: _Optional[str] = ..., tier_id: _Optional[str] = ..., member_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., renewed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., renews_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancelled_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., paused_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., payment_method: _Optional[str] = ..., recurrence: _Optional[_Union[Subscription.Recurrence, str]] = ..., currency: _Optional[str] = ..., amount: _Optional[int] = ..., tax_name: _Optional[str] = ..., tax_amount: _Optional[int] = ..., tax_percentage: _Optional[int] = ...) -> None: ...
