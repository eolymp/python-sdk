from eolymp.universe import quota_pb2 as _quota_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Space(_message.Message):
    __slots__ = ["graphql_url", "home_url", "id", "image", "issuer_url", "key", "name", "plan", "quota", "seats", "type", "url", "visibility"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CLASSROOM: Space.Type
    COMPETITION: Space.Type
    GRAPHQL_URL_FIELD_NUMBER: _ClassVar[int]
    HOME_URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    ISSUER_URL_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OTHER: Space.Type
    PLAN_FIELD_NUMBER: _ClassVar[int]
    PRIVATE: Space.Visibility
    PUBLIC: Space.Visibility
    QUOTA_FIELD_NUMBER: _ClassVar[int]
    SEATS_FIELD_NUMBER: _ClassVar[int]
    TEAMROOM: Space.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_TYPE: Space.Type
    UNKNOWN_VISIBILITY: Space.Visibility
    URL_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    graphql_url: str
    home_url: str
    id: str
    image: str
    issuer_url: str
    key: str
    name: str
    plan: str
    quota: _quota_pb2.Quota
    seats: int
    type: Space.Type
    url: str
    visibility: Space.Visibility
    def __init__(self, id: _Optional[str] = ..., key: _Optional[str] = ..., url: _Optional[str] = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., type: _Optional[_Union[Space.Type, str]] = ..., visibility: _Optional[_Union[Space.Visibility, str]] = ..., quota: _Optional[_Union[_quota_pb2.Quota, _Mapping]] = ..., plan: _Optional[str] = ..., seats: _Optional[int] = ..., home_url: _Optional[str] = ..., issuer_url: _Optional[str] = ..., graphql_url: _Optional[str] = ...) -> None: ...
