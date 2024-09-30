from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Module(_message.Message):
    __slots__ = ["complete_before", "description", "draft", "duration", "extra", "id", "image_url", "index", "name", "progress", "start_after", "url"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Progress(_message.Message):
        __slots__ = ["assigned_at", "complete_before", "completed_at", "duration", "grade", "percentage", "start_after", "started_at", "status", "upsolve"]
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ACTIVE: Module.Progress.Status
        ASSIGNED_AT_FIELD_NUMBER: _ClassVar[int]
        COMPLETE: Module.Progress.Status
        COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
        COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        GRADE_FIELD_NUMBER: _ClassVar[int]
        PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        READY: Module.Progress.Status
        SCHEDULED: Module.Progress.Status
        STARTED_AT_FIELD_NUMBER: _ClassVar[int]
        START_AFTER_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        UNASSIGNED: Module.Progress.Status
        UNKNOWN_STATUS: Module.Progress.Status
        UPSOLVE: Module.Progress.Status
        UPSOLVE_FIELD_NUMBER: _ClassVar[int]
        assigned_at: _timestamp_pb2.Timestamp
        complete_before: _timestamp_pb2.Timestamp
        completed_at: _timestamp_pb2.Timestamp
        duration: int
        grade: int
        percentage: float
        start_after: _timestamp_pb2.Timestamp
        started_at: _timestamp_pb2.Timestamp
        status: Module.Progress.Status
        upsolve: bool
        def __init__(self, status: _Optional[_Union[Module.Progress.Status, str]] = ..., percentage: _Optional[float] = ..., grade: _Optional[int] = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., upsolve: bool = ..., assigned_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
    COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_RENDER: Module.Extra
    DESCRIPTION_VALUE: Module.Extra
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROGRESS: Module.Extra
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    START_AFTER_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Module.Extra
    URL_FIELD_NUMBER: _ClassVar[int]
    complete_before: _timestamp_pb2.Timestamp
    description: _content_pb2.Content
    draft: bool
    duration: int
    extra: bool
    id: str
    image_url: str
    index: int
    name: str
    progress: Module.Progress
    start_after: _timestamp_pb2.Timestamp
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., draft: bool = ..., extra: bool = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., index: _Optional[int] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ..., progress: _Optional[_Union[Module.Progress, _Mapping]] = ...) -> None: ...
