from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Policy(_message.Message):
    __slots__ = ["id", "name", "principal", "scope", "statements"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    principal: str
    scope: str
    statements: _containers.RepeatedCompositeFieldContainer[Statement]
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., principal: _Optional[str] = ..., scope: _Optional[str] = ..., statements: _Optional[_Iterable[_Union[Statement, _Mapping]]] = ...) -> None: ...

class Statement(_message.Message):
    __slots__ = ["actions", "attributes", "effect", "id", "resource"]
    class Effect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class AttributesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOW: Statement.Effect
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DENY: Statement.Effect
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NONE: Statement.Effect
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]
    attributes: _containers.ScalarMap[str, str]
    effect: Statement.Effect
    id: str
    resource: str
    def __init__(self, id: _Optional[str] = ..., effect: _Optional[_Union[Statement.Effect, str]] = ..., resource: _Optional[str] = ..., actions: _Optional[_Iterable[str]] = ..., attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...
