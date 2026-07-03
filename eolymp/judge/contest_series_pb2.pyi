from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContestSeries(_message.Message):
    __slots__ = ("id", "name", "hidden", "variants")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[ContestSeries.Extra]
        VARIANTS: _ClassVar[ContestSeries.Extra]
    UNKNOWN_EXTRA: ContestSeries.Extra
    VARIANTS: ContestSeries.Extra
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
    VARIANTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    hidden: bool
    variants: _containers.RepeatedCompositeFieldContainer[ContestSeries.Variant]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., hidden: _Optional[bool] = ..., variants: _Optional[_Iterable[_Union[ContestSeries.Variant, _Mapping]]] = ...) -> None: ...
