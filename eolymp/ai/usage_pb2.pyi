from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Usage(_message.Message):
    __slots__ = ("prompt_tokens", "completion_tokens", "thinking_tokens", "total_tokens", "cached_prompt_tokens")
    PROMPT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    THINKING_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CACHED_PROMPT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    prompt_tokens: int
    completion_tokens: int
    thinking_tokens: int
    total_tokens: int
    cached_prompt_tokens: int
    def __init__(self, prompt_tokens: _Optional[int] = ..., completion_tokens: _Optional[int] = ..., thinking_tokens: _Optional[int] = ..., total_tokens: _Optional[int] = ..., cached_prompt_tokens: _Optional[int] = ...) -> None: ...
