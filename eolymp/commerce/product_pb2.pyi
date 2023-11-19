from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ["active", "default_price", "description", "id", "image", "name", "page_url", "unit_label"]
    class Recurrence(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Price(_message.Message):
        __slots__ = ["currency", "id", "recurrence", "unit_amount"]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        RECURRENCE_FIELD_NUMBER: _ClassVar[int]
        UNIT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        currency: str
        id: str
        recurrence: Product.Recurrence
        unit_amount: int
        def __init__(self, id: _Optional[str] = ..., recurrence: _Optional[_Union[Product.Recurrence, str]] = ..., currency: _Optional[str] = ..., unit_amount: _Optional[int] = ...) -> None: ...
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PRICE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    MONTHLY: Product.Recurrence
    NAME_FIELD_NUMBER: _ClassVar[int]
    ONETIME: Product.Recurrence
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    UNIT_LABEL_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_RECURRENCE: Product.Recurrence
    YEARLY: Product.Recurrence
    active: bool
    default_price: Product.Price
    description: str
    id: str
    image: str
    name: str
    page_url: str
    unit_label: str
    def __init__(self, id: _Optional[str] = ..., active: bool = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., description: _Optional[str] = ..., page_url: _Optional[str] = ..., unit_label: _Optional[str] = ..., default_price: _Optional[_Union[Product.Price, _Mapping]] = ...) -> None: ...
