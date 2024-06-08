from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Institution(_message.Message):
    __slots__ = ["abbr", "abbr_local", "address", "country_id", "governance", "id", "level", "links", "logo_url", "name", "name_locale", "region_id", "type"]
    class Governance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class LinksEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ABBR_FIELD_NUMBER: _ClassVar[int]
    ABBR_LOCAL_FIELD_NUMBER: _ClassVar[int]
    ACADEMY: Institution.Type
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CHARTER: Institution.Governance
    COLLEGE: Institution.Type
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    GOVERNANCE_FIELD_NUMBER: _ClassVar[int]
    GYMNASIUM: Institution.Type
    ID_FIELD_NUMBER: _ClassVar[int]
    INSTITUTE: Institution.Type
    KINDERGARTEN: Institution.Type
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    LYCEUM: Institution.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_LOCALE_FIELD_NUMBER: _ClassVar[int]
    PRESCHOOL: Institution.Level
    PRIMARY: Institution.Level
    PRIVATE: Institution.Governance
    PUBLIC: Institution.Governance
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    SCHOOL: Institution.Type
    SECONDARY: Institution.Level
    TERTIARY: Institution.Level
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNIVERSITY: Institution.Type
    UNKNOWN_CLASS: Institution.Level
    UNKNOWN_GOVERNANCE: Institution.Governance
    UNKNOWN_TYPE: Institution.Type
    abbr: str
    abbr_local: str
    address: str
    country_id: str
    governance: Institution.Governance
    id: str
    level: Institution.Level
    links: _containers.ScalarMap[str, str]
    logo_url: str
    name: str
    name_locale: str
    region_id: str
    type: Institution.Type
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., name_locale: _Optional[str] = ..., abbr: _Optional[str] = ..., abbr_local: _Optional[str] = ..., logo_url: _Optional[str] = ..., governance: _Optional[_Union[Institution.Governance, str]] = ..., level: _Optional[_Union[Institution.Level, str]] = ..., type: _Optional[_Union[Institution.Type, str]] = ..., country_id: _Optional[str] = ..., region_id: _Optional[str] = ..., address: _Optional[str] = ..., links: _Optional[_Mapping[str, str]] = ...) -> None: ...
