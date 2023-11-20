from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Subscription(_message.Message):
    __slots__ = ["cancel_url", "cancellation_comment", "cancellation_feedback", "cancellation_reason", "cancelled_at", "checkout_url", "created_at", "currency", "id", "items", "member_id", "payer_email", "payment_method", "period_end", "period_start", "space_id", "started_at", "status", "success_url", "total_amount", "user_id"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Item(_message.Message):
        __slots__ = ["active", "id", "price_id", "product_id"]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        PRICE_ID_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        active: bool
        id: str
        price_id: str
        product_id: str
        def __init__(self, id: _Optional[str] = ..., active: bool = ..., product_id: _Optional[str] = ..., price_id: _Optional[str] = ...) -> None: ...
    ACTIVE: Subscription.Status
    CANCELLATION_COMMENT_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    CANCELLATION_REASON_FIELD_NUMBER: _ClassVar[int]
    CANCELLED: Subscription.Status
    CANCELLED_AT_FIELD_NUMBER: _ClassVar[int]
    CANCEL_URL_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PAUSED: Subscription.Status
    PAYER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    PENDING: Subscription.Status
    PERIOD_END_FIELD_NUMBER: _ClassVar[int]
    PERIOD_START_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_URL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STATUS: Subscription.Status
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    cancel_url: str
    cancellation_comment: str
    cancellation_feedback: str
    cancellation_reason: str
    cancelled_at: _timestamp_pb2.Timestamp
    checkout_url: str
    created_at: _timestamp_pb2.Timestamp
    currency: str
    id: str
    items: _containers.RepeatedCompositeFieldContainer[Subscription.Item]
    member_id: str
    payer_email: str
    payment_method: str
    period_end: _timestamp_pb2.Timestamp
    period_start: _timestamp_pb2.Timestamp
    space_id: str
    started_at: _timestamp_pb2.Timestamp
    status: Subscription.Status
    success_url: str
    total_amount: int
    user_id: str
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[Subscription.Status, str]] = ..., space_id: _Optional[str] = ..., user_id: _Optional[str] = ..., member_id: _Optional[str] = ..., payer_email: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancelled_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., payment_method: _Optional[str] = ..., cancellation_comment: _Optional[str] = ..., cancellation_feedback: _Optional[str] = ..., cancellation_reason: _Optional[str] = ..., currency: _Optional[str] = ..., total_amount: _Optional[int] = ..., success_url: _Optional[str] = ..., cancel_url: _Optional[str] = ..., checkout_url: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Subscription.Item, _Mapping]]] = ...) -> None: ...
