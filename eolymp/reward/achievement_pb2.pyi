from eolymp.annotations import mcp_pb2 as _mcp_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Achievement(_message.Message):
    __slots__ = ("id", "value", "rarity", "threshold", "multi_award", "name", "image_url", "summary", "locale", "locales", "cursor")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTRA: _ClassVar[Achievement.Extra]
        SUMMARY_VALUE: _ClassVar[Achievement.Extra]
        SUMMARY_RENDER: _ClassVar[Achievement.Extra]
    NO_EXTRA: Achievement.Extra
    SUMMARY_VALUE: Achievement.Extra
    SUMMARY_RENDER: Achievement.Extra
    class Patch(_message.Message):
        __slots__ = ("value", "threshold", "multi_award", "name", "image_url", "summary")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        MULTI_AWARD_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        value: int
        threshold: int
        multi_award: bool
        name: str
        image_url: str
        summary: _content_pb2.Content
        def __init__(self, value: _Optional[int] = ..., threshold: _Optional[int] = ..., multi_award: _Optional[bool] = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., summary: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RARITY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MULTI_AWARD_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    LOCALES_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    value: int
    rarity: int
    threshold: int
    multi_award: bool
    name: str
    image_url: str
    summary: _content_pb2.Content
    locale: str
    locales: _containers.RepeatedScalarFieldContainer[str]
    cursor: str
    def __init__(self, id: _Optional[str] = ..., value: _Optional[int] = ..., rarity: _Optional[int] = ..., threshold: _Optional[int] = ..., multi_award: _Optional[bool] = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., summary: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., locale: _Optional[str] = ..., locales: _Optional[_Iterable[str]] = ..., cursor: _Optional[str] = ...) -> None: ...
