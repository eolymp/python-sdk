from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Policy(_message.Message):
    __slots__ = ["name", "statements"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATEMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    statements: _containers.RepeatedCompositeFieldContainer[Statement]
    def __init__(self, name: _Optional[str] = ..., statements: _Optional[_Iterable[_Union[Statement, _Mapping]]] = ...) -> None: ...

class Statement(_message.Message):
    __slots__ = ["actions", "effect", "id", "principal", "resources"]
    class Effect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOW: Statement.Effect
    DENY: Statement.Effect
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NONE: Statement.Effect
    PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedScalarFieldContainer[str]
    effect: Statement.Effect
    id: str
    principal: str
    resources: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., effect: _Optional[_Union[Statement.Effect, str]] = ..., principal: _Optional[str] = ..., resources: _Optional[_Iterable[str]] = ..., actions: _Optional[_Iterable[str]] = ...) -> None: ...