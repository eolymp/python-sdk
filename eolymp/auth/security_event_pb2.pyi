from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SecurityEvent(_message.Message):
    __slots__ = ("session_closed", "token_revoked", "account_purged")
    class SessionClosed(_message.Message):
        __slots__ = ("issuer", "subject", "session_id")
        ISSUER_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        issuer: str
        subject: str
        session_id: str
        def __init__(self, issuer: _Optional[str] = ..., subject: _Optional[str] = ..., session_id: _Optional[str] = ...) -> None: ...
    class TokenRevoked(_message.Message):
        __slots__ = ("issuer", "subject", "token_type", "token_hash_md5")
        ISSUER_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        TOKEN_TYPE_FIELD_NUMBER: _ClassVar[int]
        TOKEN_HASH_MD5_FIELD_NUMBER: _ClassVar[int]
        issuer: str
        subject: str
        token_type: str
        token_hash_md5: str
        def __init__(self, issuer: _Optional[str] = ..., subject: _Optional[str] = ..., token_type: _Optional[str] = ..., token_hash_md5: _Optional[str] = ...) -> None: ...
    class AccountPurged(_message.Message):
        __slots__ = ("issuer", "subject")
        ISSUER_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        issuer: str
        subject: str
        def __init__(self, issuer: _Optional[str] = ..., subject: _Optional[str] = ...) -> None: ...
    SESSION_CLOSED_FIELD_NUMBER: _ClassVar[int]
    TOKEN_REVOKED_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_PURGED_FIELD_NUMBER: _ClassVar[int]
    session_closed: SecurityEvent.SessionClosed
    token_revoked: SecurityEvent.TokenRevoked
    account_purged: SecurityEvent.AccountPurged
    def __init__(self, session_closed: _Optional[_Union[SecurityEvent.SessionClosed, _Mapping]] = ..., token_revoked: _Optional[_Union[SecurityEvent.TokenRevoked, _Mapping]] = ..., account_purged: _Optional[_Union[SecurityEvent.AccountPurged, _Mapping]] = ...) -> None: ...
