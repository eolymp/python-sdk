from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import attachment_pb2 as _attachment_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAttachmentInput(_message.Message):
    __slots__ = ("attachment",)
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    attachment: _attachment_pb2.Attachment
    def __init__(self, attachment: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]] = ...) -> None: ...

class CreateAttachmentOutput(_message.Message):
    __slots__ = ("attachment_id",)
    ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    attachment_id: str
    def __init__(self, attachment_id: _Optional[str] = ...) -> None: ...

class UpdateAttachmentInput(_message.Message):
    __slots__ = ("attachment_id", "attachment")
    ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    attachment_id: str
    attachment: _attachment_pb2.Attachment
    def __init__(self, attachment_id: _Optional[str] = ..., attachment: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]] = ...) -> None: ...

class UpdateAttachmentOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteAttachmentInput(_message.Message):
    __slots__ = ("attachment_id",)
    ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    attachment_id: str
    def __init__(self, attachment_id: _Optional[str] = ...) -> None: ...

class DeleteAttachmentOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListAttachmentsInput(_message.Message):
    __slots__ = ("offset", "size", "filters", "version")
    class Filter(_message.Message):
        __slots__ = ("id", "name")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ...) -> None: ...
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    filters: ListAttachmentsInput.Filter
    version: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., filters: _Optional[_Union[ListAttachmentsInput.Filter, _Mapping]] = ..., version: _Optional[int] = ...) -> None: ...

class ListAttachmentsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_attachment_pb2.Attachment]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_attachment_pb2.Attachment, _Mapping]]] = ...) -> None: ...

class DescribeAttachmentInput(_message.Message):
    __slots__ = ("attachment_id", "version")
    ATTACHMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    attachment_id: str
    version: int
    def __init__(self, attachment_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DescribeAttachmentOutput(_message.Message):
    __slots__ = ("attachment",)
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    attachment: _attachment_pb2.Attachment
    def __init__(self, attachment: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]] = ...) -> None: ...
