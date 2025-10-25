from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import member_pb2 as _member_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestAdmissionInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequestAdmissionOutput(_message.Message):
    __slots__ = ("required", "code")
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    required: bool
    code: str
    def __init__(self, required: bool = ..., code: _Optional[str] = ...) -> None: ...

class AcceptAdmissionInput(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class AcceptAdmissionOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeAdmissionInput(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class DescribeAdmissionOutput(_message.Message):
    __slots__ = ("participant_id", "session_id", "member")
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FIELD_NUMBER: _ClassVar[int]
    participant_id: str
    session_id: str
    member: _member_pb2.Member
    def __init__(self, participant_id: _Optional[str] = ..., session_id: _Optional[str] = ..., member: _Optional[_Union[_member_pb2.Member, _Mapping]] = ...) -> None: ...

class WatchAdmissionInput(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class WatchAdmissionOutput(_message.Message):
    __slots__ = ("status",)
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[WatchAdmissionOutput.Status]
        ACCEPTED: _ClassVar[WatchAdmissionOutput.Status]
        EXPIRED: _ClassVar[WatchAdmissionOutput.Status]
    UNKNOWN_STATUS: WatchAdmissionOutput.Status
    ACCEPTED: WatchAdmissionOutput.Status
    EXPIRED: WatchAdmissionOutput.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: WatchAdmissionOutput.Status
    def __init__(self, status: _Optional[_Union[WatchAdmissionOutput.Status, str]] = ...) -> None: ...
