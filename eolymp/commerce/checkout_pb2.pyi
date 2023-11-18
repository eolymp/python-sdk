from eolymp.commerce import recurrence_pb2 as _recurrence_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Checkout(_message.Message):
    __slots__ = ["cancel_url", "currency", "items", "member_id", "mode", "payer_email", "reference", "space_id", "success_url", "user_id"]
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Item(_message.Message):
        __slots__ = ["description", "name", "price", "recurrence", "reference"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        RECURRENCE_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        description: str
        name: str
        price: int
        recurrence: _recurrence_pb2.Recurrence
        reference: str
        def __init__(self, reference: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., price: _Optional[int] = ..., recurrence: _Optional[_Union[_recurrence_pb2.Recurrence, str]] = ...) -> None: ...
    CANCEL_URL_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    PAYER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    PAYMENT: Checkout.Mode
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION: Checkout.Mode
    SUCCESS_URL_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_MODE: Checkout.Mode
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    cancel_url: str
    currency: str
    items: _containers.RepeatedCompositeFieldContainer[Checkout.Item]
    member_id: str
    mode: Checkout.Mode
    payer_email: str
    reference: str
    space_id: str
    success_url: str
    user_id: str
    def __init__(self, space_id: _Optional[str] = ..., reference: _Optional[str] = ..., currency: _Optional[str] = ..., mode: _Optional[_Union[Checkout.Mode, str]] = ..., success_url: _Optional[str] = ..., cancel_url: _Optional[str] = ..., member_id: _Optional[str] = ..., user_id: _Optional[str] = ..., payer_email: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Checkout.Item, _Mapping]]] = ...) -> None: ...
