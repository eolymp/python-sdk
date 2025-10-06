from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Certificate(_message.Message):
    __slots__ = ("id", "use", "type", "algorithm", "rsa_exponent", "rsa_modulus", "ec_curve", "ec_x", "ec_y")
    ID_FIELD_NUMBER: _ClassVar[int]
    USE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    RSA_EXPONENT_FIELD_NUMBER: _ClassVar[int]
    RSA_MODULUS_FIELD_NUMBER: _ClassVar[int]
    EC_CURVE_FIELD_NUMBER: _ClassVar[int]
    EC_X_FIELD_NUMBER: _ClassVar[int]
    EC_Y_FIELD_NUMBER: _ClassVar[int]
    id: str
    use: str
    type: str
    algorithm: str
    rsa_exponent: str
    rsa_modulus: str
    ec_curve: str
    ec_x: str
    ec_y: str
    def __init__(self, id: _Optional[str] = ..., use: _Optional[str] = ..., type: _Optional[str] = ..., algorithm: _Optional[str] = ..., rsa_exponent: _Optional[str] = ..., rsa_modulus: _Optional[str] = ..., ec_curve: _Optional[str] = ..., ec_x: _Optional[str] = ..., ec_y: _Optional[str] = ...) -> None: ...
