from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResourceUsage(_message.Message):
    __slots__ = ("user_cpu_time", "system_cpu_time", "max_resident_set_size", "page_reclaims", "page_faults", "block_input_operations", "block_output_operations", "voluntary_context_switches", "involuntary_context_switches")
    USER_CPU_TIME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_CPU_TIME_FIELD_NUMBER: _ClassVar[int]
    MAX_RESIDENT_SET_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_RECLAIMS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FAULTS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_INPUT_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_OUTPUT_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    VOLUNTARY_CONTEXT_SWITCHES_FIELD_NUMBER: _ClassVar[int]
    INVOLUNTARY_CONTEXT_SWITCHES_FIELD_NUMBER: _ClassVar[int]
    user_cpu_time: int
    system_cpu_time: int
    max_resident_set_size: int
    page_reclaims: int
    page_faults: int
    block_input_operations: int
    block_output_operations: int
    voluntary_context_switches: int
    involuntary_context_switches: int
    def __init__(self, user_cpu_time: _Optional[int] = ..., system_cpu_time: _Optional[int] = ..., max_resident_set_size: _Optional[int] = ..., page_reclaims: _Optional[int] = ..., page_faults: _Optional[int] = ..., block_input_operations: _Optional[int] = ..., block_output_operations: _Optional[int] = ..., voluntary_context_switches: _Optional[int] = ..., involuntary_context_switches: _Optional[int] = ...) -> None: ...
