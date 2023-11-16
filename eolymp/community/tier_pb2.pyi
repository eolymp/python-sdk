from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tier(_message.Message):
    __slots__ = ["description", "id", "monthly_price", "name", "onetime_price", "yearly_price"]
    class Price(_message.Message):
        __slots__ = ["currency", "price", "promotion_due_date", "promotion_percentage", "promotion_price"]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        PROMOTION_DUE_DATE_FIELD_NUMBER: _ClassVar[int]
        PROMOTION_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        PROMOTION_PRICE_FIELD_NUMBER: _ClassVar[int]
        currency: str
        price: float
        promotion_due_date: _timestamp_pb2.Timestamp
        promotion_percentage: float
        promotion_price: float
        def __init__(self, currency: _Optional[str] = ..., price: _Optional[float] = ..., promotion_price: _Optional[float] = ..., promotion_percentage: _Optional[float] = ..., promotion_due_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_PRICE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ONETIME_PRICE_FIELD_NUMBER: _ClassVar[int]
    YEARLY_PRICE_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    monthly_price: Tier.Price
    name: str
    onetime_price: Tier.Price
    yearly_price: Tier.Price
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., onetime_price: _Optional[_Union[Tier.Price, _Mapping]] = ..., monthly_price: _Optional[_Union[Tier.Price, _Mapping]] = ..., yearly_price: _Optional[_Union[Tier.Price, _Mapping]] = ...) -> None: ...
