from eolymp.annotations import resource_pb2 as _resource_pb2
from eolymp.community import attribute_pb2 as _attribute_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Member(_message.Message):
    __slots__ = ["disabled", "ern", "ghost", "id", "name", "out_of_competition", "registered", "staffed", "status", "users", "values"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class User(_message.Message):
        __slots__ = ["user_id"]
        USER_ID_FIELD_NUMBER: _ClassVar[int]
        user_id: str
        def __init__(self, user_id: _Optional[str] = ...) -> None: ...
    class Value(_message.Message):
        __slots__ = ["attribute_key", "attribute_type", "value_number", "value_string"]
        ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        VALUE_STRING_FIELD_NUMBER: _ClassVar[int]
        attribute_key: str
        attribute_type: _attribute_pb2.Attribute.Type
        value_number: int
        value_string: str
        def __init__(self, attribute_key: _Optional[str] = ..., attribute_type: _Optional[_Union[_attribute_pb2.Attribute.Type, str]] = ..., value_string: _Optional[str] = ..., value_number: _Optional[int] = ...) -> None: ...
    ACTIVE: Member.Status
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    ERN_FIELD_NUMBER: _ClassVar[int]
    GHOST: Member.Status
    GHOST_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INACTIVE: Member.Status
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_COMPETITION_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_FIELD_NUMBER: _ClassVar[int]
    STAFFED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_STATUS: Member.Status
    UNREGISTERED: Member.Status
    UNSTAFFED: Member.Status
    USERS_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    ern: str
    ghost: bool
    id: str
    name: str
    out_of_competition: bool
    registered: bool
    staffed: bool
    status: Member.Status
    users: _containers.RepeatedCompositeFieldContainer[Member.User]
    values: _containers.RepeatedCompositeFieldContainer[Member.Value]
    def __init__(self, id: _Optional[str] = ..., ern: _Optional[str] = ..., name: _Optional[str] = ..., disabled: bool = ..., registered: bool = ..., staffed: bool = ..., ghost: bool = ..., out_of_competition: bool = ..., status: _Optional[_Union[Member.Status, str]] = ..., users: _Optional[_Iterable[_Union[Member.User, _Mapping]]] = ..., values: _Optional[_Iterable[_Union[Member.Value, _Mapping]]] = ...) -> None: ...
