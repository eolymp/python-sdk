from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tier(_message.Message):
    __slots__ = ["currency", "description", "id", "image", "monthly_price", "name", "onetime_price", "yearly_price"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_PRICE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ONETIME_PRICE_FIELD_NUMBER: _ClassVar[int]
    YEARLY_PRICE_FIELD_NUMBER: _ClassVar[int]
    currency: str
    description: _content_pb2.Content
    id: str
    image: str
    monthly_price: int
    name: str
    onetime_price: int
    yearly_price: int
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., image: _Optional[str] = ..., currency: _Optional[str] = ..., onetime_price: _Optional[int] = ..., monthly_price: _Optional[int] = ..., yearly_price: _Optional[int] = ...) -> None: ...
