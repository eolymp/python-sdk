import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Log(_message.Message):
    __slots__ = ("timestamp", "actor", "ip_address", "user_agent", "method", "scope", "mutation", "payload")
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_EXTRA: _ClassVar[Log.Extra.Field]
            PAYLOAD: _ClassVar[Log.Extra.Field]
        UNKNOWN_EXTRA: Log.Extra.Field
        PAYLOAD: Log.Extra.Field
        def __init__(self) -> None: ...
    class Actor(_message.Message):
        __slots__ = ("type", "id", "subject")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_TYPE: _ClassVar[Log.Actor.Type]
            MEMBER: _ClassVar[Log.Actor.Type]
            USER: _ClassVar[Log.Actor.Type]
            SERVICE: _ClassVar[Log.Actor.Type]
        UNKNOWN_TYPE: Log.Actor.Type
        MEMBER: Log.Actor.Type
        USER: Log.Actor.Type
        SERVICE: Log.Actor.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        type: Log.Actor.Type
        id: str
        subject: str
        def __init__(self, type: _Optional[_Union[Log.Actor.Type, str]] = ..., id: _Optional[str] = ..., subject: _Optional[str] = ...) -> None: ...
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    MUTATION_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    actor: Log.Actor
    ip_address: str
    user_agent: str
    method: str
    scope: str
    mutation: bool
    payload: str
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., actor: _Optional[_Union[Log.Actor, _Mapping]] = ..., ip_address: _Optional[str] = ..., user_agent: _Optional[str] = ..., method: _Optional[str] = ..., scope: _Optional[str] = ..., mutation: _Optional[bool] = ..., payload: _Optional[str] = ...) -> None: ...
