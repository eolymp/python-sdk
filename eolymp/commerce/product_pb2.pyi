from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Product(_message.Message):
    __slots__ = ("id", "name", "summary", "description", "images", "out_of_stock", "featured", "inactive", "backorder", "currency", "price", "regular_price", "attributes", "variants", "cursor")
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
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[Product.Patch.Field]
            ALL: _ClassVar[Product.Patch.Field]
            NAME: _ClassVar[Product.Patch.Field]
            SUMMARY: _ClassVar[Product.Patch.Field]
            DESCRIPTION: _ClassVar[Product.Patch.Field]
            IMAGES: _ClassVar[Product.Patch.Field]
            PRICE: _ClassVar[Product.Patch.Field]
            REGULAR_PRICE: _ClassVar[Product.Patch.Field]
            ATTRIBUTES: _ClassVar[Product.Patch.Field]
            VARIANTS: _ClassVar[Product.Patch.Field]
            FEATURED: _ClassVar[Product.Patch.Field]
            INACTIVE: _ClassVar[Product.Patch.Field]
            BACKORDER: _ClassVar[Product.Patch.Field]
        UNKNOWN_FIELD: Product.Patch.Field
        ALL: Product.Patch.Field
        NAME: Product.Patch.Field
        SUMMARY: Product.Patch.Field
        DESCRIPTION: Product.Patch.Field
        IMAGES: Product.Patch.Field
        PRICE: Product.Patch.Field
        REGULAR_PRICE: Product.Patch.Field
        ATTRIBUTES: Product.Patch.Field
        VARIANTS: Product.Patch.Field
        FEATURED: Product.Patch.Field
        INACTIVE: Product.Patch.Field
        BACKORDER: Product.Patch.Field
        def __init__(self) -> None: ...
    class Attribute(_message.Message):
        __slots__ = ("key", "label")
        KEY_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        key: str
        label: str
        def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...
    class Variant(_message.Message):
        __slots__ = ("id", "name", "values", "images", "out_of_stock", "max_quantity", "available_quantity")
        class ValuesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        OUT_OF_STOCK_FIELD_NUMBER: _ClassVar[int]
        MAX_QUANTITY_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_QUANTITY_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        values: _containers.ScalarMap[str, str]
        images: _containers.RepeatedScalarFieldContainer[str]
        out_of_stock: bool
        max_quantity: int
        available_quantity: int
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., values: _Optional[_Mapping[str, str]] = ..., images: _Optional[_Iterable[str]] = ..., out_of_stock: bool = ..., max_quantity: _Optional[int] = ..., available_quantity: _Optional[int] = ...) -> None: ...
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
    cursor: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., summary: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., images: _Optional[_Iterable[str]] = ..., out_of_stock: bool = ..., featured: bool = ..., inactive: bool = ..., backorder: bool = ..., currency: _Optional[str] = ..., price: _Optional[int] = ..., regular_price: _Optional[int] = ..., attributes: _Optional[_Iterable[_Union[Product.Attribute, _Mapping]]] = ..., variants: _Optional[_Iterable[_Union[Product.Variant, _Mapping]]] = ..., cursor: _Optional[str] = ...) -> None: ...
