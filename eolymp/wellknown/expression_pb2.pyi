from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExpressionID(_message.Message):
    __slots__ = ("value",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ExpressionID.Type]
        EQUAL: _ClassVar[ExpressionID.Type]
        NOT_EQUAL: _ClassVar[ExpressionID.Type]
    NONE: ExpressionID.Type
    EQUAL: ExpressionID.Type
    NOT_EQUAL: ExpressionID.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ..., **kwargs) -> None: ...

class ExpressionInt(_message.Message):
    __slots__ = ("value",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ExpressionInt.Type]
        EQUAL: _ClassVar[ExpressionInt.Type]
        NOT_EQUAL: _ClassVar[ExpressionInt.Type]
        GREATER_THAN: _ClassVar[ExpressionInt.Type]
        GREATER_THAN_EQUAL: _ClassVar[ExpressionInt.Type]
        LESS_THAN: _ClassVar[ExpressionInt.Type]
        LESS_THAN_EQUAL: _ClassVar[ExpressionInt.Type]
    NONE: ExpressionInt.Type
    EQUAL: ExpressionInt.Type
    NOT_EQUAL: ExpressionInt.Type
    GREATER_THAN: ExpressionInt.Type
    GREATER_THAN_EQUAL: ExpressionInt.Type
    LESS_THAN: ExpressionInt.Type
    LESS_THAN_EQUAL: ExpressionInt.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ..., **kwargs) -> None: ...

class ExpressionFloat(_message.Message):
    __slots__ = ("value",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ExpressionFloat.Type]
        EQUAL: _ClassVar[ExpressionFloat.Type]
        NOT_EQUAL: _ClassVar[ExpressionFloat.Type]
        GREATER_THAN: _ClassVar[ExpressionFloat.Type]
        GREATER_THAN_EQUAL: _ClassVar[ExpressionFloat.Type]
        LESS_THAN: _ClassVar[ExpressionFloat.Type]
        LESS_THAN_EQUAL: _ClassVar[ExpressionFloat.Type]
    NONE: ExpressionFloat.Type
    EQUAL: ExpressionFloat.Type
    NOT_EQUAL: ExpressionFloat.Type
    GREATER_THAN: ExpressionFloat.Type
    GREATER_THAN_EQUAL: ExpressionFloat.Type
    LESS_THAN: ExpressionFloat.Type
    LESS_THAN_EQUAL: ExpressionFloat.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ..., **kwargs) -> None: ...

class ExpressionString(_message.Message):
    __slots__ = ("value",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ExpressionString.Type]
        EQUAL: _ClassVar[ExpressionString.Type]
        NOT_EQUAL: _ClassVar[ExpressionString.Type]
        CONTAINING: _ClassVar[ExpressionString.Type]
        STARTING: _ClassVar[ExpressionString.Type]
    NONE: ExpressionString.Type
    EQUAL: ExpressionString.Type
    NOT_EQUAL: ExpressionString.Type
    CONTAINING: ExpressionString.Type
    STARTING: ExpressionString.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ..., **kwargs) -> None: ...

class ExpressionEnum(_message.Message):
    __slots__ = ("value",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ExpressionEnum.Type]
        EQUAL: _ClassVar[ExpressionEnum.Type]
        NOT_EQUAL: _ClassVar[ExpressionEnum.Type]
    NONE: ExpressionEnum.Type
    EQUAL: ExpressionEnum.Type
    NOT_EQUAL: ExpressionEnum.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ..., **kwargs) -> None: ...

class ExpressionBool(_message.Message):
    __slots__ = ("value",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ExpressionBool.Type]
        EQUAL: _ClassVar[ExpressionBool.Type]
    NONE: ExpressionBool.Type
    EQUAL: ExpressionBool.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ..., **kwargs) -> None: ...

class ExpressionTimestamp(_message.Message):
    __slots__ = ("value",)
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[ExpressionTimestamp.Type]
        EQUAL: _ClassVar[ExpressionTimestamp.Type]
        NOT_EQUAL: _ClassVar[ExpressionTimestamp.Type]
        GREATER_THAN: _ClassVar[ExpressionTimestamp.Type]
        GREATER_THAN_EQUAL: _ClassVar[ExpressionTimestamp.Type]
        LESS_THAN: _ClassVar[ExpressionTimestamp.Type]
        LESS_THAN_EQUAL: _ClassVar[ExpressionTimestamp.Type]
    NONE: ExpressionTimestamp.Type
    EQUAL: ExpressionTimestamp.Type
    NOT_EQUAL: ExpressionTimestamp.Type
    GREATER_THAN: ExpressionTimestamp.Type
    GREATER_THAN_EQUAL: ExpressionTimestamp.Type
    LESS_THAN: ExpressionTimestamp.Type
    LESS_THAN_EQUAL: ExpressionTimestamp.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _timestamp_pb2.Timestamp
    def __init__(self, value: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...
