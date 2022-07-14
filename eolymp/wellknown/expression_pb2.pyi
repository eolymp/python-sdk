from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExpressionBool(_message.Message):
    __slots__ = ["value"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    EQUAL: ExpressionBool.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    NONE: ExpressionBool.Type
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ..., **kwargs) -> None: ...

class ExpressionEnum(_message.Message):
    __slots__ = ["value"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    EQUAL: ExpressionEnum.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    NONE: ExpressionEnum.Type
    NOT_EQUAL: ExpressionEnum.Type
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ..., **kwargs) -> None: ...

class ExpressionFloat(_message.Message):
    __slots__ = ["value"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    EQUAL: ExpressionFloat.Type
    GREATER_THAN: ExpressionFloat.Type
    GREATER_THAN_EQUAL: ExpressionFloat.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    LESS_THAN: ExpressionFloat.Type
    LESS_THAN_EQUAL: ExpressionFloat.Type
    NONE: ExpressionFloat.Type
    NOT_EQUAL: ExpressionFloat.Type
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ..., **kwargs) -> None: ...

class ExpressionID(_message.Message):
    __slots__ = ["value"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    EQUAL: ExpressionID.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    NONE: ExpressionID.Type
    NOT_EQUAL: ExpressionID.Type
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ..., **kwargs) -> None: ...

class ExpressionInt(_message.Message):
    __slots__ = ["value"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    EQUAL: ExpressionInt.Type
    GREATER_THAN: ExpressionInt.Type
    GREATER_THAN_EQUAL: ExpressionInt.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    LESS_THAN: ExpressionInt.Type
    LESS_THAN_EQUAL: ExpressionInt.Type
    NONE: ExpressionInt.Type
    NOT_EQUAL: ExpressionInt.Type
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ..., **kwargs) -> None: ...

class ExpressionString(_message.Message):
    __slots__ = ["value"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CONTAINING: ExpressionString.Type
    EQUAL: ExpressionString.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    NONE: ExpressionString.Type
    NOT_EQUAL: ExpressionString.Type
    STARTING: ExpressionString.Type
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ..., **kwargs) -> None: ...

class ExpressionTimestamp(_message.Message):
    __slots__ = ["value"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    EQUAL: ExpressionTimestamp.Type
    GREATER_THAN: ExpressionTimestamp.Type
    GREATER_THAN_EQUAL: ExpressionTimestamp.Type
    IS_FIELD_NUMBER: _ClassVar[int]
    LESS_THAN: ExpressionTimestamp.Type
    LESS_THAN_EQUAL: ExpressionTimestamp.Type
    NONE: ExpressionTimestamp.Type
    NOT_EQUAL: ExpressionTimestamp.Type
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _timestamp_pb2.Timestamp
    def __init__(self, value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...
