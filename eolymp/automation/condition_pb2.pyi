import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Condition(_message.Message):
    __slots__ = ("field", "logical", "string", "number", "timestamp", "bool", "list", "empty")
    class Logical(_message.Message):
        __slots__ = ("operator", "children")
        class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_OPERATOR: _ClassVar[Condition.Logical.Operator]
            AND: _ClassVar[Condition.Logical.Operator]
            OR: _ClassVar[Condition.Logical.Operator]
            NOT: _ClassVar[Condition.Logical.Operator]
        UNKNOWN_OPERATOR: Condition.Logical.Operator
        AND: Condition.Logical.Operator
        OR: Condition.Logical.Operator
        NOT: Condition.Logical.Operator
        OPERATOR_FIELD_NUMBER: _ClassVar[int]
        CHILDREN_FIELD_NUMBER: _ClassVar[int]
        operator: Condition.Logical.Operator
        children: _containers.RepeatedCompositeFieldContainer[Condition]
        def __init__(self, operator: _Optional[_Union[Condition.Logical.Operator, str]] = ..., children: _Optional[_Iterable[_Union[Condition, _Mapping]]] = ...) -> None: ...
    class String(_message.Message):
        __slots__ = ("operator", "value", "case_insensitive")
        class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_OPERATOR: _ClassVar[Condition.String.Operator]
            EQUAL: _ClassVar[Condition.String.Operator]
            NOT_EQUAL: _ClassVar[Condition.String.Operator]
            STARTS_WITH: _ClassVar[Condition.String.Operator]
            ENDS_WITH: _ClassVar[Condition.String.Operator]
            CONTAINS: _ClassVar[Condition.String.Operator]
            NOT_CONTAINS: _ClassVar[Condition.String.Operator]
        UNKNOWN_OPERATOR: Condition.String.Operator
        EQUAL: Condition.String.Operator
        NOT_EQUAL: Condition.String.Operator
        STARTS_WITH: Condition.String.Operator
        ENDS_WITH: Condition.String.Operator
        CONTAINS: Condition.String.Operator
        NOT_CONTAINS: Condition.String.Operator
        OPERATOR_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        CASE_INSENSITIVE_FIELD_NUMBER: _ClassVar[int]
        operator: Condition.String.Operator
        value: str
        case_insensitive: bool
        def __init__(self, operator: _Optional[_Union[Condition.String.Operator, str]] = ..., value: _Optional[str] = ..., case_insensitive: _Optional[bool] = ...) -> None: ...
    class Number(_message.Message):
        __slots__ = ("operator", "value")
        class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_OPERATOR: _ClassVar[Condition.Number.Operator]
            EQUAL: _ClassVar[Condition.Number.Operator]
            NOT_EQUAL: _ClassVar[Condition.Number.Operator]
            GREATER_THAN: _ClassVar[Condition.Number.Operator]
            GREATER_THAN_EQUAL: _ClassVar[Condition.Number.Operator]
            LESS_THAN: _ClassVar[Condition.Number.Operator]
            LESS_THAN_EQUAL: _ClassVar[Condition.Number.Operator]
        UNKNOWN_OPERATOR: Condition.Number.Operator
        EQUAL: Condition.Number.Operator
        NOT_EQUAL: Condition.Number.Operator
        GREATER_THAN: Condition.Number.Operator
        GREATER_THAN_EQUAL: Condition.Number.Operator
        LESS_THAN: Condition.Number.Operator
        LESS_THAN_EQUAL: Condition.Number.Operator
        OPERATOR_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        operator: Condition.Number.Operator
        value: float
        def __init__(self, operator: _Optional[_Union[Condition.Number.Operator, str]] = ..., value: _Optional[float] = ...) -> None: ...
    class Timestamp(_message.Message):
        __slots__ = ("operator", "value")
        class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_OPERATOR: _ClassVar[Condition.Timestamp.Operator]
            EQUAL: _ClassVar[Condition.Timestamp.Operator]
            NOT_EQUAL: _ClassVar[Condition.Timestamp.Operator]
            GREATER_THAN: _ClassVar[Condition.Timestamp.Operator]
            GREATER_THAN_EQUAL: _ClassVar[Condition.Timestamp.Operator]
            LESS_THAN: _ClassVar[Condition.Timestamp.Operator]
            LESS_THAN_EQUAL: _ClassVar[Condition.Timestamp.Operator]
        UNKNOWN_OPERATOR: Condition.Timestamp.Operator
        EQUAL: Condition.Timestamp.Operator
        NOT_EQUAL: Condition.Timestamp.Operator
        GREATER_THAN: Condition.Timestamp.Operator
        GREATER_THAN_EQUAL: Condition.Timestamp.Operator
        LESS_THAN: Condition.Timestamp.Operator
        LESS_THAN_EQUAL: Condition.Timestamp.Operator
        OPERATOR_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        operator: Condition.Timestamp.Operator
        value: _timestamp_pb2.Timestamp
        def __init__(self, operator: _Optional[_Union[Condition.Timestamp.Operator, str]] = ..., value: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Bool(_message.Message):
        __slots__ = ("operator", "value")
        class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_OPERATOR: _ClassVar[Condition.Bool.Operator]
            EQUAL: _ClassVar[Condition.Bool.Operator]
        UNKNOWN_OPERATOR: Condition.Bool.Operator
        EQUAL: Condition.Bool.Operator
        OPERATOR_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        operator: Condition.Bool.Operator
        value: bool
        def __init__(self, operator: _Optional[_Union[Condition.Bool.Operator, str]] = ..., value: _Optional[bool] = ...) -> None: ...
    class List(_message.Message):
        __slots__ = ("operator", "value")
        class Operator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_OPERATOR: _ClassVar[Condition.List.Operator]
            CONTAINS_ANY: _ClassVar[Condition.List.Operator]
            CONTAINS_ALL: _ClassVar[Condition.List.Operator]
            CONTAINS_NONE: _ClassVar[Condition.List.Operator]
        UNKNOWN_OPERATOR: Condition.List.Operator
        CONTAINS_ANY: Condition.List.Operator
        CONTAINS_ALL: Condition.List.Operator
        CONTAINS_NONE: Condition.List.Operator
        OPERATOR_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        operator: Condition.List.Operator
        value: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, operator: _Optional[_Union[Condition.List.Operator, str]] = ..., value: _Optional[_Iterable[str]] = ...) -> None: ...
    class Empty(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: bool
        def __init__(self, value: _Optional[bool] = ...) -> None: ...
    FIELD_FIELD_NUMBER: _ClassVar[int]
    LOGICAL_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_NUMBER: _ClassVar[int]
    LIST_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    field: str
    logical: Condition.Logical
    string: Condition.String
    number: Condition.Number
    timestamp: Condition.Timestamp
    bool: Condition.Bool
    list: Condition.List
    empty: Condition.Empty
    def __init__(self, field: _Optional[str] = ..., logical: _Optional[_Union[Condition.Logical, _Mapping]] = ..., string: _Optional[_Union[Condition.String, _Mapping]] = ..., number: _Optional[_Union[Condition.Number, _Mapping]] = ..., timestamp: _Optional[_Union[Condition.Timestamp, _Mapping]] = ..., bool: _Optional[_Union[Condition.Bool, _Mapping]] = ..., list: _Optional[_Union[Condition.List, _Mapping]] = ..., empty: _Optional[_Union[Condition.Empty, _Mapping]] = ...) -> None: ...
