from eolymp.annotations import audit_pb2 as _audit_pb2
from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import namespace_pb2 as _namespace_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.atlas import widget_pb2 as _widget_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetChangedEvent(_message.Message):
    __slots__ = ("problem_id", "before", "after")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_FIELD_NUMBER: _ClassVar[int]
    AFTER_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    before: _widget_pb2.Widget
    after: _widget_pb2.Widget
    def __init__(self, problem_id: _Optional[str] = ..., before: _Optional[_Union[_widget_pb2.Widget, _Mapping]] = ..., after: _Optional[_Union[_widget_pb2.Widget, _Mapping]] = ...) -> None: ...

class UpdateWidgetInput(_message.Message):
    __slots__ = ("problem_id", "widget")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    WIDGET_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    widget: _widget_pb2.Widget
    def __init__(self, problem_id: _Optional[str] = ..., widget: _Optional[_Union[_widget_pb2.Widget, _Mapping]] = ...) -> None: ...

class UpdateWidgetOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteWidgetInput(_message.Message):
    __slots__ = ("problem_id",)
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    def __init__(self, problem_id: _Optional[str] = ...) -> None: ...

class DeleteWidgetOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeWidgetInput(_message.Message):
    __slots__ = ("problem_id", "version")
    PROBLEM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    problem_id: str
    version: int
    def __init__(self, problem_id: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DescribeWidgetOutput(_message.Message):
    __slots__ = ("widget",)
    WIDGET_FIELD_NUMBER: _ClassVar[int]
    widget: _widget_pb2.Widget
    def __init__(self, widget: _Optional[_Union[_widget_pb2.Widget, _Mapping]] = ...) -> None: ...
