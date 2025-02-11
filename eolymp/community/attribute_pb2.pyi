from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Attribute(_message.Message):
    __slots__ = ("id", "key", "label", "help", "type", "index", "required", "readonly", "hidden", "visibility", "regexp", "min", "max", "choices", "country", "constraints")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PATCH_ALL: _ClassVar[Attribute.Patch]
        PATCH_LABEL: _ClassVar[Attribute.Patch]
        PATCH_HELP: _ClassVar[Attribute.Patch]
        PATCH_TYPE: _ClassVar[Attribute.Patch]
        PATCH_INDEX: _ClassVar[Attribute.Patch]
        PATCH_REQUIRED: _ClassVar[Attribute.Patch]
        PATCH_READONLY: _ClassVar[Attribute.Patch]
        PATCH_VISIBILITY: _ClassVar[Attribute.Patch]
        PATCH_REGEXP: _ClassVar[Attribute.Patch]
        PATCH_MIN: _ClassVar[Attribute.Patch]
        PATCH_MAX: _ClassVar[Attribute.Patch]
        PATCH_CHOICES: _ClassVar[Attribute.Patch]
        PATCH_CONSTRAINTS: _ClassVar[Attribute.Patch]
    PATCH_ALL: Attribute.Patch
    PATCH_LABEL: Attribute.Patch
    PATCH_HELP: Attribute.Patch
    PATCH_TYPE: Attribute.Patch
    PATCH_INDEX: Attribute.Patch
    PATCH_REQUIRED: Attribute.Patch
    PATCH_READONLY: Attribute.Patch
    PATCH_VISIBILITY: Attribute.Patch
    PATCH_REGEXP: Attribute.Patch
    PATCH_MIN: Attribute.Patch
    PATCH_MAX: Attribute.Patch
    PATCH_CHOICES: Attribute.Patch
    PATCH_CONSTRAINTS: Attribute.Patch
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_TYPE: _ClassVar[Attribute.Type]
        STRING: _ClassVar[Attribute.Type]
        TEXT: _ClassVar[Attribute.Type]
        NUMBER: _ClassVar[Attribute.Type]
        CHOICE: _ClassVar[Attribute.Type]
        DATE: _ClassVar[Attribute.Type]
        EMAIL: _ClassVar[Attribute.Type]
        CHECKBOX: _ClassVar[Attribute.Type]
        COUNTRY: _ClassVar[Attribute.Type]
        REGION: _ClassVar[Attribute.Type]
        INSTITUTION: _ClassVar[Attribute.Type]
        IMAGE: _ClassVar[Attribute.Type]
        FILE: _ClassVar[Attribute.Type]
    UNKNOWN_TYPE: Attribute.Type
    STRING: Attribute.Type
    TEXT: Attribute.Type
    NUMBER: Attribute.Type
    CHOICE: Attribute.Type
    DATE: Attribute.Type
    EMAIL: Attribute.Type
    CHECKBOX: Attribute.Type
    COUNTRY: Attribute.Type
    REGION: Attribute.Type
    INSTITUTION: Attribute.Type
    IMAGE: Attribute.Type
    FILE: Attribute.Type
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_VISIBILITY: _ClassVar[Attribute.Visibility]
        PRIVATE: _ClassVar[Attribute.Visibility]
        PUBLIC: _ClassVar[Attribute.Visibility]
        INTERNAL: _ClassVar[Attribute.Visibility]
    UNKNOWN_VISIBILITY: Attribute.Visibility
    PRIVATE: Attribute.Visibility
    PUBLIC: Attribute.Visibility
    INTERNAL: Attribute.Visibility
    class Description(_message.Message):
        __slots__ = ("locale", "label", "help", "choices")
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        HELP_FIELD_NUMBER: _ClassVar[int]
        CHOICES_FIELD_NUMBER: _ClassVar[int]
        locale: str
        label: str
        help: str
        choices: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, locale: _Optional[str] = ..., label: _Optional[str] = ..., help: _Optional[str] = ..., choices: _Optional[_Iterable[str]] = ...) -> None: ...
    class Value(_message.Message):
        __slots__ = ("attribute_key", "attribute_type", "string", "number")
        ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
        STRING_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        attribute_key: str
        attribute_type: Attribute.Type
        string: str
        number: int
        def __init__(self, attribute_key: _Optional[str] = ..., attribute_type: _Optional[_Union[Attribute.Type, str]] = ..., string: _Optional[str] = ..., number: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    HELP_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    READONLY_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    REGEXP_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    CHOICES_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    key: str
    label: str
    help: str
    type: Attribute.Type
    index: int
    required: bool
    readonly: bool
    hidden: bool
    visibility: Attribute.Visibility
    regexp: str
    min: int
    max: int
    choices: _containers.RepeatedScalarFieldContainer[str]
    country: str
    constraints: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., label: _Optional[str] = ..., help: _Optional[str] = ..., type: _Optional[_Union[Attribute.Type, str]] = ..., index: _Optional[int] = ..., required: bool = ..., readonly: bool = ..., hidden: bool = ..., visibility: _Optional[_Union[Attribute.Visibility, str]] = ..., regexp: _Optional[str] = ..., min: _Optional[int] = ..., max: _Optional[int] = ..., choices: _Optional[_Iterable[str]] = ..., country: _Optional[str] = ..., constraints: _Optional[_Iterable[str]] = ...) -> None: ...
