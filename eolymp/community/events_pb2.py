# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/community/events.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.community import member_pb2 as eolymp_dot_community_dot_member__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x65olymp/community/events.proto\x12\x10\x65olymp.community\x1a\x1d\x65olymp/community/member.proto\">\n\x12MemberCreatedEvent\x12(\n\x06member\x18\x01 \x01(\x0b\x32\x18.eolymp.community.Member\">\n\x12MemberUpdatedEvent\x12(\n\x06member\x18\x01 \x01(\x0b\x32\x18.eolymp.community.Member\">\n\x12MemberDeletedEvent\x12(\n\x06member\x18\x01 \x01(\x0b\x32\x18.eolymp.community.MemberB5Z3github.com/eolymp/go-sdk/eolymp/community;communityb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.community.events_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z3github.com/eolymp/go-sdk/eolymp/community;community'
  _MEMBERCREATEDEVENT._serialized_start=82
  _MEMBERCREATEDEVENT._serialized_end=144
  _MEMBERUPDATEDEVENT._serialized_start=146
  _MEMBERUPDATEDEVENT._serialized_end=208
  _MEMBERDELETEDEVENT._serialized_start=210
  _MEMBERDELETEDEVENT._serialized_end=272
# @@protoc_insertion_point(module_scope)