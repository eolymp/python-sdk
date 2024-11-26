from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Statement(_message.Message):
    __slots__ = ["author", "author_id", "automatic", "content", "download_link", "draft", "id", "locale", "source", "title"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_RENDER: Statement.Extra
    CONTENT_VALUE: Statement.Extra
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PATCH_ALL: Statement.Patch
    PATCH_AUTHOR: Statement.Patch
    PATCH_AUTHOR_ID: Statement.Patch
    PATCH_AUTOMATIC: Statement.Patch
    PATCH_CONTENT: Statement.Patch
    PATCH_DOWNLOAD_LINK: Statement.Patch
    PATCH_DRAFT: Statement.Patch
    PATCH_LOCALE: Statement.Patch
    PATCH_SOURCE: Statement.Patch
    PATCH_TITLE: Statement.Patch
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Statement.Extra
    UNKNOWN_PATCH: Statement.Patch
    author: str
    author_id: str
    automatic: bool
    content: _content_pb2.Content
    download_link: str
    draft: bool
    id: str
    locale: str
    source: str
    title: str
    def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., automatic: bool = ..., draft: bool = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., download_link: _Optional[str] = ..., author: _Optional[str] = ..., source: _Optional[str] = ..., author_id: _Optional[str] = ...) -> None: ...
