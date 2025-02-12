from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import script_pb2 as _script_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScriptChangedEvent(_message.Message):
    __slots__ = ("problem_id", "before", "after")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    before: _script_pb2.Script
    after: _script_pb2.Script
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Union[_script_pb2.Script, _Mapping]] = ..., after: _Optional[_Union[_script_pb2.Script, _Mapping]] = ...) -> None: ...

class CreateScriptInput(_message.Message):
    __slots__ = ("script",)
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: _script_pb2.Script
    def __init__(self, script: _Optional[_Union[_script_pb2.Script, _Mapping]] = ...) -> None: ...

class CreateScriptOutput(_message.Message):
    __slots__ = ("script_id",)
    SCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    script_id: str
    def __init__(self, script_id: _Optional[str] = ...) -> None: ...

class UpdateScriptInput(_message.Message):
    __slots__ = ("patch", "script_id", "script")
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALL: _ClassVar[UpdateScriptInput.Patch]
        NAME: _ClassVar[UpdateScriptInput.Patch]
        SECRET: _ClassVar[UpdateScriptInput.Patch]
        RUNTIME: _ClassVar[UpdateScriptInput.Patch]
        SOURCE_URL: _ClassVar[UpdateScriptInput.Patch]
        FILES: _ClassVar[UpdateScriptInput.Patch]
    ALL: UpdateScriptInput.Patch
    NAME: UpdateScriptInput.Patch
    SECRET: UpdateScriptInput.Patch
    RUNTIME: UpdateScriptInput.Patch
    SOURCE_URL: UpdateScriptInput.Patch
    FILES: UpdateScriptInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[UpdateScriptInput.Patch]
    script_id: str
    script: _script_pb2.Script
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateScriptInput.Patch, str]]] = ..., script_id: _Optional[str] = ..., script: _Optional[_Union[_script_pb2.Script, _Mapping]] = ...) -> None: ...

class UpdateScriptOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteScriptInput(_message.Message):
    __slots__ = ("script_id",)
    SCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    script_id: str
    def __init__(self, script_id: _Optional[str] = ...) -> None: ...

class DeleteScriptOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeScriptInput(_message.Message):
    __slots__ = ("script_id", "version", "extra")
    SCRIPT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    script_id: str
    version: int
    extra: _containers.RepeatedScalarFieldContainer[_script_pb2.Script.Extra]
    def __init__(self, script_id: _Optional[str] = ..., version: _Optional[int] = ..., extra: _Optional[_Iterable[_Union[_script_pb2.Script.Extra, str]]] = ...) -> None: ...

class DescribeScriptOutput(_message.Message):
    __slots__ = ("script",)
    SCRIPT_FIELD_NUMBER: _ClassVar[int]
    script: _script_pb2.Script
    def __init__(self, script: _Optional[_Union[_script_pb2.Script, _Mapping]] = ...) -> None: ...

class ListScriptsInput(_message.Message):
    __slots__ = ("version", "offset", "size", "search", "filters", "sort", "order", "extra")
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NAME: _ClassVar[ListScriptsInput.Sortable]
    NAME: ListScriptsInput.Sortable
    class Filter(_message.Message):
        __slots__ = ("id", "name", "runtime")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        RUNTIME_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        runtime: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., runtime: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    version: int
    offset: int
    size: int
    search: str
    filters: ListScriptsInput.Filter
    sort: ListScriptsInput.Sortable
    order: _direction_pb2.Direction
    extra: _containers.RepeatedScalarFieldContainer[_script_pb2.Script.Extra]
    def __init__(self, version: _Optional[int] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListScriptsInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListScriptsInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_script_pb2.Script.Extra, str]]] = ...) -> None: ...

class ListScriptsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_script_pb2.Script]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_script_pb2.Script, _Mapping]]] = ...) -> None: ...
