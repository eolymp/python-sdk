from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.taxonomy import dataset_pb2 as _dataset_pb2
from eolymp.taxonomy import dataset_entry_pb2 as _dataset_entry_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateDatasetInput(_message.Message):
    __slots__ = ["dataset"]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: _dataset_pb2.Dataset
    def __init__(self, dataset: _Optional[_Union[_dataset_pb2.Dataset, _Mapping]] = ...) -> None: ...

class CreateDatasetOutput(_message.Message):
    __slots__ = ["dataset_id"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    def __init__(self, dataset_id: _Optional[str] = ...) -> None: ...

class CreateEntryInput(_message.Message):
    __slots__ = ["dataset_id", "entry"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    entry: _dataset_entry_pb2.Entry
    def __init__(self, dataset_id: _Optional[str] = ..., entry: _Optional[_Union[_dataset_entry_pb2.Entry, _Mapping]] = ...) -> None: ...

class CreateEntryOutput(_message.Message):
    __slots__ = ["entry_id"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    def __init__(self, entry_id: _Optional[str] = ...) -> None: ...

class DeleteDatasetInput(_message.Message):
    __slots__ = ["dataset_id"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    def __init__(self, dataset_id: _Optional[str] = ...) -> None: ...

class DeleteDatasetOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteEntryInput(_message.Message):
    __slots__ = ["dataset_id", "entry_id"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    entry_id: str
    def __init__(self, dataset_id: _Optional[str] = ..., entry_id: _Optional[str] = ...) -> None: ...

class DeleteEntryOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteTranslationInput(_message.Message):
    __slots__ = ["dataset_id", "entry_id", "locale"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    entry_id: str
    locale: str
    def __init__(self, dataset_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class DeleteTranslationOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeDatasetInput(_message.Message):
    __slots__ = ["dataset_id"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    def __init__(self, dataset_id: _Optional[str] = ...) -> None: ...

class DescribeDatasetOutput(_message.Message):
    __slots__ = ["dataset"]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    dataset: _dataset_pb2.Dataset
    def __init__(self, dataset: _Optional[_Union[_dataset_pb2.Dataset, _Mapping]] = ...) -> None: ...

class DescribeEntryInput(_message.Message):
    __slots__ = ["dataset_id", "entry_id", "locale"]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    entry_id: str
    locale: str
    def __init__(self, dataset_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class DescribeEntryOutput(_message.Message):
    __slots__ = ["entry"]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _dataset_entry_pb2.Entry
    def __init__(self, entry: _Optional[_Union[_dataset_entry_pb2.Entry, _Mapping]] = ...) -> None: ...

class ListDatasetsInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "name", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListDatasetsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListDatasetsInput.Filter, _Mapping]] = ...) -> None: ...

class ListDatasetsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_dataset_pb2.Dataset]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_dataset_pb2.Dataset, _Mapping]]] = ...) -> None: ...

class ListEntriesInput(_message.Message):
    __slots__ = ["dataset_id", "filters", "locale", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "name", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    filters: ListEntriesInput.Filter
    locale: str
    offset: int
    size: int
    def __init__(self, dataset_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListEntriesInput.Filter, _Mapping]] = ..., locale: _Optional[str] = ...) -> None: ...

class ListEntriesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_dataset_entry_pb2.Entry]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_dataset_entry_pb2.Entry, _Mapping]]] = ...) -> None: ...

class ListTranslationsInput(_message.Message):
    __slots__ = ["dataset_id", "entry_id", "filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["locale"]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        def __init__(self, locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    entry_id: str
    filters: ListTranslationsInput.Filter
    offset: int
    size: int
    def __init__(self, dataset_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListTranslationsInput.Filter, _Mapping]] = ...) -> None: ...

class ListTranslationsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_dataset_entry_pb2.Entry.Translation]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_dataset_entry_pb2.Entry.Translation, _Mapping]]] = ...) -> None: ...

class TranslateEntryInput(_message.Message):
    __slots__ = ["entry_id", "locale", "translation"]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    entry_id: str
    locale: str
    translation: _dataset_entry_pb2.Entry.Translation
    def __init__(self, entry_id: _Optional[str] = ..., locale: _Optional[str] = ..., translation: _Optional[_Union[_dataset_entry_pb2.Entry.Translation, _Mapping]] = ...) -> None: ...

class TranslateEntryOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateDatasetInput(_message.Message):
    __slots__ = ["dataset", "dataset_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateDatasetInput.Patch
    DATASET_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    NAME: UpdateDatasetInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    dataset: _dataset_pb2.Dataset
    dataset_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateDatasetInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateDatasetInput.Patch, str]]] = ..., dataset_id: _Optional[str] = ..., dataset: _Optional[_Union[_dataset_pb2.Dataset, _Mapping]] = ...) -> None: ...

class UpdateDatasetOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UpdateEntryInput(_message.Message):
    __slots__ = ["dataset_id", "entry", "entry_id", "patch"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ABBR: UpdateEntryInput.Patch
    ALL: UpdateEntryInput.Patch
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    ENTRY_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE: UpdateEntryInput.Patch
    KEYWORDS: UpdateEntryInput.Patch
    NAME: UpdateEntryInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SUMMARY: UpdateEntryInput.Patch
    dataset_id: str
    entry: _dataset_entry_pb2.Entry
    entry_id: str
    patch: _containers.RepeatedScalarFieldContainer[UpdateEntryInput.Patch]
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateEntryInput.Patch, str]]] = ..., dataset_id: _Optional[str] = ..., entry_id: _Optional[str] = ..., entry: _Optional[_Union[_dataset_entry_pb2.Entry, _Mapping]] = ...) -> None: ...

class UpdateEntryOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
