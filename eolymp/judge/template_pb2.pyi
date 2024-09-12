from eolymp.executor import file_pb2 as _file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Template(_message.Message):
    __slots__ = ["files", "footer_url", "header_url", "id", "problem_id", "runtime", "source_url"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    FOOTER_URL_FIELD_NUMBER: _ClassVar[int]
    HEADER_URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    footer_url: str
    header_url: str
    id: str
    problem_id: str
    runtime: str
    source_url: str
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., runtime: _Optional[str] = ..., source_url: _Optional[str] = ..., header_url: _Optional[str] = ..., footer_url: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...
