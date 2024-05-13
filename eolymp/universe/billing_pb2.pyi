from eolymp.commerce import address_pb2 as _address_pb2
from eolymp.universe import plan_pb2 as _plan_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Billing(_message.Message):
    __slots__ = []
    class Recurrence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Information(_message.Message):
        __slots__ = ["address", "currency", "email", "language", "name", "phone", "tax_id_type", "tax_id_value"]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PHONE_FIELD_NUMBER: _ClassVar[int]
        TAX_ID_TYPE_FIELD_NUMBER: _ClassVar[int]
        TAX_ID_VALUE_FIELD_NUMBER: _ClassVar[int]
        address: _address_pb2.Address
        currency: str
        email: str
        language: str
        name: str
        phone: str
        tax_id_type: str
        tax_id_value: str
        def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., tax_id_type: _Optional[str] = ..., tax_id_value: _Optional[str] = ..., address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., currency: _Optional[str] = ..., language: _Optional[str] = ...) -> None: ...
    class Subscription(_message.Message):
        __slots__ = ["cancel_at", "cancelled_at", "created_at", "ended_at", "has_payment_method", "id", "irregular", "period_end", "period_start", "plan", "seats", "started_at", "status", "trial_end", "trial_start", "variant"]
        CANCELLED_AT_FIELD_NUMBER: _ClassVar[int]
        CANCEL_AT_FIELD_NUMBER: _ClassVar[int]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        ENDED_AT_FIELD_NUMBER: _ClassVar[int]
        HAS_PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        IRREGULAR_FIELD_NUMBER: _ClassVar[int]
        PERIOD_END_FIELD_NUMBER: _ClassVar[int]
        PERIOD_START_FIELD_NUMBER: _ClassVar[int]
        PLAN_FIELD_NUMBER: _ClassVar[int]
        SEATS_FIELD_NUMBER: _ClassVar[int]
        STARTED_AT_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TRIAL_END_FIELD_NUMBER: _ClassVar[int]
        TRIAL_START_FIELD_NUMBER: _ClassVar[int]
        VARIANT_FIELD_NUMBER: _ClassVar[int]
        cancel_at: _timestamp_pb2.Timestamp
        cancelled_at: _timestamp_pb2.Timestamp
        created_at: _timestamp_pb2.Timestamp
        ended_at: _timestamp_pb2.Timestamp
        has_payment_method: bool
        id: str
        irregular: bool
        period_end: _timestamp_pb2.Timestamp
        period_start: _timestamp_pb2.Timestamp
        plan: _plan_pb2.Plan
        seats: int
        started_at: _timestamp_pb2.Timestamp
        status: Billing.Status
        trial_end: _timestamp_pb2.Timestamp
        trial_start: _timestamp_pb2.Timestamp
        variant: _plan_pb2.Plan.Variant
        def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[Billing.Status, str]] = ..., irregular: bool = ..., has_payment_method: bool = ..., plan: _Optional[_Union[_plan_pb2.Plan, _Mapping]] = ..., variant: _Optional[_Union[_plan_pb2.Plan.Variant, _Mapping]] = ..., seats: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancel_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cancelled_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ended_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., period_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., trial_start: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., trial_end: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    ACTIVE: Billing.Status
    CANCELLED: Billing.Status
    MONTHLY: Billing.Recurrence
    TRIAL: Billing.Status
    UNKNOWN_RECURRENCE: Billing.Recurrence
    UNKNOWN_STATUS: Billing.Status
    YEARLY: Billing.Recurrence
    def __init__(self) -> None: ...
