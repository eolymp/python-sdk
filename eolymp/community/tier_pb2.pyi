from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tier(_message.Message):
    __slots__ = ["description", "id", "image", "name", "price"]
    class Price(_message.Message):
        __slots__ = ["currency", "monthly_price", "onetime_price", "yearly_price"]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        MONTHLY_PRICE_FIELD_NUMBER: _ClassVar[int]
        ONETIME_PRICE_FIELD_NUMBER: _ClassVar[int]
        YEARLY_PRICE_FIELD_NUMBER: _ClassVar[int]
        currency: str
        monthly_price: int
        onetime_price: int
        yearly_price: int
        def __init__(self, currency: _Optional[str] = ..., onetime_price: _Optional[int] = ..., monthly_price: _Optional[int] = ..., yearly_price: _Optional[int] = ...) -> None: ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    description: _content_pb2.Content
    id: str
    image: str
    name: str
    price: Tier.Price
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., image: _Optional[str] = ..., price: _Optional[_Union[Tier.Price, _Mapping]] = ...) -> None: ...
