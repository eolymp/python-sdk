from eolymp.commerce import price_pb2 as _price_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Subscription(_message.Message):
    __slots__ = ["cancel_at", "cancellation_comment", "cancellation_feedback", "cancellation_reason", "cancelled_at", "created_at", "currency", "customer_id", "description", "ended_at", "id", "items", "period_end", "period_start", "started_at", "status", "trial_end", "trial_start"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Item(_message.Message):
        __slots__ = ["id", "price", "product_id", "quantity"]
        ID_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        id: str
        price: _price_pb2.Price
        product_id: str
        quantity: int
        def __init__(self, id: _Optional[str] = ..., quantity: _Optional[int] = ..., product_id: _Optional[str] = ..., price: _Optional[_Union[_price_pb2.Price, _Mapping]] = ...) -> None: ...
    ACTIVE: Subscription.Status
    CANCELLATION_COMMENT_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REASON_FIELD_NUMBER: _ClassVar[int]
    CANCELLED: Subscription.Status
    CANCELLED_AT_FIELD_NUMBER: _ClassVar[int]
    CANCEL_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENDED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INCOMPLETE: Subscription.Status
    INCOMPLETE_EXPIRED: Subscription.Status
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PAST_DUE: Subscription.Status
    PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    PERIOD_START_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TRIALING: Subscription.Status
    TRIAL_END_FIELD_NUMBER: _ClassVar[int]
    TRIAL_START_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STATUS: Subscription.Status
    UNPAID: Subscription.Status
    cancel_at: _timestamp_pb2.Timestamp
    cancellation_comment: str
    cancellation_feedback: str
    cancellation_reason: str
    cancelled_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    currency: str
    customer_id: str
    description: str
    ended_at: _timestamp_pb2.Timestamp
    id: str
    items: _containers.RepeatedCompositeFieldContainer[Subscription.Item]
    period_end: _timestamp_pb2.Timestamp
    period_start: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    status: Subscription.Status
    trial_end: _timestamp_pb2.Timestamp
    trial_start: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[Subscription.Status, str]] = ..., customer_id: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancel_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancelled_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., trial_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., trial_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancellation_comment: _Optional[str] = ..., cancellation_feedback: _Optional[str] = ..., cancellation_reason: _Optional[str] = ..., currency: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Subscription.Item, _Mapping]]] = ...) -> None: ...
