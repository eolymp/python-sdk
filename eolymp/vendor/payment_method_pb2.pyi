from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentMethod(_message.Message):
    __slots__ = ("id", "name", "default", "country", "sepa_transfer", "swift_transfer")
    class TransferSEPA(_message.Message):
        __slots__ = ("iban",)
        IBAN_FIELD_NUMBER: _ClassVar[int]
        iban: str
        def __init__(self, iban: _Optional[str] = ...) -> None: ...
    class TransferSWIFT(_message.Message):
        __slots__ = ("bic_code", "account_number")
        BIC_CODE_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        bic_code: str
        account_number: str
        def __init__(self, bic_code: _Optional[str] = ..., account_number: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    SEPA_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    SWIFT_TRANSFER_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    default: bool
    country: str
    sepa_transfer: PaymentMethod.TransferSEPA
    swift_transfer: PaymentMethod.TransferSWIFT
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., default: bool = ..., country: _Optional[str] = ..., sepa_transfer: _Optional[_Union[PaymentMethod.TransferSEPA, _Mapping]] = ..., swift_transfer: _Optional[_Union[PaymentMethod.TransferSWIFT, _Mapping]] = ...) -> None: ...
