# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/discussion/post_type.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!eolymp/discussion/post_type.proto\x12\x11\x65olymp.discussion\"\xcd\x01\n\x08PostType\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06hidden\x18\x03 \x01(\x08\x12\r\n\x05order\x18\n \x01(\x05\x12\x35\n\x08variants\x18\x64 \x03(\x0b\x32#.eolymp.discussion.PostType.Variant\x1a\'\n\x07Variant\x12\x0e\n\x06locale\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"(\n\x05\x45xtra\x12\x11\n\rUNKNOWN_EXTRA\x10\x00\x12\x0c\n\x08VARIANTS\x10\x01\x42\x37Z5github.com/eolymp/go-sdk/eolymp/discussion;discussionb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.discussion.post_type_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z5github.com/eolymp/go-sdk/eolymp/discussion;discussion'
  _POSTTYPE._serialized_start=57
  _POSTTYPE._serialized_end=262
  _POSTTYPE_VARIANT._serialized_start=181
  _POSTTYPE_VARIANT._serialized_end=220
  _POSTTYPE_EXTRA._serialized_start=222
  _POSTTYPE_EXTRA._serialized_end=262
# @@protoc_insertion_point(module_scope)