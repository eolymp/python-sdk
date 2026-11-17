from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.copilot import skill_pb2 as _skill_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSkillInput(_message.Message):
    __slots__ = ("skill",)
    SKILL_FIELD_NUMBER: _ClassVar[int]
    skill: _skill_pb2.Skill
    def __init__(self, skill: _Optional[_Union[_skill_pb2.Skill, _Mapping]] = ...) -> None: ...

class CreateSkillOutput(_message.Message):
    __slots__ = ("skill_id",)
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    skill_id: str
    def __init__(self, skill_id: _Optional[str] = ...) -> None: ...

class UpdateSkillInput(_message.Message):
    __slots__ = ("skill_id", "skill")
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    SKILL_FIELD_NUMBER: _ClassVar[int]
    skill_id: str
    skill: _skill_pb2.Skill.Patch
    def __init__(self, skill_id: _Optional[str] = ..., skill: _Optional[_Union[_skill_pb2.Skill.Patch, _Mapping]] = ...) -> None: ...

class UpdateSkillOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteSkillInput(_message.Message):
    __slots__ = ("skill_id",)
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    skill_id: str
    def __init__(self, skill_id: _Optional[str] = ...) -> None: ...

class DeleteSkillOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeSkillInput(_message.Message):
    __slots__ = ("skill_id",)
    SKILL_ID_FIELD_NUMBER: _ClassVar[int]
    skill_id: str
    def __init__(self, skill_id: _Optional[str] = ...) -> None: ...

class DescribeSkillOutput(_message.Message):
    __slots__ = ("skill",)
    SKILL_FIELD_NUMBER: _ClassVar[int]
    skill: _skill_pb2.Skill
    def __init__(self, skill: _Optional[_Union[_skill_pb2.Skill, _Mapping]] = ...) -> None: ...

class ListSkillsInput(_message.Message):
    __slots__ = ("offset", "size", "search", "filters")
    class Filter(_message.Message):
        __slots__ = ("id", "path")
        ID_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        path: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., path: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    search: str
    filters: ListSkillsInput.Filter
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., search: _Optional[str] = ..., filters: _Optional[_Union[ListSkillsInput.Filter, _Mapping]] = ...) -> None: ...

class ListSkillsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_skill_pb2.Skill]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_skill_pb2.Skill, _Mapping]]] = ...) -> None: ...
