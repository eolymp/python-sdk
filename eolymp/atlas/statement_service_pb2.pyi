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
    __slots__ = ["problem_id", "statement"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    statement: _statement_pb2.Statement
    def __init__(self, problem_id: _Optional[str] = ..., statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class CreateStatementOutput(_message.Message):
    __slots__ = ["statement_id"]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    statement_id: str
    def __init__(self, statement_id: _Optional[str] = ...) -> None: ...

class DeleteStatementInput(_message.Message):
    __slots__ = ["problem_id", "statement_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    statement_id: str
    def __init__(self, problem_id: _Optional[str] = ..., statement_id: _Optional[str] = ...) -> None: ...

class DeleteStatementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeStatementInput(_message.Message):
    __slots__ = ["problem_id", "statement_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    statement_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., statement_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DescribeStatementOutput(_message.Message):
    __slots__ = ["statement"]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: _statement_pb2.Statement
    def __init__(self, statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class ListStatementsInput(_message.Message):
    __slots__ = ["problem_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ListStatementsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_statement_pb2.Statement]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_statement_pb2.Statement, _Mapping]]] = ...) -> None: ...

class LookupStatementInput(_message.Message):
    __slots__ = ["preferred_locale", "problem_id", "version"]
    PREFERRED_LOCALE_FIELD_NUMBER: _ClassVar[int]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    preferred_locale: _containers.RepeatedScalarFieldContainer[str]
    problem_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., preferred_locale: _Optional[_Iterable[str]] = ..., version: _Optional[int] = ...) -> None: ...

class LookupStatementOutput(_message.Message):
    __slots__ = ["statement"]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: _statement_pb2.Statement
    def __init__(self, statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class PreviewStatementInput(_message.Message):
    __slots__ = ["problem_id", "statement"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    statement: _statement_pb2.Statement
    def __init__(self, problem_id: _Optional[str] = ..., statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class PreviewStatementOutput(_message.Message):
    __slots__ = ["statement"]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: _statement_pb2.Statement
    def __init__(self, statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class RenderStatementInput(_message.Message):
    __slots__ = ["problem_id", "statement_id", "version"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    statement_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., statement_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class RenderStatementOutput(_message.Message):
    __slots__ = ["statement"]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: _statement_pb2.Statement
    def __init__(self, statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class UpdateStatementInput(_message.Message):
    __slots__ = ["problem_id", "statement", "statement_id"]
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    statement: _statement_pb2.Statement
    statement_id: str
    def __init__(self, problem_id: _Optional[str] = ..., statement_id: _Optional[str] = ..., statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class UpdateStatementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
