from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Editorial(_message.Message):
    __slots__ = ("id", "locale", "automatic", "draft", "content", "download_link", "author_id")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTRA: _ClassVar[Editorial.Extra]
        CONTENT_RENDER: _ClassVar[Editorial.Extra]
        CONTENT_VALUE: _ClassVar[Editorial.Extra]
    NO_EXTRA: Editorial.Extra
    CONTENT_RENDER: Editorial.Extra
    CONTENT_VALUE: Editorial.Extra
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_PATCH: _ClassVar[Editorial.Patch]
        PATCH_ALL: _ClassVar[Editorial.Patch]
        PATCH_LOCALE: _ClassVar[Editorial.Patch]
        PATCH_AUTOMATIC: _ClassVar[Editorial.Patch]
        PATCH_DRAFT: _ClassVar[Editorial.Patch]
        PATCH_CONTENT: _ClassVar[Editorial.Patch]
        PATCH_DOWNLOAD_LINK: _ClassVar[Editorial.Patch]
        PATCH_AUTHOR_ID: _ClassVar[Editorial.Patch]
    UNKNOWN_PATCH: Editorial.Patch
    PATCH_ALL: Editorial.Patch
    PATCH_LOCALE: Editorial.Patch
    PATCH_AUTOMATIC: Editorial.Patch
    PATCH_DRAFT: Editorial.Patch
    PATCH_CONTENT: Editorial.Patch
    PATCH_DOWNLOAD_LINK: Editorial.Patch
    PATCH_AUTHOR_ID: Editorial.Patch
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    locale: str
    automatic: bool
    draft: bool
    content: _content_pb2.Content
    download_link: str
    author_id: str
    def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., automatic: bool = ..., draft: bool = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., download_link: _Optional[str] = ..., author_id: _Optional[str] = ...) -> None: ...
