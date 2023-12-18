from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Billing(_message.Message):
    __slots__ = []
    class Recurrence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Information(_message.Message):
        __slots__ = ["address_address_line1", "address_address_line2", "address_address_line3", "address_city", "address_country", "address_post_code", "address_region", "currency", "email", "language", "name", "phone", "tax_id"]
        ADDRESS_ADDRESS_LINE1_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_ADDRESS_LINE2_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_ADDRESS_LINE3_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_CITY_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_COUNTRY_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_POST_CODE_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_REGION_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PHONE_FIELD_NUMBER: _ClassVar[int]
        TAX_ID_FIELD_NUMBER: _ClassVar[int]
        address_address_line1: str
        address_address_line2: str
        address_address_line3: str
        address_city: str
        address_country: str
        address_post_code: str
        address_region: str
        currency: str
        email: str
        language: str
        name: str
        phone: str
        tax_id: str
        def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., address_country: _Optional[str] = ..., address_post_code: _Optional[str] = ..., address_region: _Optional[str] = ..., address_city: _Optional[str] = ..., address_address_line1: _Optional[str] = ..., address_address_line2: _Optional[str] = ..., address_address_line3: _Optional[str] = ..., tax_id: _Optional[str] = ..., currency: _Optional[str] = ..., language: _Optional[str] = ...) -> None: ...
    ACTIVE: Billing.Status
    CANCELLED: Billing.Status
    MONTHLY: Billing.Recurrence
    TRIAL: Billing.Status
    UNKNOWN_RECURRENCE: Billing.Recurrence
    UNKNOWN_STATUS: Billing.Status
    YEARLY: Billing.Recurrence
    def __init__(self) -> None: ...
