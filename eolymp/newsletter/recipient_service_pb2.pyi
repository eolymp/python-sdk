from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.newsletter import recipient_pb2 as _recipient_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRecipientInput(_message.Message):
    __slots__ = ["recipient"]
    RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    recipient: _recipient_pb2.Recipient
    def __init__(self, recipient: _Optional[_Union[_recipient_pb2.Recipient, _Mapping]] = ...) -> None: ...

class CreateRecipientOutput(_message.Message):
    __slots__ = ["recipient_id"]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    recipient_id: str
    def __init__(self, recipient_id: _Optional[str] = ...) -> None: ...

class DescribeRecipientInput(_message.Message):
    __slots__ = ["recipient_id"]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    recipient_id: str
    def __init__(self, recipient_id: _Optional[str] = ...) -> None: ...

class DescribeRecipientOutput(_message.Message):
    __slots__ = ["recipient"]
    RECIPIENT_FIELD_NUMBER: _ClassVar[int]
    recipient: _recipient_pb2.Recipient
    def __init__(self, recipient: _Optional[_Union[_recipient_pb2.Recipient, _Mapping]] = ...) -> None: ...

class ImportRecipientsInput(_message.Message):
    __slots__ = ["group_id"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    def __init__(self, group_id: _Optional[str] = ...) -> None: ...

class ImportRecipientsOutput(_message.Message):
    __slots__ = ["imported_total"]
    IMPORTED_TOTAL_FIELD_NUMBER: _ClassVar[int]
    imported_total: str
    def __init__(self, imported_total: _Optional[str] = ...) -> None: ...

class ListRecipientsInput(_message.Message):
    __slots__ = ["offset", "size"]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ...) -> None: ...

class ListRecipientsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_recipient_pb2.Recipient]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_recipient_pb2.Recipient, _Mapping]]] = ...) -> None: ...

class RemoveRecipientInput(_message.Message):
    __slots__ = ["recipient_id"]
    RECIPIENT_ID_FIELD_NUMBER: _ClassVar[int]
    recipient_id: str
    def __init__(self, recipient_id: _Optional[str] = ...) -> None: ...

class RemoveRecipientOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
