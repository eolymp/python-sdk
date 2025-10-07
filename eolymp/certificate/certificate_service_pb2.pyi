from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.certificate import certificate_pb2 as _certificate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCertificateInput(_message.Message):
    __slots__ = ("certificate",)
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    certificate: _certificate_pb2.Certificate
    def __init__(self, certificate: _Optional[_Union[_certificate_pb2.Certificate, _Mapping]] = ...) -> None: ...

class CreateCertificateOutput(_message.Message):
    __slots__ = ("certificate_id", "download_url")
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    certificate_id: str
    download_url: str
    def __init__(self, certificate_id: _Optional[str] = ..., download_url: _Optional[str] = ...) -> None: ...

class VoidCertificateInput(_message.Message):
    __slots__ = ("certificate_id",)
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    certificate_id: str
    def __init__(self, certificate_id: _Optional[str] = ...) -> None: ...

class VoidCertificateOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeCertificateInput(_message.Message):
    __slots__ = ("certificate_id",)
    CERTIFICATE_ID_FIELD_NUMBER: _ClassVar[int]
    certificate_id: str
    def __init__(self, certificate_id: _Optional[str] = ...) -> None: ...

class DescribeCertificateOutput(_message.Message):
    __slots__ = ("certificate",)
    CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    certificate: _certificate_pb2.Certificate
    def __init__(self, certificate: _Optional[_Union[_certificate_pb2.Certificate, _Mapping]] = ...) -> None: ...

class ListCertificatesInput(_message.Message):
    __slots__ = ("offset", "size", "member_id")
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    offset: int
    size: int
    member_id: str
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., member_id: _Optional[str] = ...) -> None: ...

class ListCertificatesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_certificate_pb2.Certificate]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_certificate_pb2.Certificate, _Mapping]]] = ...) -> None: ...
