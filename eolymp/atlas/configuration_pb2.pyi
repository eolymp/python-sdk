from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ("hourly_ip_submission_limit", "daily_ip_submission_limit", "tracing_enabled")
    class Patch(_message.Message):
        __slots__ = ("hourly_ip_submission_limit", "daily_ip_submission_limit", "tracing_enabled")
        HOURLY_IP_SUBMISSION_LIMIT_FIELD_NUMBER: _ClassVar[int]
        DAILY_IP_SUBMISSION_LIMIT_FIELD_NUMBER: _ClassVar[int]
        TRACING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        hourly_ip_submission_limit: int
        daily_ip_submission_limit: int
        tracing_enabled: bool
        def __init__(self, hourly_ip_submission_limit: _Optional[int] = ..., daily_ip_submission_limit: _Optional[int] = ..., tracing_enabled: _Optional[bool] = ...) -> None: ...
    HOURLY_IP_SUBMISSION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DAILY_IP_SUBMISSION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TRACING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    hourly_ip_submission_limit: int
    daily_ip_submission_limit: int
    tracing_enabled: bool
    def __init__(self, hourly_ip_submission_limit: _Optional[int] = ..., daily_ip_submission_limit: _Optional[int] = ..., tracing_enabled: _Optional[bool] = ...) -> None: ...
