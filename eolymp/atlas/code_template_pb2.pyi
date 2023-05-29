from eolymp.atlas import code_template_file_pb2 as _code_template_file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Template(_message.Message):
    __slots__ = ["files", "footer", "footer_ern", "header", "header_ern", "id", "problem_id", "runtime", "source", "source_ern"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    FOOTER_ERN_FIELD_NUMBER: _ClassVar[int]
    FOOTER_FIELD_NUMBER: _ClassVar[int]
    HEADER_ERN_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ERN_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[_code_template_file_pb2.File]
    footer: str
    footer_ern: str
    header: str
    header_ern: str
    id: str
    problem_id: str
    runtime: str
    source: str
    source_ern: str
    def __init__(self, id: _Optional[str] = ..., problem_id: _Optional[str] = ..., runtime: _Optional[str] = ..., source: _Optional[str] = ..., header: _Optional[str] = ..., footer: _Optional[str] = ..., source_ern: _Optional[str] = ..., header_ern: _Optional[str] = ..., footer_ern: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_code_template_file_pb2.File, _Mapping]]] = ...) -> None: ...
