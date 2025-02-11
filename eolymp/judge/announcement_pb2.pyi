from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Announcement(_message.Message):
    __slots__ = ("id", "contest_id", "created_at", "subject", "message")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTRA: _ClassVar[Announcement.Extra]
        MESSAGE_RENDER: _ClassVar[Announcement.Extra]
        MESSAGE_VALUE: _ClassVar[Announcement.Extra]
    NO_EXTRA: Announcement.Extra
    MESSAGE_RENDER: Announcement.Extra
    MESSAGE_VALUE: Announcement.Extra
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    contest_id: str
    created_at: _timestamp_pb2.Timestamp
    subject: str
    message: _content_pb2.Content
    def __init__(self, id: _Optional[str] = ..., contest_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., subject: _Optional[str] = ..., message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
