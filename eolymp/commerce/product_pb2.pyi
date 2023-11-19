from eolymp.commerce import price_pb2 as _price_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ["active", "default_price", "description", "id", "image", "name", "page_url", "unit_label"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PRICE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    UNIT_LABEL_FIELD_NUMBER: _ClassVar[int]
    active: bool
    default_price: _price_pb2.Price
    description: str
    id: str
    image: str
    name: str
    page_url: str
    unit_label: str
    def __init__(self, id: _Optional[str] = ..., active: bool = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., description: _Optional[str] = ..., page_url: _Optional[str] = ..., unit_label: _Optional[str] = ..., default_price: _Optional[_Union[_price_pb2.Price, _Mapping]] = ...) -> None: ...
