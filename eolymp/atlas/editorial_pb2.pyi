from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Editorial(_message.Message):
    __slots__ = ["author_id", "automatic", "content", "download_link", "draft", "id", "locale"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_RENDER: Editorial.Extra
    CONTENT_VALUE: Editorial.Extra
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    NO_EXTRA: Editorial.Extra
    PATCH_ALL: Editorial.Patch
    PATCH_AUTHOR_ID: Editorial.Patch
    PATCH_AUTOMATIC: Editorial.Patch
    PATCH_CONTENT: Editorial.Patch
    PATCH_DOWNLOAD_LINK: Editorial.Patch
    PATCH_DRAFT: Editorial.Patch
    PATCH_LOCALE: Editorial.Patch
    UNKNOWN_PATCH: Editorial.Patch
    author_id: str
    automatic: bool
    content: _content_pb2.Content
    download_link: str
    draft: bool
    id: str
    locale: str
    def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., automatic: bool = ..., draft: bool = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., download_link: _Optional[str] = ..., author_id: _Optional[str] = ...) -> None: ...
