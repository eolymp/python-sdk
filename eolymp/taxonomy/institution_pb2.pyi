from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Institution(_message.Message):
    __slots__ = ("id", "name", "acronym", "local_name", "local_acronym", "logo_url", "governance", "level", "type", "country_id", "region_id", "address", "links")
    class Governance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_GOVERNANCE: _ClassVar[Institution.Governance]
        PUBLIC: _ClassVar[Institution.Governance]
        PRIVATE: _ClassVar[Institution.Governance]
        CHARTER: _ClassVar[Institution.Governance]
    UNKNOWN_GOVERNANCE: Institution.Governance
    PUBLIC: Institution.Governance
    PRIVATE: Institution.Governance
    CHARTER: Institution.Governance
    class Level(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_LEVEL: _ClassVar[Institution.Level]
        PRESCHOOL: _ClassVar[Institution.Level]
        PRIMARY: _ClassVar[Institution.Level]
        SECONDARY: _ClassVar[Institution.Level]
        TERTIARY: _ClassVar[Institution.Level]
    UNKNOWN_LEVEL: Institution.Level
    PRESCHOOL: Institution.Level
    PRIMARY: Institution.Level
    SECONDARY: Institution.Level
    TERTIARY: Institution.Level
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TYPE: _ClassVar[Institution.Type]
        KINDERGARTEN: _ClassVar[Institution.Type]
        SCHOOL: _ClassVar[Institution.Type]
        LYCEUM: _ClassVar[Institution.Type]
        GYMNASIUM: _ClassVar[Institution.Type]
        COLLEGE: _ClassVar[Institution.Type]
        INSTITUTE: _ClassVar[Institution.Type]
        UNIVERSITY: _ClassVar[Institution.Type]
        ACADEMY: _ClassVar[Institution.Type]
    UNKNOWN_TYPE: Institution.Type
    KINDERGARTEN: Institution.Type
    SCHOOL: Institution.Type
    LYCEUM: Institution.Type
    GYMNASIUM: Institution.Type
    COLLEGE: Institution.Type
    INSTITUTE: Institution.Type
    UNIVERSITY: Institution.Type
    ACADEMY: Institution.Type
    class LinksEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACRONYM_FIELD_NUMBER: _ClassVar[int]
    LOCAL_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCAL_ACRONYM_FIELD_NUMBER: _ClassVar[int]
    LOGO_URL_FIELD_NUMBER: _ClassVar[int]
    GOVERNANCE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_ID_FIELD_NUMBER: _ClassVar[int]
    REGION_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    acronym: str
    local_name: str
    local_acronym: str
    logo_url: str
    governance: Institution.Governance
    level: Institution.Level
    type: Institution.Type
    country_id: str
    region_id: str
    address: str
    links: _containers.ScalarMap[str, str]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., acronym: _Optional[str] = ..., local_name: _Optional[str] = ..., local_acronym: _Optional[str] = ..., logo_url: _Optional[str] = ..., governance: _Optional[_Union[Institution.Governance, str]] = ..., level: _Optional[_Union[Institution.Level, str]] = ..., type: _Optional[_Union[Institution.Type, str]] = ..., country_id: _Optional[str] = ..., region_id: _Optional[str] = ..., address: _Optional[str] = ..., links: _Optional[_Mapping[str, str]] = ...) -> None: ...
