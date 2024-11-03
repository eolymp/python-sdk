from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ["device", "first_seen_at", "id", "ip_address", "last_seen_at", "location", "user_agent"]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_AT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    device: str
    first_seen_at: _timestamp_pb2.Timestamp
    id: str
    ip_address: str
    last_seen_at: _timestamp_pb2.Timestamp
    location: str
    user_agent: str
    def __init__(self, id: _Optional[str] = ..., user_agent: _Optional[str] = ..., device: _Optional[str] = ..., location: _Optional[str] = ..., ip_address: _Optional[str] = ..., first_seen_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_seen_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
