from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Course(_message.Message):
    __slots__ = ("id", "url", "locale", "name", "description", "image_url", "visibility", "duration", "topics", "estimate")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[Course.Extra]
        DESCRIPTION_VALUE: _ClassVar[Course.Extra]
        DESCRIPTION_RENDER: _ClassVar[Course.Extra]
    UNKNOWN_EXTRA: Course.Extra
    DESCRIPTION_VALUE: Course.Extra
    DESCRIPTION_RENDER: Course.Extra
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_VISIBILITY: _ClassVar[Course.Visibility]
        PUBLIC: _ClassVar[Course.Visibility]
        UNLISTED: _ClassVar[Course.Visibility]
        PRIVATE: _ClassVar[Course.Visibility]
    UNKNOWN_VISIBILITY: Course.Visibility
    PUBLIC: Course.Visibility
    UNLISTED: Course.Visibility
    PRIVATE: Course.Visibility
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    locale: str
    name: str
    description: _content_pb2.Content
    image_url: str
    visibility: Course.Visibility
    duration: int
    topics: _containers.RepeatedScalarFieldContainer[str]
    estimate: int
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., locale: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., image_url: _Optional[str] = ..., visibility: _Optional[_Union[Course.Visibility, str]] = ..., duration: _Optional[int] = ..., topics: _Optional[_Iterable[str]] = ..., estimate: _Optional[int] = ...) -> None: ...
