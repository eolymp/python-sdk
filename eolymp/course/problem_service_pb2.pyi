from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import code_template_pb2 as _code_template_pb2
from eolymp.atlas import question_pb2 as _question_pb2
from eolymp.atlas import statement_pb2 as _statement_pb2
from eolymp.atlas import testing_test_pb2 as _testing_test_pb2
from eolymp.course import run_service_pb2 as _run_service_pb2
from eolymp.course import submission_service_pb2 as _submission_service_pb2
from eolymp.runtime import runtime_pb2 as _runtime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListStatementsInput(_message.Message):
    __slots__ = ("course_id", "material_id")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    material_id: str
    def __init__(self, course_id: _Optional[str] = ..., material_id: _Optional[str] = ...) -> None: ...

class ListStatementsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_statement_pb2.Statement]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_statement_pb2.Statement, _Mapping]]] = ...) -> None: ...

class ListQuestionsInput(_message.Message):
    __slots__ = ("course_id", "material_id")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    material_id: str
    def __init__(self, course_id: _Optional[str] = ..., material_id: _Optional[str] = ...) -> None: ...

class ListQuestionsOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_question_pb2.Question]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_question_pb2.Question, _Mapping]]] = ...) -> None: ...

class LookupStatementInput(_message.Message):
    __slots__ = ("course_id", "material_id", "locale")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    material_id: str
    locale: str
    def __init__(self, course_id: _Optional[str] = ..., material_id: _Optional[str] = ..., locale: _Optional[str] = ...) -> None: ...

class LookupStatementOutput(_message.Message):
    __slots__ = ("statement",)
    STATEMENT_FIELD_NUMBER: _ClassVar[int]
    statement: _statement_pb2.Statement
    def __init__(self, statement: _Optional[_Union[_statement_pb2.Statement, _Mapping]] = ...) -> None: ...

class ListExamplesInput(_message.Message):
    __slots__ = ("course_id", "material_id")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    material_id: str
    def __init__(self, course_id: _Optional[str] = ..., material_id: _Optional[str] = ...) -> None: ...

class ListExamplesOutput(_message.Message):
    __slots__ = ("examples",)
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    examples: _containers.RepeatedCompositeFieldContainer[_testing_test_pb2.Test]
    def __init__(self, examples: _Optional[_Iterable[_Union[_testing_test_pb2.Test, _Mapping]]] = ...) -> None: ...

class LookupCodeTemplateInput(_message.Message):
    __slots__ = ("course_id", "material_id", "runtime")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    material_id: str
    runtime: str
    def __init__(self, course_id: _Optional[str] = ..., material_id: _Optional[str] = ..., runtime: _Optional[str] = ...) -> None: ...

class LookupCodeTemplateOutput(_message.Message):
    __slots__ = ("template",)
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: _code_template_pb2.Template
    def __init__(self, template: _Optional[_Union[_code_template_pb2.Template, _Mapping]] = ...) -> None: ...

class ListRuntimesInput(_message.Message):
    __slots__ = ("course_id", "material_id")
    COURSE_ID_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_ID_FIELD_NUMBER: _ClassVar[int]
    course_id: str
    material_id: str
    def __init__(self, course_id: _Optional[str] = ..., material_id: _Optional[str] = ...) -> None: ...

class ListRuntimesOutput(_message.Message):
    __slots__ = ("total", "items")
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    total: int
    items: _containers.RepeatedCompositeFieldContainer[_runtime_pb2.Runtime]
    def __init__(self, total: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_runtime_pb2.Runtime, _Mapping]]] = ...) -> None: ...
