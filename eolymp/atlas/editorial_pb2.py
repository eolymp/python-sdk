# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/atlas/editorial.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.ecm import content_pb2 as eolymp_dot_ecm_dot_content__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x65olymp/atlas/editorial.proto\x12\x0c\x65olymp.atlas\x1a\x18\x65olymp/ecm/content.proto\"d\n\tEditorial\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06locale\x18\x03 \x01(\t\x12$\n\x07\x63ontent\x18\x06 \x01(\x0b\x32\x13.eolymp.ecm.Content\x12\x15\n\rdownload_link\x18\x07 \x01(\tB-Z+github.com/eolymp/go-sdk/eolymp/atlas;atlasb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.atlas.editorial_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/eolymp/go-sdk/eolymp/atlas;atlas'
  _EDITORIAL._serialized_start=72
  _EDITORIAL._serialized_end=172
# @@protoc_insertion_point(module_scope)
