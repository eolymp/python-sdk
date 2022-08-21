from eolymp.annotations import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Attribute(_message.Message):
    __slots__ = ["choices", "country", "description", "ern", "hidden", "index", "key", "max", "min", "regexp", "required", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Description(_message.Message):
        __slots__ = ["choices", "default", "help", "label", "locale"]
        CHOICES_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_FIELD_NUMBER: _ClassVar[int]
        HELP_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        choices: _containers.RepeatedScalarFieldContainer[str]
        default: bool
        help: str
        label: str
        locale: str
        def __init__(self, default: bool = ..., locale: _Optional[str] = ..., label: _Optional[str] = ..., help: _Optional[str] = ..., choices: _Optional[_Iterable[str]] = ...) -> None: ...
    CHECKBOX: Attribute.Type
    CHOICE: Attribute.Type
    CHOICES_FIELD_NUMBER: _ClassVar[int]
    COUNTRY: Attribute.Type
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    DATE: Attribute.Type
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EMAIL: Attribute.Type
    ERN_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    NUMBER: Attribute.Type
    REGEXP_FIELD_NUMBER: _ClassVar[int]
    REGION: Attribute.Type
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    STRING: Attribute.Type
    TEXT: Attribute.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: Attribute.Type
    choices: _containers.RepeatedScalarFieldContainer[str]
    country: str
    description: _containers.RepeatedCompositeFieldContainer[Attribute.Description]
    ern: str
    hidden: bool
    index: int
    key: str
    max: int
    min: int
    regexp: str
    required: bool
    type: Attribute.Type
    def __init__(self, key: _Optional[str] = ..., ern: _Optional[str] = ..., description: _Optional[_Iterable[_Union[Attribute.Description, _Mapping]]] = ..., type: _Optional[_Union[Attribute.Type, str]] = ..., index: _Optional[int] = ..., required: bool = ..., hidden: bool = ..., regexp: _Optional[str] = ..., min: _Optional[int] = ..., max: _Optional[int] = ..., choices: _Optional[_Iterable[str]] = ..., country: _Optional[str] = ...) -> None: ...
