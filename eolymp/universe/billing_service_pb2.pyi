from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.commerce import invoice_pb2 as _invoice_pb2
from eolymp.universe import billing_pb2 as _billing_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CancelSubscriptionInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CancelSubscriptionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreatePortalLinkInput(_message.Message):
    __slots__ = ["back_url", "flow", "return_url"]
    BACK_URL_FIELD_NUMBER: _ClassVar[int]
    FLOW_FIELD_NUMBER: _ClassVar[int]
    RETURN_URL_FIELD_NUMBER: _ClassVar[int]
    back_url: str
    flow: str
    return_url: str
    def __init__(self, flow: _Optional[str] = ..., back_url: _Optional[str] = ..., return_url: _Optional[str] = ...) -> None: ...

class CreatePortalLinkOutput(_message.Message):
    __slots__ = ["portal_link"]
    PORTAL_LINK_FIELD_NUMBER: _ClassVar[int]
    portal_link: str
    def __init__(self, portal_link: _Optional[str] = ...) -> None: ...

class CreateSubscriptionInput(_message.Message):
    __slots__ = ["plan_id", "seats", "variant_id"]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    SEATS_FIELD_NUMBER: _ClassVar[int]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    plan_id: str
    seats: int
    variant_id: str
    def __init__(self, plan_id: _Optional[str] = ..., variant_id: _Optional[str] = ..., seats: _Optional[int] = ...) -> None: ...

class CreateSubscriptionOutput(_message.Message):
    __slots__ = ["checkout_url"]
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    checkout_url: str
    def __init__(self, checkout_url: _Optional[str] = ...) -> None: ...

class DescribeBillingInformationInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeBillingInformationOutput(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _billing_pb2.Billing.Information
    def __init__(self, info: _Optional[_Union[_billing_pb2.Billing.Information, _Mapping]] = ...) -> None: ...

class DescribeInvoiceInput(_message.Message):
    __slots__ = ["invoice_id"]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    def __init__(self, invoice_id: _Optional[str] = ...) -> None: ...

class DescribeInvoiceOutput(_message.Message):
    __slots__ = ["invoice"]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoice_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ...) -> None: ...

class DescribeSubscriptionInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeSubscriptionOutput(_message.Message):
    __slots__ = ["current", "upcoming"]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    UPCOMING_FIELD_NUMBER: _ClassVar[int]
    current: _billing_pb2.Billing.Subscription
    upcoming: _billing_pb2.Billing.Subscription
    def __init__(self, current: _Optional[_Union[_billing_pb2.Billing.Subscription, _Mapping]] = ..., upcoming: _Optional[_Union[_billing_pb2.Billing.Subscription, _Mapping]] = ...) -> None: ...

class EndSubscriptionTrialInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class EndSubscriptionTrialOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ListInvoicesInput(_message.Message):
    __slots__ = ["after", "before", "size"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    after: str
    before: str
    size: int
    def __init__(self, size: _Optional[int] = ..., after: _Optional[str] = ..., before: _Optional[str] = ...) -> None: ...

class ListInvoicesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_invoice_pb2.Invoice]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_invoice_pb2.Invoice, _Mapping]]] = ...) -> None: ...

class PayInvoiceInput(_message.Message):
    __slots__ = ["invoice_id"]
    INVOICE_ID_FIELD_NUMBER: _ClassVar[int]
    invoice_id: str
    def __init__(self, invoice_id: _Optional[str] = ...) -> None: ...

class PayInvoiceOutput(_message.Message):
    __slots__ = ["checkout_url"]
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    checkout_url: str
    def __init__(self, checkout_url: _Optional[str] = ...) -> None: ...

class SimulateSubscriptionInput(_message.Message):
    __slots__ = ["coupon", "plan_id", "seats", "variant_id"]
    COUPON_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    SEATS_FIELD_NUMBER: _ClassVar[int]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    coupon: str
    plan_id: str
    seats: int
    variant_id: str
    def __init__(self, plan_id: _Optional[str] = ..., variant_id: _Optional[str] = ..., seats: _Optional[int] = ..., coupon: _Optional[str] = ...) -> None: ...

class SimulateSubscriptionOutput(_message.Message):
    __slots__ = ["due", "invoice"]
    DUE_FIELD_NUMBER: _ClassVar[int]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    due: _invoice_pb2.Invoice
    invoice: _invoice_pb2.Invoice
    def __init__(self, due: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ..., invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ...) -> None: ...

class StartSubscriptionTrialInput(_message.Message):
    __slots__ = ["plan_id", "variant_id"]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    plan_id: str
    variant_id: str
    def __init__(self, plan_id: _Optional[str] = ..., variant_id: _Optional[str] = ...) -> None: ...

class StartSubscriptionTrialOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpcomingInvoiceInput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpcomingInvoiceOutput(_message.Message):
    __slots__ = ["invoice"]
    INVOICE_FIELD_NUMBER: _ClassVar[int]
    invoice: _invoice_pb2.Invoice
    def __init__(self, invoice: _Optional[_Union[_invoice_pb2.Invoice, _Mapping]] = ...) -> None: ...

class UpdateBillingInformationInput(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _billing_pb2.Billing.Information
    def __init__(self, info: _Optional[_Union[_billing_pb2.Billing.Information, _Mapping]] = ...) -> None: ...

class UpdateBillingInformationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateSubscriptionInput(_message.Message):
    __slots__ = ["plan_id", "seats", "variant_id"]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    SEATS_FIELD_NUMBER: _ClassVar[int]
    VARIANT_ID_FIELD_NUMBER: _ClassVar[int]
    plan_id: str
    seats: int
    variant_id: str
    def __init__(self, plan_id: _Optional[str] = ..., variant_id: _Optional[str] = ..., seats: _Optional[int] = ...) -> None: ...

class UpdateSubscriptionOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
