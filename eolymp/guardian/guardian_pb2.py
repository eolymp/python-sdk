# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/guardian/guardian.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.guardian import policy_pb2 as eolymp_dot_guardian_dot_policy__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x65olymp/guardian/guardian.proto\x12\x0f\x65olymp.universe\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1c\x65olymp/guardian/policy.proto\"\x13\n\x11ListPoliciesInput\"K\n\x12ListPoliciesOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12&\n\x05items\x18\x02 \x03(\x0b\x32\x17.eolymp.universe.Policy\"#\n\x13\x44\x65scribePolicyInput\x12\x0c\n\x04name\x18\x01 \x01(\t\"?\n\x14\x44\x65scribePolicyOutput\x12\'\n\x06policy\x18\x01 \x01(\x0b\x32\x17.eolymp.universe.Policy\"J\n\x11\x44\x65\x66inePolicyInput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\'\n\x06policy\x18\x02 \x01(\x0b\x32\x17.eolymp.universe.Policy\"\x14\n\x12\x44\x65\x66inePolicyOutput\"!\n\x11RemovePolicyInput\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x14\n\x12RemovePolicyOutput2\x94\x04\n\x08Guardian\x12y\n\x0cListPolicies\x12\".eolymp.universe.ListPoliciesInput\x1a#.eolymp.universe.ListPoliciesOutput\" \xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x0b\x12\t/policies\x12\x86\x01\n\x0e\x44\x65scribePolicy\x12$.eolymp.universe.DescribePolicyInput\x1a%.eolymp.universe.DescribePolicyOutput\"\'\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x12\x12\x10/policies/{name}\x12\x80\x01\n\x0c\x44\x65\x66inePolicy\x12\".eolymp.universe.DefinePolicyInput\x1a#.eolymp.universe.DefinePolicyOutput\"\'\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x12\x1a\x10/policies/{name}\x12\x80\x01\n\x0cRemovePolicy\x12\".eolymp.universe.RemovePolicyInput\x1a#.eolymp.universe.RemovePolicyOutput\"\'\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x12*\x10/policies/{name}B3Z1github.com/eolymp/go-sdk/eolymp/guardian;guardianb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.guardian.guardian_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/eolymp/go-sdk/eolymp/guardian;guardian'
  _GUARDIAN.methods_by_name['ListPolicies']._options = None
  _GUARDIAN.methods_by_name['ListPolicies']._serialized_options = b'\352\342\n\013\365\342\n\000\000 A\370\342\nd\202\323\344\223\002\013\022\t/policies'
  _GUARDIAN.methods_by_name['DescribePolicy']._options = None
  _GUARDIAN.methods_by_name['DescribePolicy']._serialized_options = b'\352\342\n\013\365\342\n\000\000 A\370\342\nd\202\323\344\223\002\022\022\020/policies/{name}'
  _GUARDIAN.methods_by_name['DefinePolicy']._options = None
  _GUARDIAN.methods_by_name['DefinePolicy']._serialized_options = b'\352\342\n\013\365\342\n\000\000 A\370\342\nd\202\323\344\223\002\022\032\020/policies/{name}'
  _GUARDIAN.methods_by_name['RemovePolicy']._options = None
  _GUARDIAN.methods_by_name['RemovePolicy']._serialized_options = b'\352\342\n\013\365\342\n\000\000 A\370\342\nd\202\323\344\223\002\022*\020/policies/{name}'
  _LISTPOLICIESINPUT._serialized_start=148
  _LISTPOLICIESINPUT._serialized_end=167
  _LISTPOLICIESOUTPUT._serialized_start=169
  _LISTPOLICIESOUTPUT._serialized_end=244
  _DESCRIBEPOLICYINPUT._serialized_start=246
  _DESCRIBEPOLICYINPUT._serialized_end=281
  _DESCRIBEPOLICYOUTPUT._serialized_start=283
  _DESCRIBEPOLICYOUTPUT._serialized_end=346
  _DEFINEPOLICYINPUT._serialized_start=348
  _DEFINEPOLICYINPUT._serialized_end=422
  _DEFINEPOLICYOUTPUT._serialized_start=424
  _DEFINEPOLICYOUTPUT._serialized_end=444
  _REMOVEPOLICYINPUT._serialized_start=446
  _REMOVEPOLICYINPUT._serialized_end=479
  _REMOVEPOLICYOUTPUT._serialized_start=481
  _REMOVEPOLICYOUTPUT._serialized_end=501
  _GUARDIAN._serialized_start=504
  _GUARDIAN._serialized_end=1036
# @@protoc_insertion_point(module_scope)