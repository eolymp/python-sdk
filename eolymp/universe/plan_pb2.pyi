from eolymp.commerce import price_pb2 as _price_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Plan(_message.Message):
    __slots__ = ["id", "name", "prices"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DESCRIPTION_RENDER: Plan.Extra
    DESCRIPTION_VALUE: Plan.Extra
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NO_EXTRA: Plan.Extra
    PRICES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    prices: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., prices: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]] = ...) -> None: ...
