from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Ticket(_message.Message):
    __slots__ = ["message", "metadata", "status", "subject", "type", "user_email", "user_id"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    APPROVED: Ticket.Status
    AWAITING: Ticket.Status
    CLOSED: Ticket.Status
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    NONE: Ticket.Type
    PENDING: Ticket.Status
    QUESTION: Ticket.Type
    QUOTA_INCREASE: Ticket.Type
    REJECTED: Ticket.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: Ticket.Status
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    message: str
    metadata: _containers.ScalarMap[str, str]
    status: Ticket.Status
    subject: str
    type: Ticket.Type
    user_email: str
    user_id: str
    def __init__(self, type: _Optional[_Union[Ticket.Type, str]] = ..., user_id: _Optional[str] = ..., user_email: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ..., status: _Optional[_Union[Ticket.Status, str]] = ..., subject: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
