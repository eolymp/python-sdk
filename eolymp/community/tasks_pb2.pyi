from eolymp.community import member_service_pb2 as _member_service_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImportMembersTask(_message.Message):
    __slots__ = ("file_url",)
    class Checkpoint(_message.Message):
        __slots__ = ("line", "created", "updated", "failed")
        LINE_FIELD_NUMBER: _ClassVar[int]
        CREATED_FIELD_NUMBER: _ClassVar[int]
        UPDATED_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        line: int
        created: int
        updated: int
        failed: int
        def __init__(self, line: _Optional[int] = ..., created: _Optional[int] = ..., updated: _Optional[int] = ..., failed: _Optional[int] = ...) -> None: ...
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    file_url: str
    def __init__(self, file_url: _Optional[str] = ...) -> None: ...

class ExportMembersTask(_message.Message):
    __slots__ = ("filters",)
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: _member_service_pb2.ListMembersInput.Filter
    def __init__(self, filters: _Optional[_Union[_member_service_pb2.ListMembersInput.Filter, _Mapping]] = ...) -> None: ...
