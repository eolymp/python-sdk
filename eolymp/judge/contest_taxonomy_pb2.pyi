from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Taxonomy(_message.Message):
    __slots__ = ("year", "series", "scale", "difficulty", "country", "region", "city")
    class Scale(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_SCALE: _ClassVar[Taxonomy.Scale]
        LOCAL: _ClassVar[Taxonomy.Scale]
        REGIONAL: _ClassVar[Taxonomy.Scale]
        NATIONAL: _ClassVar[Taxonomy.Scale]
        INTERNATIONAL: _ClassVar[Taxonomy.Scale]
    UNKNOWN_SCALE: Taxonomy.Scale
    LOCAL: Taxonomy.Scale
    REGIONAL: Taxonomy.Scale
    NATIONAL: Taxonomy.Scale
    INTERNATIONAL: Taxonomy.Scale
    YEAR_FIELD_NUMBER: _ClassVar[int]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    DIFFICULTY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    year: int
    series: str
    scale: Taxonomy.Scale
    difficulty: int
    country: str
    region: str
    city: str
    def __init__(self, year: _Optional[int] = ..., series: _Optional[str] = ..., scale: _Optional[_Union[Taxonomy.Scale, str]] = ..., difficulty: _Optional[int] = ..., country: _Optional[str] = ..., region: _Optional[str] = ..., city: _Optional[str] = ...) -> None: ...
