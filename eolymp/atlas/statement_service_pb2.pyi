from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import statement_pb2 as _statement_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
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
    __slots__ = ["render", "statement_id", "version"]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    render: bool
    statement_id: str
    version: int
    def __init__(self, statement_id: _Optional[str] = ..., render: bool = ..., version: _Optional[int] = ...) -> None: ...

class DescribeStatementOutput(_message.Message):
    __slots__ = ["statement"]
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: _statement_pb2.Statement
    def __init__(self, statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class ListStatementsInput(_message.Message):
    __slots__ = ["render", "version"]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    render: bool
    version: int
    def __init__(self, render: bool = ..., version: _Optional[int] = ...) -> None: ...

class ListStatementsOutput(_message.Message):
    __slots__ = ["items", "total"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_statement_pb2.Statement]
    total: int
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_statement_pb2.Statement, _Mapping]]] = ...) -> None: ...

class LookupStatementInput(_message.Message):
    __slots__ = ["locale", "render", "version"]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    RENDER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    locale: str
    render: bool
    version: int
    def __init__(self, locale: _Optional[str] = ..., render: bool = ..., version: _Optional[int] = ...) -> None: ...

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

class UpdateStatementInput(_message.Message):
    __slots__ = ["patch", "statement", "statement_id"]
    class Patch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALL: UpdateStatementInput.Patch
    AUTHOR: UpdateStatementInput.Patch
    CONTENT: UpdateStatementInput.Patch
    DOWNLOAD_LINK: UpdateStatementInput.Patch
    LOCALE: UpdateStatementInput.Patch
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SOURCE: UpdateStatementInput.Patch
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    STATEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE: UpdateStatementInput.Patch
    patch: _containers.RepeatedScalarFieldContainer[UpdateStatementInput.Patch]
    statement: _statement_pb2.Statement
    statement_id: str
    def __init__(self, patch: _Optional[_Iterable[_Union[UpdateStatementInput.Patch, str]]] = ..., statement_id: _Optional[str] = ..., statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class UpdateStatementOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
