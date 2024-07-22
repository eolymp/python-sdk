from eolymp.ecm import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Module(_message.Message):
    __slots__ = ["description", "draft", "id", "image_url", "index", "name", "url"]
    class Extra(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BLOCKED: Module.Status
    COMPLETE: Module.Status
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_RENDER: Module.Extra
    DESCRIPTION_VALUE: Module.Extra
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    IN_PROGRESS: Module.Status
    NAME_FIELD_NUMBER: _ClassVar[int]
    READY: Module.Status
    UNKNOWN_EXTRA: Module.Extra
    UNKNOWN_STATUS: Module.Status
    URL_FIELD_NUMBER: _ClassVar[int]
    description: _content_pb2.Content
    draft: bool
    id: str
    image_url: str
    index: int
    name: str
    url: str
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., draft: bool = ..., name: _Optional[str] = ..., image_url: _Optional[str] = ..., index: _Optional[int] = ..., description: _Optional[_Union[_content_pb2.Content, _Mapping]] = ...) -> None: ...
