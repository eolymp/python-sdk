from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Variant(_message.Message):
    __slots__ = ("id", "locale", "title", "content", "automatic")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTRA: _ClassVar[Variant.Extra]
        CONTENT_RENDER: _ClassVar[Variant.Extra]
        CONTENT_VALUE: _ClassVar[Variant.Extra]
    NO_EXTRA: Variant.Extra
    CONTENT_RENDER: Variant.Extra
    CONTENT_VALUE: Variant.Extra
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    id: str
    locale: str
    title: str
    content: _content_pb2.Content
    automatic: bool
    def __init__(self, id: _Optional[str] = ..., locale: _Optional[str] = ..., title: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., automatic: bool = ...) -> None: ...
