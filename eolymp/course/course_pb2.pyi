from eolymp.course import assignment_pb2 as _assignment_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Course(_message.Message):
    __slots__ = ["assignment", "description", "duration", "estimate", "id", "image", "locale", "name", "participation_mode", "topics", "url", "visibility"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ParticipationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ASSIGNMENT: Course.Extra
    ASSIGNMENT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_RENDER: Course.Extra
    DESCRIPTION_VALUE: Course.Extra
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MODERATED: Course.ParticipationMode
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTICIPATION_MODE_FIELD_NUMBER: _ClassVar[int]
    PRIVATE: Course.Visibility
    PUBLIC: Course.Visibility
    SELF_PACED: Course.ParticipationMode
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Course.Extra
    UNKNOWN_PARTICIPATION_MODE: Course.ParticipationMode
    UNKNOWN_VISIBILITY: Course.Visibility
    UNLISTED: Course.Visibility
    URL_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    assignment: _assignment_pb2.Assignment
    description: _content_pb2.Content
    duration: int
    estimate: int
    id: str
    image: str
    locale: str
    name: str
    participation_mode: Course.ParticipationMode
    topics: _containers.RepeatedScalarFieldContainer[str]
    url: str
    visibility: Course.Visibility
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., locale: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., image: _Optional[str] = ..., visibility: _Optional[_Union[Course.Visibility, str]] = ..., duration: _Optional[int] = ..., topics: _Optional[_Iterable[str]] = ..., estimate: _Optional[int] = ..., participation_mode: _Optional[_Union[Course.ParticipationMode, str]] = ..., assignment: _Optional[_Union[_assignment_pb2.Assignment, _Mapping]] = ...) -> None: ...
