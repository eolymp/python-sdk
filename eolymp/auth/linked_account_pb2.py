# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/auth/linked_account.proto
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
    'eolymp/auth/linked_account.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n eolymp/auth/linked_account.proto\x12\x0b\x65olymp.auth\"\xbc\x01\n\rLinkedAccount\x12\n\n\x02id\x18\x01 \x01(\t\x12-\n\x04type\x18\x02 \x01(\x0e\x32\x1f.eolymp.auth.LinkedAccount.Type\x12\x0e\n\x06issuer\x18\x03 \x01(\t\x12\x0f\n\x07subject\x18\x04 \x01(\t\x12\x10\n\x08nickname\x18\x05 \x01(\t\"=\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\n\n\x06GOOGLE\x10\x01\x12\n\n\x06GITHUB\x10\x02\x12\x0b\n\x07\x44ISCORD\x10\x03\x42+Z)github.com/eolymp/go-sdk/eolymp/auth;authb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.auth.linked_account_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z)github.com/eolymp/go-sdk/eolymp/auth;auth'
  _globals['_LINKEDACCOUNT']._serialized_start=50
  _globals['_LINKEDACCOUNT']._serialized_end=238
  _globals['_LINKEDACCOUNT_TYPE']._serialized_start=177
  _globals['_LINKEDACCOUNT_TYPE']._serialized_end=238
# @@protoc_insertion_point(module_scope)
