# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/community/rating_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.annotations import scope_pb2 as eolymp_dot_annotations_dot_scope__pb2
from eolymp.community import rating_point_pb2 as eolymp_dot_community_dot_rating__point__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%eolymp/community/rating_service.proto\x12\x10\x65olymp.community\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a#eolymp/community/rating_point.proto\"R\n\x0eSetRatingInput\x12\x11\n\trating_id\x18\x01 \x01(\t\x12-\n\x06rating\x18\x02 \x01(\x0b\x32\x1d.eolymp.community.RatingPoint\"$\n\x0fSetRatingOutput\x12\x11\n\trating_id\x18\x01 \x01(\t\"T\n\x11\x44\x65leteRatingInput\x12\x11\n\trating_id\x18\x02 \x01(\t\x12,\n\x05point\x18\x03 \x01(\x0b\x32\x1d.eolymp.community.RatingPoint\"\x14\n\x12\x44\x65leteRatingOutput2\xc6\x02\n\rRatingService\x12\x8e\x01\n\tSetRating\x12 .eolymp.community.SetRatingInput\x1a!.eolymp.community.SetRatingOutput\"<\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\nd\x82\xd3\xe4\x93\x02\t\"\x07/rating\x12\xa3\x01\n\x0c\x44\x65leteRating\x12#.eolymp.community.DeleteRatingInput\x1a$.eolymp.community.DeleteRatingOutput\"H\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x15*\x13/rating/{rating_id}B5Z3github.com/eolymp/go-sdk/eolymp/community;communityb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.community.rating_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z3github.com/eolymp/go-sdk/eolymp/community;community'
  _RATINGSERVICE.methods_by_name['SetRating']._options = None
  _RATINGSERVICE.methods_by_name['SetRating']._serialized_options = b'\202\343\n\032\212\343\n\026community:member:write\352\342\n\013\365\342\n\000\000 A\370\342\nd\202\323\344\223\002\t\"\007/rating'
  _RATINGSERVICE.methods_by_name['DeleteRating']._options = None
  _RATINGSERVICE.methods_by_name['DeleteRating']._serialized_options = b'\202\343\n\032\212\343\n\026community:member:write\352\342\n\013\365\342\n\000\000 A\370\342\nd\202\323\344\223\002\025*\023/rating/{rating_id}'
  _SETRATINGINPUT._serialized_start=195
  _SETRATINGINPUT._serialized_end=277
  _SETRATINGOUTPUT._serialized_start=279
  _SETRATINGOUTPUT._serialized_end=315
  _DELETERATINGINPUT._serialized_start=317
  _DELETERATINGINPUT._serialized_end=401
  _DELETERATINGOUTPUT._serialized_start=403
  _DELETERATINGOUTPUT._serialized_end=423
  _RATINGSERVICE._serialized_start=426
  _RATINGSERVICE._serialized_end=752
# @@protoc_insertion_point(module_scope)