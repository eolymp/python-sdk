from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostType(_message.Message):
    __slots__ = ("id", "name", "hidden", "order", "variants")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[PostType.Extra]
        VARIANTS: _ClassVar[PostType.Extra]
    UNKNOWN_EXTRA: PostType.Extra
    VARIANTS: PostType.Extra
    class Variant(_message.Message):
        __slots__ = ("locale", "name")
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        locale: str
        name: str
        def __init__(self, locale: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    hidden: bool
    order: int
    variants: _containers.RepeatedCompositeFieldContainer[PostType.Variant]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., hidden: bool = ..., order: _Optional[int] = ..., variants: _Optional[_Iterable[_Union[PostType.Variant, _Mapping]]] = ...) -> None: ...
