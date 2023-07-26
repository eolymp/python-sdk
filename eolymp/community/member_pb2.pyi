from eolymp.community import attribute_pb2 as _attribute_pb2
from eolymp.community import member_ghost_pb2 as _member_ghost_pb2
from eolymp.community import member_team_pb2 as _member_team_pb2
from eolymp.community import member_user_pb2 as _member_user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Member(_message.Message):
    __slots__ = ["active", "attributes", "ghost", "id", "incomplete", "name", "secret", "team", "unofficial", "user"]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    GHOST_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INCOMPLETE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    TEAM_FIELD_NUMBER: _ClassVar[int]
    UNOFFICIAL_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    active: bool
    attributes: _containers.RepeatedCompositeFieldContainer[_attribute_pb2.Attribute.Value]
    ghost: _member_ghost_pb2.Ghost
    id: str
    incomplete: bool
    name: str
    secret: bool
    team: _member_team_pb2.Team
    unofficial: bool
    user: _member_user_pb2.User
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., active: bool = ..., incomplete: bool = ..., unofficial: bool = ..., secret: bool = ..., user: _Optional[_Union[_member_user_pb2.User, _Mapping]] = ..., team: _Optional[_Union[_member_team_pb2.Team, _Mapping]] = ..., ghost: _Optional[_Union[_member_ghost_pb2.Ghost, _Mapping]] = ..., attributes: _Optional[_Iterable[_Union[_attribute_pb2.Attribute.Value, _Mapping]]] = ...) -> None: ...
