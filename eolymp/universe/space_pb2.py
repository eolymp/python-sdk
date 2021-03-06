# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/universe/space.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import resource_pb2 as eolymp_dot_annotations_dot_resource__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x65olymp/universe/space.proto\x12\x0f\x65olymp.universe\x1a!eolymp/annotations/resource.proto\"\x8f\x06\n\x05Space\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\n \x01(\t\x12\r\n\x05image\x18\x0b \x01(\t\x12)\n\x04type\x18\x0c \x01(\x0e\x32\x1b.eolymp.universe.Space.Type\x12\x0c\n\x04plan\x18\r \x01(\t\x12\x35\n\nvisibility\x18\x0e \x01(\x0e\x32!.eolymp.universe.Space.Visibility\x12\x35\n\nmembership\x18\x14 \x01(\x0e\x32!.eolymp.universe.Space.Membership\x12\x15\n\rmin_team_size\x18\x15 \x01(\r\x12\x15\n\rmax_team_size\x18\x16 \x01(\r\x1a\x99\x02\n\x05Quota\x12\x1a\n\x12problems_per_space\x18\x01 \x01(\r\x12\x19\n\x11members_per_space\x18\x02 \x01(\r\x12\x1a\n\x12\x63ontests_per_space\x18\x03 \x01(\r\x12!\n\x19\x61\x63tive_contests_per_space\x18\x04 \x01(\r\x12\x1d\n\x15scoreboards_per_space\x18\x05 \x01(\r\x12\x1d\n\x15permissions_per_space\x18\x06 \x01(\r\x12\x1c\n\x14\x61ttributes_per_space\x18\x07 \x01(\r\x12\x1c\n\x14problems_per_contest\x18\n \x01(\r\x12 \n\x18participants_per_contest\x18\x0b \x01(\r\"Q\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\t\n\x05OTHER\x10\x01\x12\r\n\tCLASSROOM\x10\x02\x12\x0c\n\x08TEAMROOM\x10\x03\x12\x0f\n\x0b\x43OMPETITION\x10\x04\">\n\nMembership\x12\x16\n\x12UNKNOWN_MEMBERSHIP\x10\x00\x12\x0e\n\nINDIVIDUAL\x10\x01\x12\x08\n\x04TEAM\x10\x02\"=\n\nVisibility\x12\x16\n\x12UNKNOWN_VISIBILITY\x10\x00\x12\n\n\x06PUBLIC\x10\x01\x12\x0b\n\x07PRIVATE\x10\x02:\r\xb2\xe3\n\t\xba\xe3\n\x05spaceB3Z1github.com/eolymp/go-sdk/eolymp/universe;universeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.universe.space_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/eolymp/go-sdk/eolymp/universe;universe'
  _SPACE._options = None
  _SPACE._serialized_options = b'\262\343\n\t\272\343\n\005space'
  _SPACE._serialized_start=84
  _SPACE._serialized_end=867
  _SPACE_QUOTA._serialized_start=361
  _SPACE_QUOTA._serialized_end=642
  _SPACE_TYPE._serialized_start=644
  _SPACE_TYPE._serialized_end=725
  _SPACE_MEMBERSHIP._serialized_start=727
  _SPACE_MEMBERSHIP._serialized_end=789
  _SPACE_VISIBILITY._serialized_start=791
  _SPACE_VISIBILITY._serialized_end=852
# @@protoc_insertion_point(module_scope)
