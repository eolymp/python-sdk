# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/community/penalty_service.proto
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
    'eolymp/community/penalty_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.annotations import scope_pb2 as eolymp_dot_annotations_dot_scope__pb2
from eolymp.community import penalty_pb2 as eolymp_dot_community_dot_penalty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&eolymp/community/penalty_service.proto\x12\x10\x65olymp.community\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a\x1e\x65olymp/community/penalty.proto\"U\n\x12\x43reatePenaltyInput\x12*\n\x07penalty\x18\x01 \x01(\x0b\x32\x19.eolymp.community.Penalty\x12\x13\n\x0b\x64ont_notify\x18\x02 \x01(\x08\")\n\x13\x43reatePenaltyOutput\x12\x12\n\npenalty_id\x18\x01 \x01(\t\"\xda\x01\n\x12UpdatePenaltyInput\x12\x39\n\x05patch\x18\x03 \x03(\x0e\x32*.eolymp.community.UpdatePenaltyInput.Patch\x12\x12\n\npenalty_id\x18\x01 \x01(\t\x12*\n\x07penalty\x18\x02 \x01(\x0b\x32\x19.eolymp.community.Penalty\"I\n\x05Patch\x12\x07\n\x03\x41LL\x10\x00\x12\x0b\n\x07SUMMARY\x10\x01\x12\x0f\n\x0b\x44\x45SCRIPTION\x10\x02\x12\t\n\x05SCOPE\x10\x03\x12\x0e\n\nEXPIRES_AT\x10\x04\"\x15\n\x13UpdatePenaltyOutput\"(\n\x12\x44\x65letePenaltyInput\x12\x12\n\npenalty_id\x18\x01 \x01(\t\"\x15\n\x13\x44\x65letePenaltyOutput\"[\n\x14\x44\x65scribePenaltyInput\x12\x12\n\npenalty_id\x18\x01 \x01(\t\x12/\n\x05\x65xtra\x18\xe3\x08 \x03(\x0e\x32\x1f.eolymp.community.Penalty.Extra\"C\n\x15\x44\x65scribePenaltyOutput\x12*\n\x07penalty\x18\x01 \x01(\x0b\x32\x19.eolymp.community.Penalty\"c\n\x12ListPenaltiesInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12/\n\x05\x65xtra\x18\xe3\x08 \x03(\x0e\x32\x1f.eolymp.community.Penalty.Extra\"N\n\x13ListPenaltiesOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12(\n\x05items\x18\x02 \x03(\x0b\x32\x19.eolymp.community.Penalty2\xdb\x06\n\x0ePenaltyService\x12\x9d\x01\n\rCreatePenalty\x12$.eolymp.community.CreatePenaltyInput\x1a%.eolymp.community.CreatePenaltyOutput\"?\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\nd\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\x82\xd3\xe4\x93\x02\x0c\"\n/penalties\x12\xaa\x01\n\rUpdatePenalty\x12$.eolymp.community.UpdatePenaltyInput\x1a%.eolymp.community.UpdatePenaltyOutput\"L\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\x82\xd3\xe4\x93\x02\x19\"\x17/penalties/{penalty_id}\x12\xaa\x01\n\rDeletePenalty\x12$.eolymp.community.DeletePenaltyInput\x1a%.eolymp.community.DeletePenaltyOutput\"L\xea\xe2\n\x0b\xf5\xe2\n\x00\x00 A\xf8\xe2\nd\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\x82\xd3\xe4\x93\x02\x19*\x17/penalties/{penalty_id}\x12\xaf\x01\n\x0f\x44\x65scribePenalty\x12&.eolymp.community.DescribePenaltyInput\x1a\'.eolymp.community.DescribePenaltyOutput\"K\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xe3\n\x19\x8a\xe3\n\x15\x63ommunity:member:read\x82\xd3\xe4\x93\x02\x19\x12\x17/penalties/{penalty_id}\x12\x9c\x01\n\rListPenalties\x12$.eolymp.community.ListPenaltiesInput\x1a%.eolymp.community.ListPenaltiesOutput\">\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xe3\n\x19\x8a\xe3\n\x15\x63ommunity:member:read\x82\xd3\xe4\x93\x02\x0c\x12\n/penaltiesB5Z3github.com/eolymp/go-sdk/eolymp/community;communityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.community.penalty_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/eolymp/go-sdk/eolymp/community;community'
  _globals['_PENALTYSERVICE'].methods_by_name['CreatePenalty']._loaded_options = None
  _globals['_PENALTYSERVICE'].methods_by_name['CreatePenalty']._serialized_options = b'\352\342\n\013\365\342\n\000\000 A\370\342\nd\202\343\n\032\212\343\n\026community:member:write\202\323\344\223\002\014\"\n/penalties'
  _globals['_PENALTYSERVICE'].methods_by_name['UpdatePenalty']._loaded_options = None
  _globals['_PENALTYSERVICE'].methods_by_name['UpdatePenalty']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\343\n\032\212\343\n\026community:member:write\202\323\344\223\002\031\"\027/penalties/{penalty_id}'
  _globals['_PENALTYSERVICE'].methods_by_name['DeletePenalty']._loaded_options = None
  _globals['_PENALTYSERVICE'].methods_by_name['DeletePenalty']._serialized_options = b'\352\342\n\013\365\342\n\000\000 A\370\342\nd\202\343\n\032\212\343\n\026community:member:write\202\323\344\223\002\031*\027/penalties/{penalty_id}'
  _globals['_PENALTYSERVICE'].methods_by_name['DescribePenalty']._loaded_options = None
  _globals['_PENALTYSERVICE'].methods_by_name['DescribePenalty']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\343\n\031\212\343\n\025community:member:read\202\323\344\223\002\031\022\027/penalties/{penalty_id}'
  _globals['_PENALTYSERVICE'].methods_by_name['ListPenalties']._loaded_options = None
  _globals['_PENALTYSERVICE'].methods_by_name['ListPenalties']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\343\n\031\212\343\n\025community:member:read\202\323\344\223\002\014\022\n/penalties'
  _globals['_CREATEPENALTYINPUT']._serialized_start=191
  _globals['_CREATEPENALTYINPUT']._serialized_end=276
  _globals['_CREATEPENALTYOUTPUT']._serialized_start=278
  _globals['_CREATEPENALTYOUTPUT']._serialized_end=319
  _globals['_UPDATEPENALTYINPUT']._serialized_start=322
  _globals['_UPDATEPENALTYINPUT']._serialized_end=540
  _globals['_UPDATEPENALTYINPUT_PATCH']._serialized_start=467
  _globals['_UPDATEPENALTYINPUT_PATCH']._serialized_end=540
  _globals['_UPDATEPENALTYOUTPUT']._serialized_start=542
  _globals['_UPDATEPENALTYOUTPUT']._serialized_end=563
  _globals['_DELETEPENALTYINPUT']._serialized_start=565
  _globals['_DELETEPENALTYINPUT']._serialized_end=605
  _globals['_DELETEPENALTYOUTPUT']._serialized_start=607
  _globals['_DELETEPENALTYOUTPUT']._serialized_end=628
  _globals['_DESCRIBEPENALTYINPUT']._serialized_start=630
  _globals['_DESCRIBEPENALTYINPUT']._serialized_end=721
  _globals['_DESCRIBEPENALTYOUTPUT']._serialized_start=723
  _globals['_DESCRIBEPENALTYOUTPUT']._serialized_end=790
  _globals['_LISTPENALTIESINPUT']._serialized_start=792
  _globals['_LISTPENALTIESINPUT']._serialized_end=891
  _globals['_LISTPENALTIESOUTPUT']._serialized_start=893
  _globals['_LISTPENALTIESOUTPUT']._serialized_end=971
  _globals['_PENALTYSERVICE']._serialized_start=974
  _globals['_PENALTYSERVICE']._serialized_end=1833
# @@protoc_insertion_point(module_scope)
