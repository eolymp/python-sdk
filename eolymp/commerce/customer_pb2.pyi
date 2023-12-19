from eolymp.commerce import address_pb2 as _address_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Customer(_message.Message):
    __slots__ = ["address", "currency", "description", "email", "id", "language", "metadata", "name", "phone", "tax_id_type", "tax_id_value"]
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    TAX_ID_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAX_ID_VALUE_FIELD_NUMBER: _ClassVar[int]
    address: _address_pb2.Address
    currency: str
    description: str
    email: str
    id: str
    language: str
    metadata: _containers.ScalarMap[str, str]
    name: str
    phone: str
    tax_id_type: str
    tax_id_value: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., tax_id_type: _Optional[str] = ..., tax_id_value: _Optional[str] = ..., address: _Optional[_Union[_address_pb2.Address, _Mapping]] = ..., currency: _Optional[str] = ..., language: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
