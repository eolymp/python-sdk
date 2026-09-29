from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Action(_message.Message):
    __slots__ = ("agentic", "scripted")
    class AgenticAction(_message.Message):
        __slots__ = ("instructions",)
        INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
        instructions: str
        def __init__(self, instructions: _Optional[str] = ...) -> None: ...
    class ScriptedAction(_message.Message):
        __slots__ = ("script",)
        SCRIPT_FIELD_NUMBER: _ClassVar[int]
        script: str
        def __init__(self, script: _Optional[str] = ...) -> None: ...
    AGENTIC_FIELD_NUMBER: _ClassVar[int]
    SCRIPTED_FIELD_NUMBER: _ClassVar[int]
    agentic: Action.AgenticAction
    scripted: Action.ScriptedAction
    def __init__(self, agentic: _Optional[_Union[Action.AgenticAction, _Mapping]] = ..., scripted: _Optional[_Union[Action.ScriptedAction, _Mapping]] = ...) -> None: ...
