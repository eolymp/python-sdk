from eolymp.community import member_pb2 as _member_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MemberChangeRecord(_message.Message):
    __slots__ = ["member", "op", "space_id"]
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CREATE: MemberChangeRecord.Operation
    DELETE: MemberChangeRecord.Operation
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    NO_OPERATION: MemberChangeRecord.Operation
    OP_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE: MemberChangeRecord.Operation
    member: _member_pb2.Member
    op: MemberChangeRecord.Operation
    space_id: str
    def __init__(self, space_id: _Optional[str] = ..., op: _Optional[_Union[MemberChangeRecord.Operation, str]] = ..., member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

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
