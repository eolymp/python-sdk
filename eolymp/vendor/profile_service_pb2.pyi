from eolymp.annotations import http_pb2 as _http_pb2
from eolymp.annotations import ratelimit_pb2 as _ratelimit_pb2
from eolymp.annotations import scope_pb2 as _scope_pb2
from eolymp.vendor import profile_pb2 as _profile_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DescribeProfileInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeProfileOutput(_message.Message):
    __slots__ = ("profile",)
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    profile: _profile_pb2.Profile
    def __init__(self, profile: _Optional[_Union[_profile_pb2.Profile, _Mapping]] = ...) -> None: ...

class UpdateProfileInput(_message.Message):
    __slots__ = ("patch", "profile")
    PATCH_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    patch: _containers.RepeatedScalarFieldContainer[_profile_pb2.Profile.Patch.Field]
    profile: _profile_pb2.Profile
    def __init__(self, patch: _Optional[_Iterable[_Union[_profile_pb2.Profile.Patch.Field, str]]] = ..., profile: _Optional[_Union[_profile_pb2.Profile, _Mapping]] = ...) -> None: ...

class UpdateProfileOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubmitProfileInput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SubmitProfileOutput(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
