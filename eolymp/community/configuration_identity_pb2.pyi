from eolymp.community import configuration_idp_pb2 as _configuration_idp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IdentityConfig(_message.Message):
    __slots__ = ["allow_sign_up", "basecamp", "display_name_attribute", "display_name_type", "local", "oidc"]
    class DisplayNameType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ALLOW_SIGN_UP_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE: IdentityConfig.DisplayNameType
    BASECAMP_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    NAME: IdentityConfig.DisplayNameType
    NICKNAME: IdentityConfig.DisplayNameType
    OIDC_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_DISPLAY_NAME: IdentityConfig.DisplayNameType
    allow_sign_up: bool
    basecamp: _configuration_idp_pb2.IdentityProvider.Basecamp
    display_name_attribute: str
    display_name_type: IdentityConfig.DisplayNameType
    local: _configuration_idp_pb2.IdentityProvider.Local
    oidc: _configuration_idp_pb2.IdentityProvider.OIDC
    def __init__(self, local: _Optional[_Union[_configuration_idp_pb2.IdentityProvider.Local, _Mapping]] = ..., basecamp: _Optional[_Union[_configuration_idp_pb2.IdentityProvider.Basecamp, _Mapping]] = ..., oidc: _Optional[_Union[_configuration_idp_pb2.IdentityProvider.OIDC, _Mapping]] = ..., display_name_type: _Optional[_Union[IdentityConfig.DisplayNameType, str]] = ..., display_name_attribute: _Optional[str] = ..., allow_sign_up: bool = ...) -> None: ...
