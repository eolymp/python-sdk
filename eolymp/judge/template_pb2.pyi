from eolymp.atlas import code_template_file_pb2 as _code_template_file_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Template(_message.Message):
    __slots__ = ["ern", "files", "footer_ern", "header_ern", "id", "problem_id", "runtime", "source_ern"]
    ERN_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    FOOTER_ERN_FIELD_NUMBER: _ClassVar[int]
    HEADER_ERN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ERN_FIELD_NUMBER: _ClassVar[int]
    ern: str
    files: _containers.RepeatedCompositeFieldContainer[_code_template_file_pb2.File]
    footer_ern: str
    header_ern: str
    id: str
    problem_id: str
    runtime: str
    source_ern: str
    def __init__(self, id: _Optional[str] = ..., ern: _Optional[str] = ..., problem_id: _Optional[str] = ..., runtime: _Optional[str] = ..., source_ern: _Optional[str] = ..., header_ern: _Optional[str] = ..., footer_ern: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_code_template_file_pb2.File, _Mapping]]] = ...) -> None: ...
