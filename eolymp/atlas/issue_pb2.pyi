import datetime

from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Issue(_message.Message):
    __slots__ = ("id", "status", "description", "member_id", "created_at", "updated_at")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_STATUS: _ClassVar[Issue.Status]
        OPEN: _ClassVar[Issue.Status]
        CLOSED: _ClassVar[Issue.Status]
    UNKNOWN_STATUS: Issue.Status
    OPEN: Issue.Status
    CLOSED: Issue.Status
    class Extra(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[Issue.Extra.Field]
            DESCRIPTION_VALUE: _ClassVar[Issue.Extra.Field]
            DESCRIPTION_RENDER: _ClassVar[Issue.Extra.Field]
        UNKNOWN_FIELD: Issue.Extra.Field
        DESCRIPTION_VALUE: Issue.Extra.Field
        DESCRIPTION_RENDER: Issue.Extra.Field
        def __init__(self) -> None: ...
    class Patch(_message.Message):
        __slots__ = ()
        class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN_FIELD: _ClassVar[Issue.Patch.Field]
            STATUS: _ClassVar[Issue.Patch.Field]
            DESCRIPTION: _ClassVar[Issue.Patch.Field]
        UNKNOWN_FIELD: Issue.Patch.Field
        STATUS: Issue.Patch.Field
        DESCRIPTION: Issue.Patch.Field
        def __init__(self) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: Issue.Status
    description: _content_pb2.Content
    member_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[Issue.Status, str]] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., member_id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
