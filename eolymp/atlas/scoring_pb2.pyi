from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

ALL: ScoringMode
BEST: ScoringMode
DESCRIPTOR: _descriptor.FileDescriptor
EACH: ScoringMode
NO_SCORE: ScoringMode
WORST: ScoringMode

class ScoringMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
