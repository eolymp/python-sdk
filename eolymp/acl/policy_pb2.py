# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/acl/policy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.acl import action_pb2 as eolymp_dot_acl_dot_action__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x65olymp/acl/policy.proto\x12\neolymp.acl\x1a\x17\x65olymp/acl/action.proto\"~\n\x06Policy\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tprincipal\x18\x03 \x01(\t\x12\x10\n\x08resource\x18\n \x01(\t\x12\x11\n\tallow_all\x18\x0c \x01(\x08\x12\"\n\x06\x61llows\x18\x0b \x03(\x0e\x32\x12.eolymp.acl.ActionB)Z\'github.com/eolymp/go-sdk/eolymp/acl;aclb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.acl.policy_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\'github.com/eolymp/go-sdk/eolymp/acl;acl'
  _POLICY._serialized_start=64
  _POLICY._serialized_end=190
# @@protoc_insertion_point(module_scope)