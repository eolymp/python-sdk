from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from eolymp.mail import email_type_pb2 as _email_type_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendEmailInput(_message.Message):
    __slots__ = ("member_id", "email_ref", "dry_run", "bcc_me", "type", "locale", "message", "template")
    class Message(_message.Message):
        __slots__ = ("subject", "body", "data")
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        subject: str
        body: _content_pb2.Content
        data: _struct_pb2.Struct
        def __init__(self, subject: _Optional[str] = ..., body: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    class Template(_message.Message):
        __slots__ = ("path", "data")
        PATH_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        path: str
        data: _struct_pb2.Struct
        def __init__(self, path: _Optional[str] = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_REF_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    BCC_ME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    email_ref: str
    dry_run: bool
    bcc_me: bool
    type: _email_type_pb2.EmailType
    locale: str
    message: SendEmailInput.Message
    template: SendEmailInput.Template
    def __init__(self, member_id: _Optional[str] = ..., email_ref: _Optional[str] = ..., dry_run: bool = ..., bcc_me: bool = ..., type: _Optional[_Union[_email_type_pb2.EmailType, str]] = ..., locale: _Optional[str] = ..., message: _Optional[_Union[SendEmailInput.Message, _Mapping]] = ..., template: _Optional[_Union[SendEmailInput.Template, _Mapping]] = ...) -> None: ...

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
