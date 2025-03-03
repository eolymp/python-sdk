from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.community import email_type_pb2 as _email_type_pb2
from eolymp.community import member_pb2 as _member_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendEmailInput(_message.Message):
    __slots__ = ("member_id", "dry_run", "bcc_me", "type", "campaign", "locale", "subject", "content", "parameters")
    class ParametersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    BCC_ME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    dry_run: bool
    bcc_me: bool
    type: _email_type_pb2.EmailType
    campaign: str
    locale: str
    subject: str
    content: _content_pb2.Content
    parameters: _containers.ScalarMap[str, str]
    def __init__(self, member_id: _Optional[str] = ..., dry_run: bool = ..., bcc_me: bool = ..., type: _Optional[_Union[_email_type_pb2.EmailType, str]] = ..., campaign: _Optional[str] = ..., locale: _Optional[str] = ..., subject: _Optional[str] = ..., content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class SendEmailOutput(_message.Message):
    __slots__ = ("message_id",)
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    def __init__(self, message_id: _Optional[str] = ...) -> None: ...

class DescribeEmailUsageInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeEmailUsageOutput(_message.Message):
    __slots__ = ("daily_emails", "monthly_emails")
    DAILY_EMAILS_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_EMAILS_FIELD_NUMBER: _ClassVar[int]
    daily_emails: int
    monthly_emails: int
    def __init__(self, daily_emails: _Optional[int] = ..., monthly_emails: _Optional[int] = ...) -> None: ...
