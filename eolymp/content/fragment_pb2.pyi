from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Fragment(_message.Message):
    __slots__ = ["content", "created_at", "draft", "id", "labels", "locale", "path", "title", "updated_at"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_RENDER: Fragment.Extra
    CONTENT_VALUE: Fragment.Extra
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NO_EXTRA: Fragment.Extra
    PATCH_ALL: Fragment.Patch
    PATCH_CONTENT: Fragment.Patch
    PATCH_DRAFT: Fragment.Patch
    PATCH_LABELS: Fragment.Patch
    PATCH_LOCALE: Fragment.Patch
    PATCH_PATH: Fragment.Patch
    PATCH_TITLE: Fragment.Patch
    PATH_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_PATCH: Fragment.Patch
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    content: _content_pb2.Content
    created_at: _timestamp_pb2.Timestamp
    draft: bool
    id: str
    labels: _containers.RepeatedScalarFieldContainer[str]
    locale: str
    path: str
    title: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., path: _Optional[str] = ..., locale: _Optional[str] = ..., draft: bool = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., labels: _Optional[_Iterable[str]] = ...) -> None: ...
