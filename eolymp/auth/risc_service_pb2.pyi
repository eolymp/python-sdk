from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.auth import claims_pb2 as _claims_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HandleSecurityEventInput(_message.Message):
    __slots__ = ["security_event"]
    SECURITY_EVENT_FIELD_NUMBER: _ClassVar[int]
    security_event: str
    def __init__(self, security_event: _Optional[str] = ...) -> None: ...

class HandleSecurityEventOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SecurityEvent(_message.Message):
    __slots__ = ["aud", "events", "iat", "iss", "jti"]
    class Event(_message.Message):
        __slots__ = ["claims", "reason", "state", "subject", "token", "token_identifier_alg", "token_type", "type"]
        CLAIMS_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        TOKEN_IDENTIFIER_ALG_FIELD_NUMBER: _ClassVar[int]
        TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        claims: _claims_pb2.Claims
        reason: str
        state: str
        subject: SecurityEvent.Subject
        token: str
        token_identifier_alg: str
        token_type: str
        type: str
        def __init__(self, type: _Optional[str] = ..., subject: _Optional[_Union[SecurityEvent.Subject, _Mapping]] = ..., claims: _Optional[_Union[_claims_pb2.Claims, _Mapping]] = ..., reason: _Optional[str] = ..., state: _Optional[str] = ..., token: _Optional[str] = ..., token_type: _Optional[str] = ..., token_identifier_alg: _Optional[str] = ...) -> None: ...
    class Subject(_message.Message):
        __slots__ = ["email", "format", "id", "iss", "sub"]
        EMAIL_FIELD_NUMBER: _ClassVar[int]
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        ISS_FIELD_NUMBER: _ClassVar[int]
        SUB_FIELD_NUMBER: _ClassVar[int]
        email: str
        format: str
        id: str
        iss: str
        sub: str
        def __init__(self, format: _Optional[str] = ..., id: _Optional[str] = ..., iss: _Optional[str] = ..., sub: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
    AUD_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    IAT_FIELD_NUMBER: _ClassVar[int]
    ISS_FIELD_NUMBER: _ClassVar[int]
    JTI_FIELD_NUMBER: _ClassVar[int]
    aud: str
    events: _containers.RepeatedCompositeFieldContainer[SecurityEvent.Event]
    iat: int
    iss: str
    jti: str
    def __init__(self, iss: _Optional[str] = ..., aud: _Optional[str] = ..., iat: _Optional[int] = ..., jti: _Optional[str] = ..., events: _Optional[_Iterable[_Union[SecurityEvent.Event, _Mapping]]] = ...) -> None: ...
