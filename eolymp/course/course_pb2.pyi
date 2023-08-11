from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Course(_message.Message):
    __slots__ = ["description", "duration_estimate", "id", "locale", "name", "picture"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DURATION_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    description: _content_pb2.Content
    duration_estimate: int
    id: str
    locale: str
    name: str
    picture: str
    def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., picture: _Optional[str] = ..., duration_estimate: _Optional[int] = ...) -> None: ...
