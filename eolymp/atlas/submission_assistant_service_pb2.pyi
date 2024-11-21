from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DebugSubmissionInput(_message.Message):
    __slots__ = ["locale", "submission_id"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    locale: str
    submission_id: str
    def __init__(self, submission_id: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class DebugSubmissionOutput(_message.Message):
    __slots__ = ["assistance_id", "assistance_message"]
    ASSISTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANCE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    assistance_id: str
    assistance_message: str
    def __init__(self, assistance_id: _Optional[str] = ..., assistance_message: _Optional[str] = ...) -> None: ...

class RateDebugAssistanceInput(_message.Message):
    __slots__ = ["rating", "submission_id"]
    RATING_FIELD_NUMBER: _ClassVar[int]
    SUBMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    rating: int
    submission_id: str
    def __init__(self, submission_id: _Optional[str] = ..., rating: _Optional[int] = ...) -> None: ...

class RateDebugAssistanceOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
