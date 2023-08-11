from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Video(_message.Message):
    __slots__ = ["duration", "image_url", "video_url"]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    duration: int
    image_url: str
    video_url: str
    def __init__(self, image_url: _Optional[str] = ..., video_url: _Optional[str] = ..., duration: _Optional[int] = ...) -> None: ...
