from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EnterPasscodeInput(_message.Message):
    __slots__ = ["contest_id", "passcode"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    passcode: str
    def __init__(self, contest_id: _Optional[str] = ..., passcode: _Optional[str] = ...) -> None: ...

class EnterPasscodeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemovePasscodeInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class RemovePasscodeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ResetPasscodeInput(_message.Message):
    __slots__ = ["contest_id", "participant_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ...) -> None: ...

class ResetPasscodeOutput(_message.Message):
    __slots__ = ["passcode"]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    passcode: str
    def __init__(self, passcode: _Optional[str] = ...) -> None: ...

class SetPasscodeInput(_message.Message):
    __slots__ = ["contest_id", "participant_id", "passcode"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_ID_FIELD_NUMBER: _ClassVar[int]
    PASSCODE_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    participant_id: str
    passcode: str
    def __init__(self, contest_id: _Optional[str] = ..., participant_id: _Optional[str] = ..., passcode: _Optional[str] = ...) -> None: ...

class SetPasscodeOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VerifyPasscodeInput(_message.Message):
    __slots__ = ["contest_id"]
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class VerifyPasscodeOutput(_message.Message):
    __slots__ = ["required", "valid"]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    VALID_FIELD_NUMBER: _ClassVar[int]
    required: bool
    valid: bool
    def __init__(self, required: bool = ..., valid: bool = ...) -> None: ...
