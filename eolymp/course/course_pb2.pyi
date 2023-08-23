from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Course(_message.Message):
    __slots__ = ["description", "duration", "estimate", "id", "image", "locale", "name", "topics", "url", "visibility"]
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NONE: Course.Visibility
    PRIVATE: Course.Visibility
    PUBLIC: Course.Visibility
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    UNLISTED: Course.Visibility
    URL_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    description: _content_pb2.Content
    duration: int
    estimate: int
    id: str
    image: str
    locale: str
    name: str
    topics: _containers.RepeatedScalarFieldContainer[str]
    url: str
    visibility: Course.Visibility
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., locale: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., image: _Optional[str] = ..., visibility: _Optional[_Union[Course.Visibility, str]] = ..., duration: _Optional[int] = ..., topics: _Optional[_Iterable[str]] = ..., estimate: _Optional[int] = ...) -> None: ...
