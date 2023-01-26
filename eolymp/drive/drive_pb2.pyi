from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.drive import file_pb2 as _file_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CompleteMultipartUploadInput(_message.Message):
    __slots__ = ["parts", "upload_id"]
    class Part(_message.Message):
        __slots__ = ["checksum_sha1", "etag", "number"]
        CHECKSUM_SHA1_FIELD_NUMBER: _ClassVar[int]
        ETAG_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        checksum_sha1: str
        etag: str
        number: int
        def __init__(self, number: _Optional[int] = ..., etag: _Optional[str] = ..., checksum_sha1: _Optional[str] = ...) -> None: ...
    PARTS_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    parts: _containers.RepeatedCompositeFieldContainer[CompleteMultipartUploadInput.Part]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ..., parts: _Optional[_Iterable[_Union[CompleteMultipartUploadInput.Part, _Mapping]]] = ...) -> None: ...

class CompleteMultipartUploadOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateFileInput(_message.Message):
    __slots__ = ["attributes", "data", "path", "type"]
    class AttributesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.ScalarMap[str, str]
    data: bytes
    path: str
    type: str
    def __init__(self, path: _Optional[str] = ..., type: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class CreateFileOutput(_message.Message):
    __slots__ = ["file_id"]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    def __init__(self, file_id: _Optional[str] = ...) -> None: ...

class DeleteFileInput(_message.Message):
    __slots__ = ["file_id"]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    def __init__(self, file_id: _Optional[str] = ...) -> None: ...

class DeleteFileOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeFileInput(_message.Message):
    __slots__ = ["file_id"]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    def __init__(self, file_id: _Optional[str] = ...) -> None: ...

class DescribeFileOutput(_message.Message):
    __slots__ = ["file"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _file_pb2.File
    def __init__(self, file: _Optional[_Union[_file_pb2.File, _Mapping]] = ...) -> None: ...

class ListFilesInput(_message.Message):
    __slots__ = ["filters", "offset", "size"]
    class Filter(_message.Message):
        __slots__ = ["created_at", "hash", "id", "path", "size", "type", "updated_at"]
        CREATED_AT_FIELD_NUMBER: _ClassVar[int]
        HASH_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
        created_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        hash: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        path: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        size: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionInt]
        type: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionEnum]
        updated_at: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionTimestamp]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., path: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., hash: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., size: _Optional[_Iterable[_Union[_expression_pb2.ExpressionInt, _Mapping]]] = ..., type: _Optional[_Iterable[_Union[_expression_pb2.ExpressionEnum, _Mapping]]] = ..., created_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ..., updated_at: _Optional[_Iterable[_Union[_expression_pb2.ExpressionTimestamp, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    filters: ListFilesInput.Filter
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListFilesInput.Filter, _Mapping]] = ...) -> None: ...

class ListFilesOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_file_pb2.File]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_file_pb2.File, _Mapping]]] = ...) -> None: ...

class StartMultipartUploadInput(_message.Message):
    __slots__ = ["attributes", "path", "type"]
    class AttributesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.ScalarMap[str, str]
    path: str
    type: str
    def __init__(self, path: _Optional[str] = ..., type: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ...) -> None: ...

class StartMultipartUploadOutput(_message.Message):
    __slots__ = ["upload_id"]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ...) -> None: ...

class UpdateFileInput(_message.Message):
    __slots__ = ["file", "file_id"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    file: _file_pb2.File
    file_id: str
    def __init__(self, file_id: _Optional[str] = ..., file: _Optional[_Union[_file_pb2.File, _Mapping]] = ...) -> None: ...

class UpdateFileOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class UploadPartInput(_message.Message):
    __slots__ = ["data", "part_number", "upload_id"]
    DATA_FIELD_NUMBER: _ClassVar[int]
    PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    part_number: int
    upload_id: str
    def __init__(self, upload_id: _Optional[str] = ..., part_number: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...

class UploadPartOutput(_message.Message):
    __slots__ = ["etag"]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    etag: str
    def __init__(self, etag: _Optional[str] = ...) -> None: ...
