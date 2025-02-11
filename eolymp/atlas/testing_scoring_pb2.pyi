from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ScoringMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_SCORE: _ClassVar[ScoringMode]
    EACH: _ClassVar[ScoringMode]
    ALL: _ClassVar[ScoringMode]
    WORST: _ClassVar[ScoringMode]
    BEST: _ClassVar[ScoringMode]
NO_SCORE: ScoringMode
EACH: ScoringMode
ALL: ScoringMode
WORST: ScoringMode
BEST: ScoringMode
