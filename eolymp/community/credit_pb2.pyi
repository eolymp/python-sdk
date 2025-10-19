import datetime

from eolymp.annotations import mcp_pb2 as _mcp_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Credit(_message.Message):
    __slots__ = ()
    class Grant(_message.Message):
        __slots__ = ("id", "reference", "note", "active", "revoked", "total_amount", "redeemed_amount", "granted_at", "expires_at")
        ID_FIELD_NUMBER: _ClassVar[int]
        REFERENCE_FIELD_NUMBER: _ClassVar[int]
        NOTE_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        REVOKED_FIELD_NUMBER: _ClassVar[int]
        TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        REDEEMED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        GRANTED_AT_FIELD_NUMBER: _ClassVar[int]
        EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
        id: str
        reference: str
        note: str
        active: bool
        revoked: bool
        total_amount: int
        redeemed_amount: int
        granted_at: _timestamp_pb2.Timestamp
        expires_at: _timestamp_pb2.Timestamp
        def __init__(self, id: _Optional[str] = ..., reference: _Optional[str] = ..., note: _Optional[str] = ..., active: bool = ..., revoked: bool = ..., total_amount: _Optional[int] = ..., redeemed_amount: _Optional[int] = ..., granted_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    class Transaction(_message.Message):
        __slots__ = ("id", "timestamp", "summary", "amount")
        ID_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        id: str
        timestamp: _timestamp_pb2.Timestamp
        summary: str
        amount: int
        def __init__(self, id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., summary: _Optional[str] = ..., amount: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
