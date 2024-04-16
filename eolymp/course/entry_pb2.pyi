from eolymp.course import entry_problem_pb2 as _entry_problem_pb2
from eolymp.course import entry_section_pb2 as _entry_section_pb2
from eolymp.course import entry_video_pb2 as _entry_video_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Entry(_message.Message):
    __slots__ = ["document", "draft", "estimate", "id", "index", "items", "parent_id", "problem", "section", "title", "url", "video", "weight"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CONTENT: Entry.Extra
    CONTENT_RENDER: Entry.Extra
    CONTENT_VALUE: Entry.Extra
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_FIELD_NUMBER: _ClassVar[int]
    SECTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Entry.Extra
    URL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    document: _content_pb2.Content
    draft: bool
    estimate: int
    id: str
    index: int
    items: _containers.RepeatedCompositeFieldContainer[Entry]
    parent_id: str
    problem: _entry_problem_pb2.Problem
    section: _entry_section_pb2.Section
    title: str
    url: str
    video: _entry_video_pb2.Video
    weight: int
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., title: _Optional[str] = ..., draft: bool = ..., parent_id: _Optional[str] = ..., index: _Optional[int] = ..., estimate: _Optional[int] = ..., weight: _Optional[int] = ..., section: _Optional[_Union[_entry_section_pb2.Section, _Mapping]] = ..., document: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., video: _Optional[_Union[_entry_video_pb2.Video, _Mapping]] = ..., problem: _Optional[_Union[_entry_problem_pb2.Problem, _Mapping]] = ..., items: _Optional[_Iterable[_Union[Entry, _Mapping]]] = ...) -> None: ...
