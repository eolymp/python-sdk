from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.executor import job_pb2 as _job_pb2
from eolymp.executor import language_pb2 as _language_pb2
from eolymp.executor import runtime_pb2 as _runtime_pb2
from eolymp.executor import task_pb2 as _task_pb2
from eolymp.wellknown import expression_pb2 as _expression_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTaskInput(_message.Message):
    __slots__ = ["job", "task"]
    JOB_FIELD_NUMBER: _ClassVar[int]
    TASK_FIELD_NUMBER: _ClassVar[int]
    job: _job_pb2.Job
    task: _task_pb2.Task
    def __init__(self, task: _Optional[_Union[_task_pb2.Task, _Mapping]] = ..., job: _Optional[_Union[_job_pb2.Job, _Mapping]] = ...) -> None: ...

class CreateTaskOutput(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DescribeCodeTemplateInput(_message.Message):
    __slots__ = ["runtime_id"]
    RUNTIME_ID_FIELD_NUMBER: _ClassVar[int]
    runtime_id: str
    def __init__(self, runtime_id: _Optional[str] = ...) -> None: ...

class DescribeCodeTemplateOutput(_message.Message):
    __slots__ = ["template"]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    template: str
    def __init__(self, template: _Optional[str] = ...) -> None: ...

class DescribeLanguageInput(_message.Message):
    __slots__ = ["language_id"]
    LANGUAGE_ID_FIELD_NUMBER: _ClassVar[int]
    language_id: str
    def __init__(self, language_id: _Optional[str] = ...) -> None: ...

class DescribeLanguageOutput(_message.Message):
    __slots__ = ["language"]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    language: _language_pb2.Language
    def __init__(self, language: _Optional[_Union[_language_pb2.Language, _Mapping]] = ...) -> None: ...

class DescribeRuntimeInput(_message.Message):
    __slots__ = ["runtime_id"]
    RUNTIME_ID_FIELD_NUMBER: _ClassVar[int]
    runtime_id: str
    def __init__(self, runtime_id: _Optional[str] = ...) -> None: ...

class DescribeRuntimeOutput(_message.Message):
    __slots__ = ["runtime"]
    RUNTIME_FIELD_NUMBER: _ClassVar[int]
    runtime: _runtime_pb2.Runtime
    def __init__(self, runtime: _Optional[_Union[_runtime_pb2.Runtime, _Mapping]] = ...) -> None: ...

class ListLanguagesInput(_message.Message):
    __slots__ = ["filters"]
    class Filter(_message.Message):
        __slots__ = ["deprecated", "id", "name"]
        DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        deprecated: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., deprecated: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: ListLanguagesInput.Filter
    def __init__(self, filters: _Optional[_Union[ListLanguagesInput.Filter, _Mapping]] = ...) -> None: ...

class ListLanguagesOutput(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_language_pb2.Language]
    def __init__(self, items: _Optional[_Iterable[_Union[_language_pb2.Language, _Mapping]]] = ...) -> None: ...

class ListRuntimeInput(_message.Message):
    __slots__ = ["filters"]
    class Filter(_message.Message):
        __slots__ = ["deprecated", "id", "lang", "name", "version"]
        DEPRECATED_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        LANG_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        deprecated: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionBool]
        id: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        lang: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        name: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionString]
        version: _containers.RepeatedCompositeFieldContainer[_expression_pb2.ExpressionID]
        def __init__(self, id: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., lang: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., version: _Optional[_Iterable[_Union[_expression_pb2.ExpressionID, _Mapping]]] = ..., name: _Optional[_Iterable[_Union[_expression_pb2.ExpressionString, _Mapping]]] = ..., deprecated: _Optional[_Iterable[_Union[_expression_pb2.ExpressionBool, _Mapping]]] = ...) -> None: ...
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: ListRuntimeInput.Filter
    def __init__(self, filters: _Optional[_Union[ListRuntimeInput.Filter, _Mapping]] = ...) -> None: ...

class ListRuntimeOutput(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_runtime_pb2.Runtime]
    def __init__(self, items: _Optional[_Iterable[_Union[_runtime_pb2.Runtime, _Mapping]]] = ...) -> None: ...
