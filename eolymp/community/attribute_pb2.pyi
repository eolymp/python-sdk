from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Attribute(_message.Message):
    __slots__ = ["choices", "constraints", "country", "description", "help", "hidden", "index", "key", "label", "max", "min", "readonly", "regexp", "required", "type", "visibility"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Description(_message.Message):
        __slots__ = ["choices", "help", "label", "locale"]
        CHOICES_FIELD_NUMBER: _ClassVar[int]
        HELP_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        choices: _containers.RepeatedScalarFieldContainer[str]
        help: str
        label: str
        locale: str
        def __init__(self, locale: _Optional[str] = ..., label: _Optional[str] = ..., help: _Optional[str] = ..., choices: _Optional[_Iterable[str]] = ...) -> None: ...
    class Value(_message.Message):
        __slots__ = ["attribute_key", "attribute_type", "number", "string"]
        ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        STRING_FIELD_NUMBER: _ClassVar[int]
        attribute_key: str
        attribute_type: Attribute.Type
        number: int
        string: str
        def __init__(self, attribute_key: _Optional[str] = ..., attribute_type: _Optional[_Union[Attribute.Type, str]] = ..., string: _Optional[str] = ..., number: _Optional[int] = ...) -> None: ...
    CHECKBOX: Attribute.Type
    CHOICE: Attribute.Type
    CHOICES_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY: Attribute.Type
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DATE: Attribute.Type
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EMAIL: Attribute.Type
    FILE: Attribute.Type
    HELP_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    IMAGE: Attribute.Type
    INDEX_FIELD_NUMBER: _ClassVar[int]
    INSTITUTION: Attribute.Type
    INTERNAL: Attribute.Visibility
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    NUMBER: Attribute.Type
    PRIVATE: Attribute.Visibility
    PUBLIC: Attribute.Visibility
    READONLY_FIELD_NUMBER: _ClassVar[int]
    REGEXP_FIELD_NUMBER: _ClassVar[int]
    REGION: Attribute.Type
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    STRING: Attribute.Type
    TEXT: Attribute.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: Attribute.Type
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    choices: _containers.RepeatedScalarFieldContainer[str]
    constraints: _containers.RepeatedScalarFieldContainer[str]
    country: str
    description: _containers.RepeatedCompositeFieldContainer[Attribute.Description]
    help: str
    hidden: bool
    index: int
    key: str
    label: str
    max: int
    min: int
    readonly: bool
    regexp: str
    required: bool
    type: Attribute.Type
    visibility: Attribute.Visibility
    def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., help: _Optional[str] = ..., description: _Optional[_Iterable[_Union[Attribute.Description, _Mapping]]] = ..., type: _Optional[_Union[Attribute.Type, str]] = ..., index: _Optional[int] = ..., required: bool = ..., readonly: bool = ..., hidden: bool = ..., visibility: _Optional[_Union[Attribute.Visibility, str]] = ..., regexp: _Optional[str] = ..., min: _Optional[int] = ..., max: _Optional[int] = ..., choices: _Optional[_Iterable[str]] = ..., country: _Optional[str] = ..., constraints: _Optional[_Iterable[str]] = ...) -> None: ...
