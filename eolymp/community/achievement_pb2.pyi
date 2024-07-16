from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Achievement(_message.Message):
    __slots__ = ["awarded_at", "cursor", "id", "image_url", "name", "quantity", "rarity", "summary", "value"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AWARDED_AT_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NO_EXTRA: Achievement.Extra
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    RARITY_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_RENDER: Achievement.Extra
    SUMMARY_VALUE: Achievement.Extra
    VALUE_FIELD_NUMBER: _ClassVar[int]
    awarded_at: _timestamp_pb2.Timestamp
    cursor: str
    id: str
    image_url: str
    name: str
    quantity: int
    rarity: int
    summary: _content_pb2.Content
    value: int
    def __init__(self, id: _Optional[str] = ..., value: _Optional[int] = ..., rarity: _Optional[int] = ..., quantity: _Optional[int] = ..., awarded_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., summary: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., cursor: _Optional[str] = ...) -> None: ...
