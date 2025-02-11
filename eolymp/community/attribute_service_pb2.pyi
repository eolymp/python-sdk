from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import attribute_pb2 as _attribute_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAttributeInput(_message.Message):
    __slots__ = ("attribute_key", "attribute")
    ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    attribute_key: str
    attribute: _attribute_pb2.Attribute
    def __init__(self, attribute_key: _Optional[str] = ..., attribute: _Optional[_Union[_attribute_pb2.Attribute, _Mapping]] = ...) -> None: ...

class CreateAttributeOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateAttributeInput(_message.Message):
    __slots__ = ("patch", "attribute_key", "attribute")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_attribute_pb2.Attribute.Patch]
    attribute_key: str
    attribute: _attribute_pb2.Attribute
    def __init__(self, patch: _Optional[_Iterable[_Union[_attribute_pb2.Attribute.Patch, str]]] = ..., attribute_key: _Optional[str] = ..., attribute: _Optional[_Union[_attribute_pb2.Attribute, _Mapping]] = ...) -> None: ...

class UpdateAttributeOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveAttributeInput(_message.Message):
    __slots__ = ("attribute_key",)
    ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
    attribute_key: str
    def __init__(self, attribute_key: _Optional[str] = ...) -> None: ...

class RemoveAttributeOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeAttributeInput(_message.Message):
    __slots__ = ("attribute_key",)
    ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
    attribute_key: str
    def __init__(self, attribute_key: _Optional[str] = ...) -> None: ...

class DescribeAttributeOutput(_message.Message):
    __slots__ = ("attribute",)
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    attribute: _attribute_pb2.Attribute
    def __init__(self, attribute: _Optional[_Union[_attribute_pb2.Attribute, _Mapping]] = ...) -> None: ...

class ListAttributesInput(_message.Message):
    __slots__ = ("offset", "size", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "key", "hidden", "required", "type")
        ID_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        HIDDEN_FIELD_NUMBER: _ClassVar[int]
        REQUIRED_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        key: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        hidden: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        required: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., key: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., hidden: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., required: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListAttributesInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListAttributesInput.Filter, _Mapping]] = ...) -> None: ...

class ListAttributesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_attribute_pb2.Attribute, _Mapping]]] = ...) -> None: ...
