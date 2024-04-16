from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.course import entry_pb2 as _entry_pb2
from eolymp.wellknown import direction_pb2 as _direction_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateEntryInput(_message.Message):
    __slots__ = ["entry"]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _entry_pb2.Entry
    def __init__(self, entry: _Optional[_Union[_entry_pb2.Entry, _Mapping]] = ...) -> None: ...

class CreateEntryOutput(_message.Message):
    __slots__ = ["entry_id"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    def __init__(self, entry_id: _Optional[str] = ...) -> None: ...

class DeleteEntryInput(_message.Message):
    __slots__ = ["entry_id"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    def __init__(self, entry_id: _Optional[str] = ...) -> None: ...

class DeleteEntryOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeEntryInput(_message.Message):
    __slots__ = ["entry_id", "extra"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    extra: _containers.RepeatedScalarFieldContainer[_entry_pb2.Entry.Extra]
    def __init__(self, entry_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_entry_pb2.Entry.Extra, str]]] = ...) -> None: ...

class DescribeEntryOutput(_message.Message):
    __slots__ = ["entry"]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _entry_pb2.Entry
    def __init__(self, entry: _Optional[_Union[_entry_pb2.Entry, _Mapping]] = ...) -> None: ...

class DescribeTreeInput(_message.Message):
    __slots__ = ["depth", "draft", "extra", "root_id"]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    DRAFT_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    ROOT_ID_FIELD_NUMBER: _ClassVar[int]
    depth: int
    draft: bool
    extra: _containers.RepeatedScalarFieldContainer[_entry_pb2.Entry.Extra]
    root_id: str
    def __init__(self, root_id: _Optional[str] = ..., depth: _Optional[int] = ..., draft: bool = ..., extra: _Optional[_Iterable[_Union[_entry_pb2.Entry.Extra, str]]] = ...) -> None: ...

class DescribeTreeOutput(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_entry_pb2.Entry]
    def __init__(self, items: _Optional[_Iterable[_Union[_entry_pb2.Entry, _Mapping]]] = ...) -> None: ...

class ListEntriesInput(_message.Message):
    __slots__ = ["extra", "filters", "offset", "order", "size", "sort"]
    class Sortable(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Filter(_message.Message):
        __slots__ = ["draft", "id", "parent_id", "query", "title"]
        DRAFT_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        PARENT_ID_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        draft: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        parent_id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        query: str
        title: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., parent_id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., draft: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ..., title: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    DEFAULT: ListEntriesInput.Sortable
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SORT_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_entry_pb2.Entry.Extra]
    filters: ListEntriesInput.Filter
    offset: int
    order: _direction_pb2.Direction
    size: int
    sort: ListEntriesInput.Sortable
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListEntriesInput.Filter, _Mapping]] = ..., sort: _Optional[_Union[ListEntriesInput.Sortable, str]] = ..., order: _Optional[_Union[_direction_pb2.Direction, str]] = ..., extra: _Optional[_Iterable[_Union[_entry_pb2.Entry.Extra, str]]] = ...) -> None: ...

class ListEntriesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_entry_pb2.Entry]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_entry_pb2.Entry, _Mapping]]] = ...) -> None: ...

class ListParentsInput(_message.Message):
    __slots__ = ["entry_id", "extra"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    extra: _containers.RepeatedScalarFieldContainer[_entry_pb2.Entry.Extra]
    def __init__(self, entry_id: _Optional[str] = ..., extra: _Optional[_Iterable[_Union[_entry_pb2.Entry.Extra, str]]] = ...) -> None: ...

class ListParentsOutput(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_entry_pb2.Entry]
    def __init__(self, items: _Optional[_Iterable[_Union[_entry_pb2.Entry, _Mapping]]] = ...) -> None: ...

class MoveEntryInput(_message.Message):
    __slots__ = ["entry_id", "index", "parent_id"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    index: int
    parent_id: str
    def __init__(self, entry_id: _Optional[str] = ..., parent_id: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...

class MoveEntryOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RenameEntryInput(_message.Message):
    __slots__ = ["entry_id", "title"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    title: str
    def __init__(self, entry_id: _Optional[str] = ..., title: _Optional[str] = ...) -> None: ...

class RenameEntryOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateEntryInput(_message.Message):
    __slots__ = ["entry", "entry_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateEntryInput.Patch
    CONTENT_ALL: UpdateEntryInput.Patch
    DRAFT: UpdateEntryInput.Patch
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_URL: UpdateEntryInput.Patch
    SECTION_DESCRIPTION: UpdateEntryInput.Patch
    SECTION_IMAGE: UpdateEntryInput.Patch
    TITLE: UpdateEntryInput.Patch
    VIDEO_IMAGE_URL: UpdateEntryInput.Patch
    VIDEO_VIDEO_URL: UpdateEntryInput.Patch
    WEIGHT: UpdateEntryInput.Patch
    entry: _entry_pb2.Entry
    entry_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateEntryInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateEntryInput.Patch, str]]] = ..., entry_id: _Optional[str] = ..., entry: _Optional[_Union[_entry_pb2.Entry, _Mapping]] = ...) -> None: ...

class UpdateEntryOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
