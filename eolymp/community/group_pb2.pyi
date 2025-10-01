from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Group(_message.Message):
    __slots__ = ("id", "name", "description", "external_ref", "icon", "badge", "color", "metadata")
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[Group.Patch.Field]
            NAME: _ClassVar[Group.Patch.Field]
            DESCRIPTION: _ClassVar[Group.Patch.Field]
            EXTERNAL_REF: _ClassVar[Group.Patch.Field]
            ICON: _ClassVar[Group.Patch.Field]
            BADGE: _ClassVar[Group.Patch.Field]
            COLOR: _ClassVar[Group.Patch.Field]
            METADATA: _ClassVar[Group.Patch.Field]
        UNKNOWN: Group.Patch.Field
        NAME: Group.Patch.Field
        DESCRIPTION: Group.Patch.Field
        EXTERNAL_REF: Group.Patch.Field
        ICON: Group.Patch.Field
        BADGE: Group.Patch.Field
        COLOR: Group.Patch.Field
        METADATA: Group.Patch.Field
        def __init__(self) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REF_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    BADGE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    external_ref: str
    icon: str
    badge: str
    color: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., external_ref: _Optional[str] = ..., icon: _Optional[str] = ..., badge: _Optional[str] = ..., color: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...
