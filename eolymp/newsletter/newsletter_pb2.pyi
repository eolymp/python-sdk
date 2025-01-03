from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Newsletter(_message.Message):
    __slots__ = ["id", "created_at", "subject", "content"]
    class Translation(_message.Message):
        __slots__ = ["id", "locale", "subject", "content"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        id: str
        locale: str
        subject: str
        content: _content_pb2.Content
        def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., subject: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    subject: str
    content: _content_pb2.Content
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., subject: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
