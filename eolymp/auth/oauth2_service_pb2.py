# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/auth/oauth2_service.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'eolymp/auth/oauth2_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.auth import claims_pb2 as eolymp_dot_auth_dot_claims__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n eolymp/auth/oauth2_service.proto\x12\x0b\x65olymp.auth\x1a\"eolymp/annotations/ratelimit.proto\x1a\x18\x65olymp/auth/claims.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xdf\x02\n\x0fIssueTokenInput\x12:\n\ngrant_type\x18\x01 \x01(\x0e\x32&.eolymp.auth.IssueTokenInput.GrantType\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x11\n\tclient_id\x18\x04 \x01(\t\x12\x15\n\rclient_secret\x18\x05 \x01(\t\x12\x0c\n\x04\x63ode\x18\x06 \x01(\t\x12\x15\n\rcode_verifier\x18\x07 \x01(\t\x12\r\n\x05scope\x18\x08 \x01(\t\x12\x15\n\rrefresh_token\x18\t \x01(\t\x12\x14\n\x0credirect_uri\x18\n \x01(\t\"a\n\tGrantType\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08PASSWORD\x10\x01\x12\x16\n\x12\x41UTHORIZATION_CODE\x10\x02\x12\x11\n\rREFRESH_TOKEN\x10\x03\x12\x11\n\rEOLYMP_SIGNIN\x10\x04\"\xad\x01\n\x10IssueTokenOutput\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x12\n\ntoken_type\x18\x02 \x01(\t\x12\x12\n\nexpires_in\x18\x03 \x01(\r\x12\x15\n\rrefresh_token\x18\x04 \x01(\t\x12\r\n\x05scope\x18\x05 \x01(\t\x12#\n\x06\x63laims\x18\n \x01(\x0b\x32\x13.eolymp.auth.Claims\x12\x10\n\x08id_token\x18\x64 \x01(\t\"%\n\x14IntrospectTokenInput\x12\r\n\x05token\x18\x01 \x01(\t\"\x87\x01\n\x15IntrospectTokenOutput\x12\x0e\n\x06\x61\x63tive\x18\x01 \x01(\x08\x12\r\n\x05scope\x18\x02 \x01(\t\x12*\n\x06\x65xpire\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12#\n\x06\x63laims\x18\n \x01(\x0b\x32\x13.eolymp.auth.Claims\"!\n\x10RevokeTokenInput\x12\r\n\x05token\x18\x01 \x01(\t\"\x13\n\x11RevokeTokenOutput\"\xa7\x01\n\x10RequestAuthInput\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x16\n\x0e\x63ode_challenge\x18\x02 \x01(\t\x12\x1d\n\x15\x63ode_challenge_method\x18\x03 \x01(\t\x12\x14\n\x0credirect_uri\x18\x04 \x01(\t\x12\x15\n\rresponse_type\x18\x05 \x01(\t\x12\r\n\x05scope\x18\x06 \x01(\t\x12\r\n\x05state\x18\x07 \x01(\t\"E\n\x11RequestAuthOutput\x12\x1a\n\x12\x61uthorization_code\x18\x01 \x01(\t\x12\x14\n\x0credirect_uri\x18\x02 \x01(\t\"\x0f\n\rUserInfoInput\"5\n\x0eUserInfoOutput\x12#\n\x06\x63laims\x18\n \x01(\x0b\x32\x13.eolymp.auth.Claims2\xef\x03\n\rOAuth2Service\x12[\n\nIssueToken\x12\x1c.eolymp.auth.IssueTokenInput\x1a\x1d.eolymp.auth.IssueTokenOutput\"\x10\xea\xe2\n\x0c\xf5\xe2\n\x00\x00\xf0\x41\xf8\xe2\n\xac\x02\x12j\n\x0fIntrospectToken\x12!.eolymp.auth.IntrospectTokenInput\x1a\".eolymp.auth.IntrospectTokenOutput\"\x10\xea\xe2\n\x0c\xf5\xe2\n\x00\x00\xf0\x41\xf8\xe2\n\xac\x02\x12^\n\x0bRevokeToken\x12\x1d.eolymp.auth.RevokeTokenInput\x1a\x1e.eolymp.auth.RevokeTokenOutput\"\x10\xea\xe2\n\x0c\xf5\xe2\n\x00\x00\xf0\x41\xf8\xe2\n\xac\x02\x12^\n\x0bRequestAuth\x12\x1d.eolymp.auth.RequestAuthInput\x1a\x1e.eolymp.auth.RequestAuthOutput\"\x10\xea\xe2\n\x0c\xf5\xe2\n\x00\x00\xf0\x41\xf8\xe2\n\xac\x02\x12U\n\x08UserInfo\x12\x1a.eolymp.auth.UserInfoInput\x1a\x1b.eolymp.auth.UserInfoOutput\"\x10\xea\xe2\n\x0c\xf5\xe2\n\x00\x00\xf0\x41\xf8\xe2\n\xac\x02\x42+Z)github.com/eolymp/go-sdk/eolymp/auth;authb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.auth.oauth2_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z)github.com/eolymp/go-sdk/eolymp/auth;auth'
  _globals['_OAUTH2SERVICE'].methods_by_name['IssueToken']._loaded_options = None
  _globals['_OAUTH2SERVICE'].methods_by_name['IssueToken']._serialized_options = b'\352\342\n\014\365\342\n\000\000\360A\370\342\n\254\002'
  _globals['_OAUTH2SERVICE'].methods_by_name['IntrospectToken']._loaded_options = None
  _globals['_OAUTH2SERVICE'].methods_by_name['IntrospectToken']._serialized_options = b'\352\342\n\014\365\342\n\000\000\360A\370\342\n\254\002'
  _globals['_OAUTH2SERVICE'].methods_by_name['RevokeToken']._loaded_options = None
  _globals['_OAUTH2SERVICE'].methods_by_name['RevokeToken']._serialized_options = b'\352\342\n\014\365\342\n\000\000\360A\370\342\n\254\002'
  _globals['_OAUTH2SERVICE'].methods_by_name['RequestAuth']._loaded_options = None
  _globals['_OAUTH2SERVICE'].methods_by_name['RequestAuth']._serialized_options = b'\352\342\n\014\365\342\n\000\000\360A\370\342\n\254\002'
  _globals['_OAUTH2SERVICE'].methods_by_name['UserInfo']._loaded_options = None
  _globals['_OAUTH2SERVICE'].methods_by_name['UserInfo']._serialized_options = b'\352\342\n\014\365\342\n\000\000\360A\370\342\n\254\002'
  _globals['_ISSUETOKENINPUT']._serialized_start=145
  _globals['_ISSUETOKENINPUT']._serialized_end=496
  _globals['_ISSUETOKENINPUT_GRANTTYPE']._serialized_start=399
  _globals['_ISSUETOKENINPUT_GRANTTYPE']._serialized_end=496
  _globals['_ISSUETOKENOUTPUT']._serialized_start=499
  _globals['_ISSUETOKENOUTPUT']._serialized_end=672
  _globals['_INTROSPECTTOKENINPUT']._serialized_start=674
  _globals['_INTROSPECTTOKENINPUT']._serialized_end=711
  _globals['_INTROSPECTTOKENOUTPUT']._serialized_start=714
  _globals['_INTROSPECTTOKENOUTPUT']._serialized_end=849
  _globals['_REVOKETOKENINPUT']._serialized_start=851
  _globals['_REVOKETOKENINPUT']._serialized_end=884
  _globals['_REVOKETOKENOUTPUT']._serialized_start=886
  _globals['_REVOKETOKENOUTPUT']._serialized_end=905
  _globals['_REQUESTAUTHINPUT']._serialized_start=908
  _globals['_REQUESTAUTHINPUT']._serialized_end=1075
  _globals['_REQUESTAUTHOUTPUT']._serialized_start=1077
  _globals['_REQUESTAUTHOUTPUT']._serialized_end=1146
  _globals['_USERINFOINPUT']._serialized_start=1148
  _globals['_USERINFOINPUT']._serialized_end=1163
  _globals['_USERINFOOUTPUT']._serialized_start=1165
  _globals['_USERINFOOUTPUT']._serialized_end=1218
  _globals['_OAUTH2SERVICE']._serialized_start=1221
  _globals['_OAUTH2SERVICE']._serialized_end=1716
# @@protoc_insertion_point(module_scope)
