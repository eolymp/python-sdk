from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Achievement(_message.Message):
    __slots__ = ("id", "value", "rarity", "quantity", "awarded_at", "name", "image_url", "summary", "cursor")
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_EXTRA: _ClassVar[Achievement.Extra]
        SUMMARY_VALUE: _ClassVar[Achievement.Extra]
        SUMMARY_RENDER: _ClassVar[Achievement.Extra]
    NO_EXTRA: Achievement.Extra
    SUMMARY_VALUE: Achievement.Extra
    SUMMARY_RENDER: Achievement.Extra
    ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    RARITY_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    AWARDED_AT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    value: int
    rarity: int
    quantity: int
    awarded_at: _timestamp_pb2.Timestamp
    name: str
    image_url: str
    summary: _content_pb2.Content
    cursor: str
    def __init__(self, id: _Optional[str] = ..., value: _Optional[int] = ..., rarity: _Optional[int] = ..., quantity: _Optional[int] = ..., awarded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., summary: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., cursor: _Optional[str] = ...) -> None: ...
