from eolymp.community import configuration_idp_pb2 as _configuration_idp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IdentityConfig(_message.Message):
    __slots__ = ("local", "basecamp", "oidc", "display_name_type", "display_name_attribute", "allow_sign_up", "require_email_verified")
    class DisplayNameType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_DISPLAY_NAME: _ClassVar[IdentityConfig.DisplayNameType]
        NICKNAME: _ClassVar[IdentityConfig.DisplayNameType]
        NAME: _ClassVar[IdentityConfig.DisplayNameType]
        ATTRIBUTE: _ClassVar[IdentityConfig.DisplayNameType]
    UNKNOWN_DISPLAY_NAME: IdentityConfig.DisplayNameType
    NICKNAME: IdentityConfig.DisplayNameType
    NAME: IdentityConfig.DisplayNameType
    ATTRIBUTE: IdentityConfig.DisplayNameType
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    BASECAMP_FIELD_NUMBER: _ClassVar[int]
    OIDC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SIGN_UP_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    local: _configuration_idp_pb2.IdentityProvider.Local
    basecamp: _configuration_idp_pb2.IdentityProvider.Basecamp
    oidc: _configuration_idp_pb2.IdentityProvider.OIDC
    display_name_type: IdentityConfig.DisplayNameType
    display_name_attribute: str
    allow_sign_up: bool
    require_email_verified: bool
    def __init__(self, local: _Optional[_Union[_configuration_idp_pb2.IdentityProvider.Local, _Mapping]] = ..., basecamp: _Optional[_Union[_configuration_idp_pb2.IdentityProvider.Basecamp, _Mapping]] = ..., oidc: _Optional[_Union[_configuration_idp_pb2.IdentityProvider.OIDC, _Mapping]] = ..., display_name_type: _Optional[_Union[IdentityConfig.DisplayNameType, str]] = ..., display_name_attribute: _Optional[str] = ..., allow_sign_up: bool = ..., require_email_verified: bool = ...) -> None: ...
