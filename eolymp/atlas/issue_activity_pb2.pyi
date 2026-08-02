import datetime

from eolymp.atlas import issue_pb2 as _issue_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IssueActivity(_message.Message):
    __slots__ = ("id", "issue_id", "user_id", "member_id", "created_at", "updated_at", "comment", "change")
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[IssueActivity.Extra.Field]
            MESSAGE_VALUE: _ClassVar[IssueActivity.Extra.Field]
            MESSAGE_RENDER: _ClassVar[IssueActivity.Extra.Field]
        UNKNOWN_FIELD: IssueActivity.Extra.Field
        MESSAGE_VALUE: IssueActivity.Extra.Field
        MESSAGE_RENDER: IssueActivity.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[IssueActivity.Patch.Field]
            MESSAGE: _ClassVar[IssueActivity.Patch.Field]
        UNKNOWN_FIELD: IssueActivity.Patch.Field
        MESSAGE: IssueActivity.Patch.Field
        def __init__(self) -> None: ...
    class Comment(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: _content_pb2.Content
        def __init__(self, message: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
    class Change(_message.Message):
        __slots__ = ("before", "after")
        BEFORE_FIELD_NUMBER: _ClassVar[int]
        AFTER_FIELD_NUMBER: _ClassVar[int]
        before: _issue_pb2.Issue
        after: _issue_pb2.Issue
        def __init__(self, before: _Optional[_Union[_issue_pb2.Issue, _Mapping]] = ..., after: _Optional[_Union[_issue_pb2.Issue, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ISSUE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CHANGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    issue_id: str
    user_id: str
    member_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    comment: IssueActivity.Comment
    change: IssueActivity.Change
    def __init__(self, id: _Optional[str] = ..., issue_id: _Optional[str] = ..., user_id: _Optional[str] = ..., member_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., comment: _Optional[_Union[IssueActivity.Comment, _Mapping]] = ..., change: _Optional[_Union[IssueActivity.Change, _Mapping]] = ...) -> None: ...
