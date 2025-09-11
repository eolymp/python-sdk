from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ("id", "name", "description", "images", "out_of_stock", "currency", "unit_price", "attributes", "variants")
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[Product.Extra.Field]
            DESCRIPTION_VALUE: _ClassVar[Product.Extra.Field]
            DESCRIPTION_RENDER: _ClassVar[Product.Extra.Field]
            ATTRIBUTES: _ClassVar[Product.Extra.Field]
            VARIANTS: _ClassVar[Product.Extra.Field]
        UNKNOWN_FIELD: Product.Extra.Field
        DESCRIPTION_VALUE: Product.Extra.Field
        DESCRIPTION_RENDER: Product.Extra.Field
        ATTRIBUTES: Product.Extra.Field
        VARIANTS: Product.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[Product.Patch.Field]
            ALL: _ClassVar[Product.Patch.Field]
            NAME: _ClassVar[Product.Patch.Field]
            DESCRIPTION: _ClassVar[Product.Patch.Field]
            IMAGES: _ClassVar[Product.Patch.Field]
            UNIT_PRICE: _ClassVar[Product.Patch.Field]
            ATTRIBUTES: _ClassVar[Product.Patch.Field]
            VARIANTS: _ClassVar[Product.Patch.Field]
        UNKNOWN_FIELD: Product.Patch.Field
        ALL: Product.Patch.Field
        NAME: Product.Patch.Field
        DESCRIPTION: Product.Patch.Field
        IMAGES: Product.Patch.Field
        UNIT_PRICE: Product.Patch.Field
        ATTRIBUTES: Product.Patch.Field
        VARIANTS: Product.Patch.Field
        def __init__(self) -> None: ...
    class Attribute(_message.Message):
        __slots__ = ("key", "label")
        KEY_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        key: str
        label: str
        def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...
    class Variant(_message.Message):
        __slots__ = ("id", "values", "images", "out_of_stock")
        class ValuesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        OUT_OF_STOCK_FIELD_NUMBER: _ClassVar[int]
        id: str
        values: _containers.ScalarMap[str, str]
        images: _containers.RepeatedScalarFieldContainer[str]
        out_of_stock: bool
        def __init__(self, id: _Optional[str] = ..., values: _Optional[_Mapping[str, str]] = ..., images: _Optional[_Iterable[str]] = ..., out_of_stock: bool = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_STOCK_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    UNIT_PRICE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: _content_pb2.Content
    images: _containers.RepeatedScalarFieldContainer[str]
    out_of_stock: bool
    currency: str
    unit_price: int
    attributes: _containers.RepeatedCompositeFieldContainer[Product.Attribute]
    variants: _containers.RepeatedCompositeFieldContainer[Product.Variant]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., images: _Optional[_Iterable[str]] = ..., out_of_stock: bool = ..., currency: _Optional[str] = ..., unit_price: _Optional[int] = ..., attributes: _Optional[_Iterable[_Union[Product.Attribute, _Mapping]]] = ..., variants: _Optional[_Iterable[_Union[Product.Variant, _Mapping]]] = ...) -> None: ...
