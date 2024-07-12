from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Achievement(_message.Message):
    __slots__ = ["id", "image_url", "name", "summary", "value"]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    image_url: str
    name: str
    summary: _content_pb2.Content
    value: int
    def __init__(self, id: _Optional[str] = ..., value: _Optional[int] = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., summary: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
