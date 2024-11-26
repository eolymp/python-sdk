from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import statement_pb2 as _statement_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateStatementInput(_message.Message):
    __slots__ = ["statement"]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: _statement_pb2.Statement
    def __init__(self, statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class CreateStatementOutput(_message.Message):
    __slots__ = ["statement_id"]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    statement_id: str
    def __init__(self, statement_id: _Optional[str] = ...) -> None: ...

class DeleteStatementInput(_message.Message):
    __slots__ = ["statement_id"]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    statement_id: str
    def __init__(self, statement_id: _Optional[str] = ...) -> None: ...

class DeleteStatementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeStatementInput(_message.Message):
    __slots__ = ["extra", "render", "statement_id", "version"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_statement_pb2.Statement.Extra]
    render: bool
    statement_id: str
    version: int
    def __init__(self, statement_id: _Optional[str] = ..., render: bool = ..., version: _Optional[int] = ..., extra: _Optional[_Iterable[_Union[_statement_pb2.Statement.Extra, str]]] = ...) -> None: ...

class DescribeStatementOutput(_message.Message):
    __slots__ = ["statement"]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: _statement_pb2.Statement
    def __init__(self, statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class ListStatementsInput(_message.Message):
    __slots__ = ["extra", "offset", "render", "size", "version"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_statement_pb2.Statement.Extra]
    offset: int
    render: bool
    size: int
    version: int
    def __init__(self, offset: _Optional[int] = ..., size: _Optional[int] = ..., render: bool = ..., version: _Optional[int] = ..., extra: _Optional[_Iterable[_Union[_statement_pb2.Statement.Extra, str]]] = ...) -> None: ...

class ListStatementsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_statement_pb2.Statement]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_statement_pb2.Statement, _Mapping]]] = ...) -> None: ...

class LookupStatementInput(_message.Message):
    __slots__ = ["extra", "locale", "render", "version"]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    extra: _containers.RepeatedScalarFieldContainer[_statement_pb2.Statement.Extra]
    locale: str
    render: bool
    version: int
    def __init__(self, locale: _Optional[str] = ..., render: bool = ..., version: _Optional[int] = ..., extra: _Optional[_Iterable[_Union[_statement_pb2.Statement.Extra, str]]] = ...) -> None: ...

class LookupStatementOutput(_message.Message):
    __slots__ = ["statement"]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: _statement_pb2.Statement
    def __init__(self, statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class PreviewStatementInput(_message.Message):
    __slots__ = ["statement"]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: _statement_pb2.Statement
    def __init__(self, statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class PreviewStatementOutput(_message.Message):
    __slots__ = ["statement"]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: _statement_pb2.Statement
    def __init__(self, statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class StatementChangedEvent(_message.Message):
    __slots__ = ["after", "before", "problem_id"]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    after: _statement_pb2.Statement
    before: _statement_pb2.Statement
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ..., after: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class TranslateStatementsInput(_message.Message):
    __slots__ = ["override_manual", "source", "target", "target_automatic"]
    OVERRIDE_MANUAL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_AUTOMATIC_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    override_manual: bool
    source: str
    target: _containers.RepeatedScalarFieldContainer[str]
    target_automatic: bool
    def __init__(self, source: _Optional[str] = ..., target: _Optional[_Iterable[str]] = ..., target_automatic: bool = ..., override_manual: bool = ...) -> None: ...

class TranslateStatementsOutput(_message.Message):
    __slots__ = ["job_id"]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class UpdateStatementInput(_message.Message):
    __slots__ = ["patch", "statement", "statement_id"]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_statement_pb2.Statement.Patch]
    statement: _statement_pb2.Statement
    statement_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[_statement_pb2.Statement.Patch, str]]] = ..., statement_id: _Optional[str] = ..., statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class UpdateStatementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
