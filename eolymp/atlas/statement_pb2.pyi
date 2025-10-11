from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Statement(_message.Message):
    __slots__ = ("id", "locale", "automatic", "draft", "title", "content", "download_link", "author", "source", "author_id")
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_EXTRA: _ClassVar[Statement.Extra.Field]
            CONTENT_RENDER: _ClassVar[Statement.Extra.Field]
            CONTENT_VALUE: _ClassVar[Statement.Extra.Field]
        UNKNOWN_EXTRA: Statement.Extra.Field
        CONTENT_RENDER: Statement.Extra.Field
        CONTENT_VALUE: Statement.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_PATCH: _ClassVar[Statement.Patch.Field]
            LOCALE: _ClassVar[Statement.Patch.Field]
            AUTOMATIC: _ClassVar[Statement.Patch.Field]
            DRAFT: _ClassVar[Statement.Patch.Field]
            TITLE: _ClassVar[Statement.Patch.Field]
            CONTENT: _ClassVar[Statement.Patch.Field]
            DOWNLOAD_LINK: _ClassVar[Statement.Patch.Field]
            AUTHOR: _ClassVar[Statement.Patch.Field]
            SOURCE: _ClassVar[Statement.Patch.Field]
            AUTHOR_ID: _ClassVar[Statement.Patch.Field]
        UNKNOWN_PATCH: Statement.Patch.Field
        LOCALE: Statement.Patch.Field
        AUTOMATIC: Statement.Patch.Field
        DRAFT: Statement.Patch.Field
        TITLE: Statement.Patch.Field
        CONTENT: Statement.Patch.Field
        DOWNLOAD_LINK: Statement.Patch.Field
        AUTHOR: Statement.Patch.Field
        SOURCE: Statement.Patch.Field
        AUTHOR_ID: Statement.Patch.Field
        def __init__(self) -> None: ...
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
