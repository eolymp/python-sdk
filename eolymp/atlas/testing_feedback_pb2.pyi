from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class FeedbackPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPLETE: _ClassVar[FeedbackPolicy]
    ICPC: _ClassVar[FeedbackPolicy]
    ICPC_EXPANDED: _ClassVar[FeedbackPolicy]
COMPLETE: FeedbackPolicy
ICPC: FeedbackPolicy
ICPC_EXPANDED: FeedbackPolicy
