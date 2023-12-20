from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.commerce import price_pb2 as _price_pb2
from eolymp.universe import billing_pb2 as _billing_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CancelCurrentPlanInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CancelCurrentPlanOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeBillingInformationInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeBillingInformationOutput(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _billing_pb2.Billing.Information
    def __init__(self, info: _Optional[_Union[_billing_pb2.Billing.Information, _Mapping]] = ...) -> None: ...

class DescribeCurrentPlanInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeCurrentPlanOutput(_message.Message):
    __slots__ = ["cancel_at", "cancelled_at", "created_at", "invoice_quantity", "invoice_subtotal", "paused_at", "plan_id", "price", "quantity", "renewed_at", "renews_at", "started_at", "status"]
    CANCELLED_AT_FIELD_NUMBER: _ClassVar[int]
    CANCEL_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    INVOICE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    INVOICE_SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    PAUSED_AT_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    RENEWED_AT_FIELD_NUMBER: _ClassVar[int]
    RENEWS_AT_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    cancel_at: _timestamp_pb2.Timestamp
    cancelled_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    invoice_quantity: int
    invoice_subtotal: int
    paused_at: _timestamp_pb2.Timestamp
    plan_id: str
    price: _price_pb2.Price
    quantity: int
    renewed_at: _timestamp_pb2.Timestamp
    renews_at: _timestamp_pb2.Timestamp
    started_at: _timestamp_pb2.Timestamp
    status: _billing_pb2.Billing.Status
    def __init__(self, plan_id: _Optional[str] = ..., quantity: _Optional[int] = ..., status: _Optional[_Union[_billing_pb2.Billing.Status, str]] = ..., price: _Optional[_Union[_price_pb2.Price, _Mapping]] = ..., invoice_quantity: _Optional[int] = ..., invoice_subtotal: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., renewed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., renews_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancel_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancelled_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., paused_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class UpdateBillingInformationInput(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _billing_pb2.Billing.Information
    def __init__(self, info: _Optional[_Union[_billing_pb2.Billing.Information, _Mapping]] = ...) -> None: ...

class UpdateBillingInformationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateCurrentPlanInput(_message.Message):
    __slots__ = ["plan_id", "price_id", "quantity"]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    plan_id: str
    price_id: str
    quantity: int
    def __init__(self, plan_id: _Optional[str] = ..., price_id: _Optional[str] = ..., quantity: _Optional[int] = ...) -> None: ...

class UpdateCurrentPlanOutput(_message.Message):
    __slots__ = ["checkout_url"]
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    checkout_url: str
    def __init__(self, checkout_url: _Optional[str] = ...) -> None: ...
