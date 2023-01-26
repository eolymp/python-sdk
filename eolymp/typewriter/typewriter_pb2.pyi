from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.typewriter import fragment_pb2 as _fragment_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFragmentInput(_message.Message):
    __slots__ = ["fragment"]
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    fragment: _fragment_pb2.Fragment
    def __init__(self, fragment: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ...) -> None: ...

class CreateFragmentOutput(_message.Message):
    __slots__ = ["fragment_id"]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    def __init__(self, fragment_id: _Optional[str] = ...) -> None: ...

class DeleteFragmentInput(_message.Message):
    __slots__ = ["fragment_id"]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    def __init__(self, fragment_id: _Optional[str] = ...) -> None: ...

class DeleteFragmentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeFragmentInput(_message.Message):
    __slots__ = ["fragment_id"]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    fragment_id: str
    def __init__(self, fragment_id: _Optional[str] = ...) -> None: ...

class DescribeFragmentOutput(_message.Message):
    __slots__ = ["fragment"]
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    fragment: _fragment_pb2.Fragment
    def __init__(self, fragment: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ...) -> None: ...

class DescribePathInput(_message.Message):
    __slots__ = ["path", "preferred_locales"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_LOCALES_FIELD_NUMBER: _ClassVar[int]
    path: str
    preferred_locales: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, path: _Optional[str] = ..., preferred_locales: _Optional[_Iterable[str]] = ...) -> None: ...

class DescribePathOutput(_message.Message):
    __slots__ = ["fragment"]
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    fragment: _fragment_pb2.Fragment
    def __init__(self, fragment: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ...) -> None: ...

class ListFragmentsInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["id", "locale", "path", "query"]
        ID_FIELD_NUMBER: _ClassVar[int]
        LOCALE_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        locale: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        path: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        def __init__(self, query: _Optional[str] = ..., id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., path: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., locale: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListFragmentsInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListFragmentsInput.Filter, _Mapping]] = ...) -> None: ...

class ListFragmentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_fragment_pb2.Fragment]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_fragment_pb2.Fragment, _Mapping]]] = ...) -> None: ...

class ListParentsInput(_message.Message):
    __slots__ = ["path", "preferred_locales"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_LOCALES_FIELD_NUMBER: _ClassVar[int]
    path: str
    preferred_locales: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, path: _Optional[str] = ..., preferred_locales: _Optional[_Iterable[str]] = ...) -> None: ...

class ListParentsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_fragment_pb2.Fragment]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_fragment_pb2.Fragment, _Mapping]]] = ...) -> None: ...

class ListPathsInput(_message.Message):
    __slots__ = ["filters", "offset", "preferred_locales", "size"]
    class Filter(_message.Message):
        __slots__ = ["label", "path", "query"]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        label: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        path: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        query: str
        def __init__(self, query: _Optional[str] = ..., path: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., label: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_LOCALES_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListPathsInput.Filter
    offset: int
    preferred_locales: _containers.RepeatedScalarFieldContainer[str]
    size: int
    def __init__(self, preferred_locales: _Optional[_Iterable[str]] = ..., offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListPathsInput.Filter, _Mapping]] = ...) -> None: ...

class ListPathsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_fragment_pb2.Fragment]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_fragment_pb2.Fragment, _Mapping]]] = ...) -> None: ...

class UpdateFragmentInput(_message.Message):
    __slots__ = ["fragment", "fragment_id"]
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
    fragment: _fragment_pb2.Fragment
    fragment_id: str
    def __init__(self, fragment_id: _Optional[str] = ..., fragment: _Optional[_Union[_fragment_pb2.Fragment, _Mapping]] = ...) -> None: ...

class UpdateFragmentOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UploadAssetInput(_message.Message):
    __slots__ = ["data", "filename"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    filename: str
    def __init__(self, filename: _Optional[str] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadAssetOutput(_message.Message):
    __slots__ = ["link"]
    LINK_FIELD_NUMBER: _ClassVar[int]
    link: str
    def __init__(self, link: _Optional[str] = ...) -> None: ...
