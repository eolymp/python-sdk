from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Consent(_message.Message):
    __slots__ = ["id", "revocable", "set_on", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ACCEPTED: Consent.Status
    ID_FIELD_NUMBER: _ClassVar[int]
    PENDING: Consent.Status
    REJECTED: Consent.Status
    REVOCABLE_FIELD_NUMBER: _ClassVar[int]
    SET_ON_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    revocable: bool
    set_on: _timestamp_pb2.Timestamp
    status: Consent.Status
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[Consent.Status, str]] = ..., set_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., revocable: bool = ...) -> None: ...
