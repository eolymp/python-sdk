from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Editorial(_message.Message):
    __slots__ = ("id", "locale", "automatic", "draft", "content", "download_link", "author_id")
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_EXTRA: _ClassVar[Editorial.Extra.Field]
            CONTENT_RENDER: _ClassVar[Editorial.Extra.Field]
            CONTENT_VALUE: _ClassVar[Editorial.Extra.Field]
        UNKNOWN_EXTRA: Editorial.Extra.Field
        CONTENT_RENDER: Editorial.Extra.Field
        CONTENT_VALUE: Editorial.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ("locale", "content", "download_link", "automatic", "draft", "author_id")
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
        AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
        DRAFT_FIELD_NUMBER: _ClassVar[int]
        AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
        locale: str
        content: _content_pb2.Content
        download_link: str
        automatic: bool
        draft: bool
        author_id: str
        def __init__(self, locale: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., download_link: _Optional[str] = ..., automatic: _Optional[bool] = ..., draft: _Optional[bool] = ..., author_id: _Optional[str] = ...) -> None: ...
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
    def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., automatic: _Optional[bool] = ..., draft: _Optional[bool] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., download_link: _Optional[str] = ..., author_id: _Optional[str] = ...) -> None: ...
