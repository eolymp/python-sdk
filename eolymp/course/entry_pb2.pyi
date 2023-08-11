from eolymp.course import entry_section_pb2 as _entry_section_pb2
from eolymp.course import entry_video_pb2 as _entry_video_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Entry(_message.Message):
    __slots__ = ["depth", "document", "duration_estimate", "id", "parent_id", "section", "title", "video"]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    DURATION_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    SECTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    depth: int
    document: _content_pb2.Content
    duration_estimate: int
    id: str
    parent_id: str
    section: _entry_section_pb2.Section
    title: str
    video: _entry_video_pb2.Video
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., parent_id: _Optional[str] = ..., depth: _Optional[int] = ..., duration_estimate: _Optional[int] = ..., section: _Optional[_Union[_entry_section_pb2.Section, _Mapping]] = ..., document: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., video: _Optional[_Union[_entry_video_pb2.Video, _Mapping]] = ...) -> None: ...
