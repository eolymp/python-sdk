from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FinishReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_FINISH_REASON: _ClassVar[FinishReason]
    STOP: _ClassVar[FinishReason]
    LENGTH: _ClassVar[FinishReason]
    TOOL_CALLS: _ClassVar[FinishReason]
    CONTENT_FILTER: _ClassVar[FinishReason]
UNKNOWN_FINISH_REASON: FinishReason
STOP: FinishReason
LENGTH: FinishReason
TOOL_CALLS: FinishReason
CONTENT_FILTER: FinishReason
