from eolymp.commerce import address_pb2 as _address_pb2
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
    ACTIVE: Billing.Status
    CANCELLED: Billing.Status
    MONTHLY: Billing.Recurrence
    TRIAL: Billing.Status
    UNKNOWN_RECURRENCE: Billing.Recurrence
    UNKNOWN_STATUS: Billing.Status
    YEARLY: Billing.Recurrence
    def __init__(self) -> None: ...
