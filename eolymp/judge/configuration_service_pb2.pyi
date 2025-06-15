from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.judge import contest_certification_pb2 as _contest_certification_pb2
from eolymp.judge import contest_environment_pb2 as _contest_environment_pb2
from eolymp.judge import contest_taxonomy_pb2 as _contest_taxonomy_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeEnvironmentInput(_message.Message):
    __slots__ = ("contest_id",)
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class DescribeEnvironmentOutput(_message.Message):
    __slots__ = ("environment",)
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    environment: _contest_environment_pb2.Environment
    def __init__(self, environment: _Optional[_Union[_contest_environment_pb2.Environment, _Mapping]] = ...) -> None: ...

class ConfigureEnvironmentInput(_message.Message):
    __slots__ = ("contest_id", "environment")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    environment: _contest_environment_pb2.Environment
    def __init__(self, contest_id: _Optional[str] = ..., environment: _Optional[_Union[_contest_environment_pb2.Environment, _Mapping]] = ...) -> None: ...

class ConfigureEnvironmentOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeCertificationInput(_message.Message):
    __slots__ = ("contest_id",)
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class DescribeCertificationOutput(_message.Message):
    __slots__ = ("certification",)
    CERTIFICATION_FIELD_NUMBER: _ClassVar[int]
    certification: _contest_certification_pb2.Certification
    def __init__(self, certification: _Optional[_Union[_contest_certification_pb2.Certification, _Mapping]] = ...) -> None: ...

class ConfigureCertificationInput(_message.Message):
    __slots__ = ("contest_id", "certification")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATION_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    certification: _contest_certification_pb2.Certification
    def __init__(self, contest_id: _Optional[str] = ..., certification: _Optional[_Union[_contest_certification_pb2.Certification, _Mapping]] = ...) -> None: ...

class ConfigureCertificationOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeTaxonomyInput(_message.Message):
    __slots__ = ("contest_id",)
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    def __init__(self, contest_id: _Optional[str] = ...) -> None: ...

class DescribeTaxonomyOutput(_message.Message):
    __slots__ = ("taxonomy",)
    TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    taxonomy: _contest_taxonomy_pb2.Taxonomy
    def __init__(self, taxonomy: _Optional[_Union[_contest_taxonomy_pb2.Taxonomy, _Mapping]] = ...) -> None: ...

class ConfigureTaxonomyInput(_message.Message):
    __slots__ = ("contest_id", "taxonomy")
    CONTEST_ID_FIELD_NUMBER: _ClassVar[int]
    TAXONOMY_FIELD_NUMBER: _ClassVar[int]
    contest_id: str
    taxonomy: _contest_taxonomy_pb2.Taxonomy
    def __init__(self, contest_id: _Optional[str] = ..., taxonomy: _Optional[_Union[_contest_taxonomy_pb2.Taxonomy, _Mapping]] = ...) -> None: ...

class ConfigureTaxonomyOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
