from eolymp.community import group_pb2 as _group_pb2
from eolymp.community import member_pb2 as _member_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupChangedEvent(_message.Message):
    __slots__ = ["after", "before"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    after: _group_pb2.Group
    before: _group_pb2.Group
    def __init__(self, before: _Optional[_Union[_group_pb2.Group, _Mapping]] = ..., after: _Optional[_Union[_group_pb2.Group, _Mapping]] = ...) -> None: ...

class MemberChangedEvent(_message.Message):
    __slots__ = ["after", "before"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    after: _member_pb2.Member
    before: _member_pb2.Member
    def __init__(self, before: _Optional[_Union[_member_pb2.Member, _Mapping]] = ..., after: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class MemberCreatedEvent(_message.Message):
    __slots__ = ["member"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _member_pb2.Member
    def __init__(self, member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class MemberDeletedEvent(_message.Message):
    __slots__ = ["member"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _member_pb2.Member
    def __init__(self, member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class MemberUpdatedEvent(_message.Message):
    __slots__ = ["member"]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    member: _member_pb2.Member
    def __init__(self, member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...
