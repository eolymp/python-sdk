from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Fragment(_message.Message):
    __slots__ = ["content", "id", "labels", "locale", "path", "title"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_RENDER: Fragment.Extra
    CONTENT_VALUE: Fragment.Extra
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NO_EXTRA: Fragment.Extra
    PATH_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    content: _content_pb2.Content
    id: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    locale: str
    path: str
    title: str
    def __init__(self, id: _Optional[str] = ..., path: _Optional[str] = ..., locale: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...
