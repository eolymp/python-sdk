from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ("name", "phone", "country", "state", "postal_code", "city", "line1", "house_number", "line2", "pickup_location")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    LINE1_FIELD_NUMBER: _ClassVar[int]
    HOUSE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LINE2_FIELD_NUMBER: _ClassVar[int]
    PICKUP_LOCATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    phone: str
    country: str
    state: str
    postal_code: str
    city: str
    line1: str
    house_number: str
    line2: str
    pickup_location: str
    def __init__(self, name: _Optional[str] = ..., phone: _Optional[str] = ..., country: _Optional[str] = ..., state: _Optional[str] = ..., postal_code: _Optional[str] = ..., city: _Optional[str] = ..., line1: _Optional[str] = ..., house_number: _Optional[str] = ..., line2: _Optional[str] = ..., pickup_location: _Optional[str] = ...) -> None: ...
