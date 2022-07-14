from eolymp.annotations import resource_pb2 as _resource_pb2
from eolymp.typewriter import block_pb2 as _block_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Statement(_message.Message):
    __slots__ = ["author", "content", "content_rich", "download_link", "format", "id", "locale", "problem_id", "source", "title"]
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_RICH_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    HTML: Statement.Format
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MARKDOWN: Statement.Format
    NONE: Statement.Format
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RICH: Statement.Format
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TEX: Statement.Format
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    content: str
    content_rich: _block_pb2.Container
    download_link: str
    format: Statement.Format
    id: str
    locale: str
    problem_id: str
    source: str
    title: str
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., locale: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., content_rich: _Optional[_Union[_block_pb2.Container, _Mapping]] = ..., download_link: _Optional[str] = ..., format: _Optional[_Union[Statement.Format, str]] = ..., author: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...
