from eolymp.commerce import address_pb2 as _address_pb2
from eolymp.universe import plan_pb2 as _plan_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Billing(_message.Message):
    __slots__ = ()
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Billing.Status]
        TRIAL: _ClassVar[Billing.Status]
        ACTIVE: _ClassVar[Billing.Status]
        CANCELLED: _ClassVar[Billing.Status]
    UNKNOWN_STATUS: Billing.Status
    TRIAL: Billing.Status
    ACTIVE: Billing.Status
    CANCELLED: Billing.Status
    class Recurrence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_RECURRENCE: _ClassVar[Billing.Recurrence]
        MONTHLY: _ClassVar[Billing.Recurrence]
        YEARLY: _ClassVar[Billing.Recurrence]
    UNKNOWN_RECURRENCE: Billing.Recurrence
    MONTHLY: Billing.Recurrence
    YEARLY: Billing.Recurrence
    class Information(_message.Message):
        __slots__ = ("name", "email", "phone", "tax_id_type", "tax_id_value", "address", "currency", "language")
        NAME_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        PHONE_FIELD_NUMBER: _ClassVar[int]
        TAX_ID_TYPE_FIELD_NUMBER: _ClassVar[int]
        TAX_ID_VALUE_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        name: str
        email: str
        phone: str
        tax_id_type: str
        tax_id_value: str
        address: _address_pb2.Address
        currency: str
        language: str
        def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., tax_id_type: _Optional[str] = ..., tax_id_value: _Optional[str] = ..., address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., currency: _Optional[str] = ..., language: _Optional[str] = ...) -> None: ...
    class Subscription(_message.Message):
        __slots__ = ("id", "status", "irregular", "has_payment_method", "plan", "variant", "seats", "created_at", "started_at", "cancel_at", "cancelled_at", "ended_at", "period_start", "period_end", "trial_start", "trial_end")
        ID_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        IRREGULAR_FIELD_NUMBER: _ClassVar[int]
        HAS_PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
        PLAN_FIELD_NUMBER: _ClassVar[int]
        VARIANT_FIELD_NUMBER: _ClassVar[int]
        SEATS_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        STARTED_AT_FIELD_NUMBER: _ClassVar[int]
        CANCEL_AT_FIELD_NUMBER: _ClassVar[int]
        CANCELLED_AT_FIELD_NUMBER: _ClassVar[int]
        ENDED_AT_FIELD_NUMBER: _ClassVar[int]
        PERIOD_START_FIELD_NUMBER: _ClassVar[int]
        PERIOD_END_FIELD_NUMBER: _ClassVar[int]
        TRIAL_START_FIELD_NUMBER: _ClassVar[int]
        TRIAL_END_FIELD_NUMBER: _ClassVar[int]
        id: str
        status: Billing.Status
        irregular: bool
        has_payment_method: bool
        plan: _plan_pb2.Plan
        variant: _plan_pb2.Plan.Variant
        seats: int
        created_at: _timestamp_pb2.Timestamp
        started_at: _timestamp_pb2.Timestamp
        cancel_at: _timestamp_pb2.Timestamp
        cancelled_at: _timestamp_pb2.Timestamp
        ended_at: _timestamp_pb2.Timestamp
        period_start: _timestamp_pb2.Timestamp
        period_end: _timestamp_pb2.Timestamp
        trial_start: _timestamp_pb2.Timestamp
        trial_end: _timestamp_pb2.Timestamp
        def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[Billing.Status, str]] = ..., irregular: bool = ..., has_payment_method: bool = ..., plan: _Optional[_Union[_plan_pb2.Plan, _Mapping]] = ..., variant: _Optional[_Union[_plan_pb2.Plan.Variant, _Mapping]] = ..., seats: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancel_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancelled_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., trial_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., trial_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
