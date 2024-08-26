from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import script_pb2 as _script_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateScriptInput(_message.Message):
    __slots__ = ["problem_id", "script"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    script: _script_pb2.Script
    def __init__(self, problem_id: _Optional[str] = ..., script: _Optional[_Union[_script_pb2.Script, _Mapping]] = ...) -> None: ...

class CreateScriptOutput(_message.Message):
    __slots__ = ["script_id"]
    SCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    script_id: str
    def __init__(self, script_id: _Optional[str] = ...) -> None: ...

class DeleteScriptInput(_message.Message):
    __slots__ = ["problem_id", "script_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    script_id: str
    def __init__(self, problem_id: _Optional[str] = ..., script_id: _Optional[str] = ...) -> None: ...

class DeleteScriptOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeScriptInput(_message.Message):
    __slots__ = ["problem_id", "render", "script_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    render: bool
    script_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., script_id: _Optional[str] = ..., render: bool = ..., version: _Optional[int] = ...) -> None: ...

class DescribeScriptOutput(_message.Message):
    __slots__ = ["script"]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: _script_pb2.Script
    def __init__(self, script: _Optional[_Union[_script_pb2.Script, _Mapping]] = ...) -> None: ...

class ListScriptsInput(_message.Message):
    __slots__ = ["problem_id", "render", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    render: bool
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., render: bool = ..., version: _Optional[int] = ...) -> None: ...

class ListScriptsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_script_pb2.Script]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_script_pb2.Script, _Mapping]]] = ...) -> None: ...

class LookupScriptInput(_message.Message):
    __slots__ = ["locale", "problem_id", "render", "version"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    locale: str
    problem_id: str
    render: bool
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., locale: _Optional[str] = ..., render: bool = ..., version: _Optional[int] = ...) -> None: ...

class LookupScriptOutput(_message.Message):
    __slots__ = ["script"]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: _script_pb2.Script
    def __init__(self, script: _Optional[_Union[_script_pb2.Script, _Mapping]] = ...) -> None: ...

class PreviewScriptInput(_message.Message):
    __slots__ = ["problem_id", "script"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    script: _script_pb2.Script
    def __init__(self, problem_id: _Optional[str] = ..., script: _Optional[_Union[_script_pb2.Script, _Mapping]] = ...) -> None: ...

class PreviewScriptOutput(_message.Message):
    __slots__ = ["script"]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: _script_pb2.Script
    def __init__(self, script: _Optional[_Union[_script_pb2.Script, _Mapping]] = ...) -> None: ...

class UpdateScriptInput(_message.Message):
    __slots__ = ["patch", "problem_id", "script", "script_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateScriptInput.Patch
    AUTHOR: UpdateScriptInput.Patch
    CONTENT: UpdateScriptInput.Patch
    DOWNLOAD_LINK: UpdateScriptInput.Patch
    LOCALE: UpdateScriptInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE: UpdateScriptInput.Patch
    TITLE: UpdateScriptInput.Patch
    patch: _containers.RepeatedScalarFieldContainer[UpdateScriptInput.Patch]
    problem_id: str
    script: _script_pb2.Script
    script_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateScriptInput.Patch, str]]] = ..., problem_id: _Optional[str] = ..., script_id: _Optional[str] = ..., script: _Optional[_Union[_script_pb2.Script, _Mapping]] = ...) -> None: ...

class UpdateScriptOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
