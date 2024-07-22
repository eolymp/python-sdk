from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enrollment(_message.Message):
    __slots__ = ["assignments", "display_name", "enrolled_at", "expires_at", "group_id", "id", "member_id", "parent_id"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Assignment(_message.Message):
        __slots__ = ["complete_before", "duration", "module_id", "start_after"]
        COMPLETE_BEFORE_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        MODULE_ID_FIELD_NUMBER: _ClassVar[int]
        START_AFTER_FIELD_NUMBER: _ClassVar[int]
        complete_before: _timestamp_pb2.Timestamp
        duration: int
        module_id: str
        start_after: _timestamp_pb2.Timestamp
        def __init__(self, module_id: _Optional[str] = ..., start_after: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., complete_before: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., duration: _Optional[int] = ...) -> None: ...
    ASSIGNMENTS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ENROLLED_AT_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_EXTRA: Enrollment.Extra
    assignments: _containers.RepeatedCompositeFieldContainer[Enrollment.Assignment]
    display_name: str
    enrolled_at: _timestamp_pb2.Timestamp
    expires_at: _timestamp_pb2.Timestamp
    group_id: str
    id: str
    member_id: str
    parent_id: str
    def __init__(self, id: _Optional[str] = ..., parent_id: _Optional[str] = ..., display_name: _Optional[str] = ..., member_id: _Optional[str] = ..., group_id: _Optional[str] = ..., enrolled_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., assignments: _Optional[_Iterable[_Union[Enrollment.Assignment, _Mapping]]] = ...) -> None: ...
