from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ("id", "name", "summary", "description", "images", "out_of_stock", "featured", "inactive", "backorder", "currency", "price", "regular_price", "attributes", "variants", "stripe_product_id", "stripe_price_id", "cursor")
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[Product.Extra.Field]
            SUMMARY_VALUE: _ClassVar[Product.Extra.Field]
            SUMMARY_RENDER: _ClassVar[Product.Extra.Field]
            DESCRIPTION_VALUE: _ClassVar[Product.Extra.Field]
            DESCRIPTION_RENDER: _ClassVar[Product.Extra.Field]
            ATTRIBUTES: _ClassVar[Product.Extra.Field]
            VARIANTS: _ClassVar[Product.Extra.Field]
        UNKNOWN_FIELD: Product.Extra.Field
        SUMMARY_VALUE: Product.Extra.Field
        SUMMARY_RENDER: Product.Extra.Field
        DESCRIPTION_VALUE: Product.Extra.Field
        DESCRIPTION_RENDER: Product.Extra.Field
        ATTRIBUTES: Product.Extra.Field
        VARIANTS: Product.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ("name", "summary", "description", "images", "unimage", "price", "regular_price", "featured", "inactive", "backorder", "attributes")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        UNIMAGE_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        REGULAR_PRICE_FIELD_NUMBER: _ClassVar[int]
        FEATURED_FIELD_NUMBER: _ClassVar[int]
        INACTIVE_FIELD_NUMBER: _ClassVar[int]
        BACKORDER_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        name: str
        summary: _content_pb2.Content
        description: _content_pb2.Content
        images: _containers.RepeatedScalarFieldContainer[str]
        unimage: bool
        price: int
        regular_price: int
        featured: bool
        inactive: bool
        backorder: bool
        attributes: _containers.RepeatedCompositeFieldContainer[Product.Attribute]
        def __init__(self, name: _Optional[str] = ..., summary: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., images: _Optional[_Iterable[str]] = ..., unimage: _Optional[bool] = ..., price: _Optional[int] = ..., regular_price: _Optional[int] = ..., featured: _Optional[bool] = ..., inactive: _Optional[bool] = ..., backorder: _Optional[bool] = ..., attributes: _Optional[_Iterable[_Union[Product.Attribute, _Mapping]]] = ...) -> None: ...
    class Attribute(_message.Message):
        __slots__ = ("key", "label")
        KEY_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        key: str
        label: str
        def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...
    class Variant(_message.Message):
        __slots__ = ("id", "product_id", "name", "values", "images", "out_of_stock", "max_quantity", "available_quantity")
        class Patch(_message.Message):
            __slots__ = ("name", "values", "images", "unimage", "available_quantity")
            class ValuesEntry(_message.Message):
                __slots__ = ("key", "value")
                KEY_FIELD_NUMBER: _ClassVar[int]
                VALUE_FIELD_NUMBER: _ClassVar[int]
                key: str
                value: str
                def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
            NAME_FIELD_NUMBER: _ClassVar[int]
            VALUES_FIELD_NUMBER: _ClassVar[int]
            IMAGES_FIELD_NUMBER: _ClassVar[int]
            UNIMAGE_FIELD_NUMBER: _ClassVar[int]
            AVAILABLE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
            name: str
            values: _containers.ScalarMap[str, str]
            images: _containers.RepeatedScalarFieldContainer[str]
            unimage: bool
            available_quantity: int
            def __init__(self, name: _Optional[str] = ..., values: _Optional[_Mapping[str, str]] = ..., images: _Optional[_Iterable[str]] = ..., unimage: _Optional[bool] = ..., available_quantity: _Optional[int] = ...) -> None: ...
        class ValuesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        OUT_OF_STOCK_FIELD_NUMBER: _ClassVar[int]
        MAX_QUANTITY_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
        id: str
        product_id: str
        name: str
        values: _containers.ScalarMap[str, str]
        images: _containers.RepeatedScalarFieldContainer[str]
        out_of_stock: bool
        max_quantity: int
        available_quantity: int
        def __init__(self, id: _Optional[str] = ..., product_id: _Optional[str] = ..., name: _Optional[str] = ..., values: _Optional[_Mapping[str, str]] = ..., images: _Optional[_Iterable[str]] = ..., out_of_stock: _Optional[bool] = ..., max_quantity: _Optional[int] = ..., available_quantity: _Optional[int] = ...) -> None: ...
    class Translation(_message.Message):
        __slots__ = ("id", "locale", "name", "summary", "description", "attributes")
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        id: str
        locale: str
        name: str
        summary: _content_pb2.Content
        description: _content_pb2.Content
        attributes: _containers.RepeatedCompositeFieldContainer[Product.Attribute]
        def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., name: _Optional[str] = ..., summary: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., attributes: _Optional[_Iterable[_Union[Product.Attribute, _Mapping]]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_STOCK_FIELD_NUMBER: _ClassVar[int]
    FEATURED_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    BACKORDER_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    REGULAR_PRICE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    STRIPE_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    STRIPE_PRICE_ID_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    summary: _content_pb2.Content
    description: _content_pb2.Content
    images: _containers.RepeatedScalarFieldContainer[str]
    out_of_stock: bool
    featured: bool
    inactive: bool
    backorder: bool
    currency: str
    price: int
    regular_price: int
    attributes: _containers.RepeatedCompositeFieldContainer[Product.Attribute]
    variants: _containers.RepeatedCompositeFieldContainer[Product.Variant]
    stripe_product_id: str
    stripe_price_id: str
    cursor: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., summary: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., images: _Optional[_Iterable[str]] = ..., out_of_stock: _Optional[bool] = ..., featured: _Optional[bool] = ..., inactive: _Optional[bool] = ..., backorder: _Optional[bool] = ..., currency: _Optional[str] = ..., price: _Optional[int] = ..., regular_price: _Optional[int] = ..., attributes: _Optional[_Iterable[_Union[Product.Attribute, _Mapping]]] = ..., variants: _Optional[_Iterable[_Union[Product.Variant, _Mapping]]] = ..., stripe_product_id: _Optional[str] = ..., stripe_price_id: _Optional[str] = ..., cursor: _Optional[str] = ...) -> None: ...
