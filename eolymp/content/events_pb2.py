# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/content/events.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.content import fragment_pb2 as eolymp_dot_content_dot_fragment__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x65olymp/content/events.proto\x12\x0e\x65olymp.content\x1a\x1d\x65olymp/content/fragment.proto\"i\n\x14\x46ragmentChangedEvent\x12(\n\x06\x62\x65\x66ore\x18\x01 \x01(\x0b\x32\x18.eolymp.content.Fragment\x12\'\n\x05\x61\x66ter\x18\x02 \x01(\x0b\x32\x18.eolymp.content.FragmentB1Z/github.com/eolymp/go-sdk/eolymp/content;contentb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.content.events_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/eolymp/go-sdk/eolymp/content;content'
  _FRAGMENTCHANGEDEVENT._serialized_start=78
  _FRAGMENTCHANGEDEVENT._serialized_end=183
# @@protoc_insertion_point(module_scope)