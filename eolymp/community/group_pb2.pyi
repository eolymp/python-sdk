from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Group(_message.Message):
    __slots__ = ("id", "key", "name", "description", "index", "icon", "badge", "color")
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[Group.Patch.Field]
            NAME: _ClassVar[Group.Patch.Field]
            DESCRIPTION: _ClassVar[Group.Patch.Field]
            KEY: _ClassVar[Group.Patch.Field]
            ICON: _ClassVar[Group.Patch.Field]
            BADGE: _ClassVar[Group.Patch.Field]
            COLOR: _ClassVar[Group.Patch.Field]
        UNKNOWN: Group.Patch.Field
        NAME: Group.Patch.Field
        DESCRIPTION: Group.Patch.Field
        KEY: Group.Patch.Field
        ICON: Group.Patch.Field
        BADGE: Group.Patch.Field
        COLOR: Group.Patch.Field
        def __init__(self) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    BADGE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    name: str
    description: str
    index: int
    icon: str
    badge: str
    color: str
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., index: _Optional[int] = ..., icon: _Optional[str] = ..., badge: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...
