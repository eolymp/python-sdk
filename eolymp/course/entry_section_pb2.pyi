from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Section(_message.Message):
    __slots__ = ["description", "image"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    description: _content_pb2.Content
    image: str
    def __init__(self, image: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
