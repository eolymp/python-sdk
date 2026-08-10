from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class WatchEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_WATCH_EVENT_TYPE: _ClassVar[WatchEventType]
    CREATED: _ClassVar[WatchEventType]
    UPDATED: _ClassVar[WatchEventType]
    DELETED: _ClassVar[WatchEventType]
UNKNOWN_WATCH_EVENT_TYPE: WatchEventType
CREATED: WatchEventType
UPDATED: WatchEventType
DELETED: WatchEventType
