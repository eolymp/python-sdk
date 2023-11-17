from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ["city", "company_name", "country", "email", "first_name", "last_name", "phone", "postcode", "state", "street_name", "tax_number"]
    CITY_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    POSTCODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STREET_NAME_FIELD_NUMBER: _ClassVar[int]
    TAX_NUMBER_FIELD_NUMBER: _ClassVar[int]
    city: str
    company_name: str
    country: str
    email: str
    first_name: str
    last_name: str
    phone: str
    postcode: str
    state: str
    street_name: str
    tax_number: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., company_name: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., country: _Optional[str] = ..., state: _Optional[str] = ..., city: _Optional[str] = ..., postcode: _Optional[str] = ..., street_name: _Optional[str] = ..., tax_number: _Optional[str] = ...) -> None: ...
