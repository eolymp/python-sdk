from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserConfig(_message.Message):
    __slots__ = ["basecamp", "display_name", "display_name_attribute", "local", "oidc"]
    class DisplayName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class BasecampProvider(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class LocalProvider(_message.Message):
        __slots__ = ["allow_modify_basics", "allow_modify_email", "allow_modify_nickname", "allow_modify_password"]
        ALLOW_MODIFY_BASICS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_MODIFY_EMAIL_FIELD_NUMBER: _ClassVar[int]
        ALLOW_MODIFY_NICKNAME_FIELD_NUMBER: _ClassVar[int]
        ALLOW_MODIFY_PASSWORD_FIELD_NUMBER: _ClassVar[int]
        allow_modify_basics: bool
        allow_modify_email: bool
        allow_modify_nickname: bool
        allow_modify_password: bool
        def __init__(self, allow_modify_password: bool = ..., allow_modify_basics: bool = ..., allow_modify_email: bool = ..., allow_modify_nickname: bool = ...) -> None: ...
    class OIDCProvider(_message.Message):
        __slots__ = ["authorize_endpoint", "client_id", "client_secret", "issuer", "keys_endpoint", "redirect_uri", "token_endpoint", "userinfo_endpoint"]
        AUTHORIZE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
        ISSUER_FIELD_NUMBER: _ClassVar[int]
        KEYS_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        REDIRECT_URI_FIELD_NUMBER: _ClassVar[int]
        TOKEN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        USERINFO_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
        authorize_endpoint: str
        client_id: str
        client_secret: str
        issuer: str
        keys_endpoint: str
        redirect_uri: str
        token_endpoint: str
        userinfo_endpoint: str
        def __init__(self, client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., issuer: _Optional[str] = ..., authorize_endpoint: _Optional[str] = ..., token_endpoint: _Optional[str] = ..., keys_endpoint: _Optional[str] = ..., userinfo_endpoint: _Optional[str] = ..., redirect_uri: _Optional[str] = ...) -> None: ...
    ATTRIBUTE: UserConfig.DisplayName
    BASECAMP_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    LOGIN: UserConfig.DisplayName
    NAME: UserConfig.DisplayName
    OIDC_FIELD_NUMBER: _ClassVar[int]
    basecamp: UserConfig.BasecampProvider
    display_name: UserConfig.DisplayName
    display_name_attribute: str
    local: UserConfig.LocalProvider
    oidc: UserConfig.OIDCProvider
    def __init__(self, basecamp: _Optional[_Union[UserConfig.BasecampProvider, _Mapping]] = ..., local: _Optional[_Union[UserConfig.LocalProvider, _Mapping]] = ..., oidc: _Optional[_Union[UserConfig.OIDCProvider, _Mapping]] = ..., display_name: _Optional[_Union[UserConfig.DisplayName, str]] = ..., display_name_attribute: _Optional[str] = ...) -> None: ...
