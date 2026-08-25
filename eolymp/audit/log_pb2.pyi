import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Log(_message.Message):
    __slots__ = ("timestamp", "subject", "ip_address", "user_agent", "method", "scope", "mutation", "operation", "payload")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_OPERATION: _ClassVar[Log.Operation]
        READ: _ClassVar[Log.Operation]
        WRITE: _ClassVar[Log.Operation]
        DELETE: _ClassVar[Log.Operation]
    UNKNOWN_OPERATION: Log.Operation
    READ: Log.Operation
    WRITE: Log.Operation
    DELETE: Log.Operation
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_EXTRA: _ClassVar[Log.Extra.Field]
            PAYLOAD: _ClassVar[Log.Extra.Field]
        UNKNOWN_EXTRA: Log.Extra.Field
        PAYLOAD: Log.Extra.Field
        def __init__(self) -> None: ...
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    MUTATION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    subject: str
    ip_address: str
    user_agent: str
    method: str
    scope: str
    mutation: bool
    operation: Log.Operation
    payload: str
    def __init__(self, timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., subject: _Optional[str] = ..., ip_address: _Optional[str] = ..., user_agent: _Optional[str] = ..., method: _Optional[str] = ..., scope: _Optional[str] = ..., mutation: _Optional[bool] = ..., operation: _Optional[_Union[Log.Operation, str]] = ..., payload: _Optional[str] = ...) -> None: ...
