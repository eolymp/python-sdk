# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/community/achievement_service.proto
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
    'eolymp/community/achievement_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.annotations import scope_pb2 as eolymp_dot_annotations_dot_scope__pb2
from eolymp.community import achievement_pb2 as eolymp_dot_community_dot_achievement__pb2
from eolymp.wellknown import expression_pb2 as eolymp_dot_wellknown_dot_expression__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*eolymp/community/achievement_service.proto\x12\x10\x65olymp.community\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a\"eolymp/community/achievement.proto\x1a!eolymp/wellknown/expression.proto\"`\n\x16\x41ssignAchievementInput\x12\x16\n\x0e\x61\x63hievement_id\x18\x02 \x01(\t\x12\x10\n\x06set_to\x18\x03 \x01(\x05H\x00\x12\x10\n\x06inc_by\x18\x04 \x01(\x05H\x00\x42\n\n\x08quantity\"+\n\x17\x41ssignAchievementOutput\x12\x10\n\x08quantity\x18\x03 \x01(\x05\"2\n\x18UnassignAchievementInput\x12\x16\n\x0e\x61\x63hievement_id\x18\x02 \x01(\t\"\x1b\n\x19UnassignAchievementOutput\"\x8f\x02\n\x15ListAchievementsInput\x12\x0e\n\x06locale\x18\x01 \x01(\t\x12\r\n\x05\x61\x66ter\x18\x0c \x01(\t\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12\x0e\n\x06offset\x18\n \x01(\x05\x12?\n\x07\x66ilters\x18( \x01(\x0b\x32..eolymp.community.ListAchievementsInput.Filter\x12\x33\n\x05\x65xtra\x18\xe3\x08 \x03(\x0e\x32#.eolymp.community.Achievement.Extra\x1a\x43\n\x06\x46ilter\x12\r\n\x05query\x18\x01 \x01(\t\x12*\n\x02id\x18\x02 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\"o\n\x16ListAchievementsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x18\n\x10next_page_cursor\x18\x03 \x01(\t\x12,\n\x05items\x18\x02 \x03(\x0b\x32\x1d.eolymp.community.Achievement2\xc5\x04\n\x12\x41\x63hievementService\x12\xbd\x01\n\x11\x41ssignAchievement\x12(.eolymp.community.AssignAchievementInput\x1a).eolymp.community.AssignAchievementOutput\"S\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\x82\xd3\xe4\x93\x02 \x1a\x1e/achievements/{achievement_id}\x12\xc3\x01\n\x13UnassignAchievement\x12*.eolymp.community.UnassignAchievementInput\x1a+.eolymp.community.UnassignAchievementOutput\"S\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\x82\xd3\xe4\x93\x02 *\x1e/achievements/{achievement_id}\x12\xa8\x01\n\x10ListAchievements\x12\'.eolymp.community.ListAchievementsInput\x1a(.eolymp.community.ListAchievementsOutput\"A\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xe3\n\x19\x8a\xe3\n\x15\x63ommunity:member:read\x82\xd3\xe4\x93\x02\x0f\x12\r/achievementsB5Z3github.com/eolymp/go-sdk/eolymp/community;communityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.community.achievement_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/eolymp/go-sdk/eolymp/community;community'
  _globals['_ACHIEVEMENTSERVICE'].methods_by_name['AssignAchievement']._loaded_options = None
  _globals['_ACHIEVEMENTSERVICE'].methods_by_name['AssignAchievement']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\343\n\032\212\343\n\026community:member:write\202\323\344\223\002 \032\036/achievements/{achievement_id}'
  _globals['_ACHIEVEMENTSERVICE'].methods_by_name['UnassignAchievement']._loaded_options = None
  _globals['_ACHIEVEMENTSERVICE'].methods_by_name['UnassignAchievement']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\343\n\032\212\343\n\026community:member:write\202\323\344\223\002 *\036/achievements/{achievement_id}'
  _globals['_ACHIEVEMENTSERVICE'].methods_by_name['ListAchievements']._loaded_options = None
  _globals['_ACHIEVEMENTSERVICE'].methods_by_name['ListAchievements']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\343\n\031\212\343\n\025community:member:read\202\323\344\223\002\017\022\r/achievements'
  _globals['_ASSIGNACHIEVEMENTINPUT']._serialized_start=234
  _globals['_ASSIGNACHIEVEMENTINPUT']._serialized_end=330
  _globals['_ASSIGNACHIEVEMENTOUTPUT']._serialized_start=332
  _globals['_ASSIGNACHIEVEMENTOUTPUT']._serialized_end=375
  _globals['_UNASSIGNACHIEVEMENTINPUT']._serialized_start=377
  _globals['_UNASSIGNACHIEVEMENTINPUT']._serialized_end=427
  _globals['_UNASSIGNACHIEVEMENTOUTPUT']._serialized_start=429
  _globals['_UNASSIGNACHIEVEMENTOUTPUT']._serialized_end=456
  _globals['_LISTACHIEVEMENTSINPUT']._serialized_start=459
  _globals['_LISTACHIEVEMENTSINPUT']._serialized_end=730
  _globals['_LISTACHIEVEMENTSINPUT_FILTER']._serialized_start=663
  _globals['_LISTACHIEVEMENTSINPUT_FILTER']._serialized_end=730
  _globals['_LISTACHIEVEMENTSOUTPUT']._serialized_start=732
  _globals['_LISTACHIEVEMENTSOUTPUT']._serialized_end=843
  _globals['_ACHIEVEMENTSERVICE']._serialized_start=846
  _globals['_ACHIEVEMENTSERVICE']._serialized_end=1427
# @@protoc_insertion_point(module_scope)
