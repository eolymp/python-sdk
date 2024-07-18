from eolymp.course import entry_pb2 as _entry_pb2
from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Module(_message.Message):
    __slots__ = ["completed_at", "description", "draft", "due_at", "ends_at", "grade", "id", "image_url", "index", "progress", "starts_at", "status", "title", "url"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BLOCKED: Module.Status
    COMPLETE: Module.Status
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    CONTENT: Module.Extra
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_RENDER: Module.Extra
    DESCRIPTION_VALUE: Module.Extra
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    DUE_AT_FIELD_NUMBER: _ClassVar[int]
    ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS: Module.Status
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    READY: Module.Status
    STARTS_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Module.Extra
    UNKNOWN_STATUS: Module.Status
    URL_FIELD_NUMBER: _ClassVar[int]
    completed_at: _timestamp_pb2.Timestamp
    description: _content_pb2.Content
    draft: bool
    due_at: _timestamp_pb2.Timestamp
    ends_at: _timestamp_pb2.Timestamp
    grade: int
    id: str
    image_url: str
    index: int
    progress: float
    starts_at: _timestamp_pb2.Timestamp
    status: Module.Status
    title: str
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., draft: bool = ..., title: _Optional[str] = ..., image_url: _Optional[str] = ..., index: _Optional[int] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., status: _Optional[_Union[Module.Status, str]] = ..., grade: _Optional[int] = ..., progress: _Optional[float] = ..., starts_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., due_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ends_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
