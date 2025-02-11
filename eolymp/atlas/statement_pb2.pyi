from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Statement(_message.Message):
    __slots__ = ("id", "locale", "automatic", "draft", "title", "content", "download_link", "author", "source", "author_id")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_EXTRA: _ClassVar[Statement.Extra]
        CONTENT_RENDER: _ClassVar[Statement.Extra]
        CONTENT_VALUE: _ClassVar[Statement.Extra]
    UNKNOWN_EXTRA: Statement.Extra
    CONTENT_RENDER: Statement.Extra
    CONTENT_VALUE: Statement.Extra
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_PATCH: _ClassVar[Statement.Patch]
        PATCH_ALL: _ClassVar[Statement.Patch]
        PATCH_LOCALE: _ClassVar[Statement.Patch]
        PATCH_AUTOMATIC: _ClassVar[Statement.Patch]
        PATCH_DRAFT: _ClassVar[Statement.Patch]
        PATCH_TITLE: _ClassVar[Statement.Patch]
        PATCH_CONTENT: _ClassVar[Statement.Patch]
        PATCH_DOWNLOAD_LINK: _ClassVar[Statement.Patch]
        PATCH_AUTHOR: _ClassVar[Statement.Patch]
        PATCH_SOURCE: _ClassVar[Statement.Patch]
        PATCH_AUTHOR_ID: _ClassVar[Statement.Patch]
    UNKNOWN_PATCH: Statement.Patch
    PATCH_ALL: Statement.Patch
    PATCH_LOCALE: Statement.Patch
    PATCH_AUTOMATIC: Statement.Patch
    PATCH_DRAFT: Statement.Patch
    PATCH_TITLE: Statement.Patch
    PATCH_CONTENT: Statement.Patch
    PATCH_DOWNLOAD_LINK: Statement.Patch
    PATCH_AUTHOR: Statement.Patch
    PATCH_SOURCE: Statement.Patch
    PATCH_AUTHOR_ID: Statement.Patch
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    locale: str
    automatic: bool
    draft: bool
    title: str
    content: _content_pb2.Content
    download_link: str
    author: str
    source: str
    author_id: str
    def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., automatic: bool = ..., draft: bool = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., download_link: _Optional[str] = ..., author: _Optional[str] = ..., source: _Optional[str] = ..., author_id: _Optional[str] = ...) -> None: ...
