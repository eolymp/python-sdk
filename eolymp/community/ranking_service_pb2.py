# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/community/ranking_service.proto
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
from eolymp.community import ranking_event_pb2 as eolymp_dot_community_dot_ranking__event__pb2
from eolymp.community import ranking_point_pb2 as eolymp_dot_community_dot_ranking__point__pb2
from eolymp.wellknown import direction_pb2 as eolymp_dot_wellknown_dot_direction__pb2
from eolymp.wellknown import expression_pb2 as eolymp_dot_wellknown_dot_expression__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&eolymp/community/ranking_service.proto\x12\x10\x65olymp.community\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a$eolymp/community/ranking_event.proto\x1a$eolymp/community/ranking_point.proto\x1a eolymp/wellknown/direction.proto\x1a!eolymp/wellknown/expression.proto\"H\n\x17\x43reateRankingEventInput\x12-\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1e.eolymp.community.RankingEvent\",\n\x18\x43reateRankingEventOutput\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\"\xd5\x01\n\x17UpdateRankingEventInput\x12>\n\x05patch\x18\x01 \x03(\x0e\x32/.eolymp.community.UpdateRankingEventInput.Patch\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\t\x12-\n\x05\x65vent\x18\x03 \x01(\x0b\x32\x1e.eolymp.community.RankingEvent\"9\n\x05Patch\x12\x07\n\x03\x41LL\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\r\n\tTIMESTAMP\x10\x02\x12\x0e\n\nCONTEST_ID\x10\x03\"\x1a\n\x18UpdateRankingEventOutput\"+\n\x17\x44\x65leteRankingEventInput\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\"\x1a\n\x18\x44\x65leteRankingEventOutput\"-\n\x19\x44\x65scribeRankingEventInput\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\t\"K\n\x1a\x44\x65scribeRankingEventOutput\x12-\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1e.eolymp.community.RankingEvent\"\xe1\x03\n\x16ListRankingEventsInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12@\n\x07\x66ilters\x18( \x01(\x0b\x32/.eolymp.community.ListRankingEventsInput.Filter\x12?\n\x04sort\x18\x32 \x01(\x0e\x32\x31.eolymp.community.ListRankingEventsInput.Sortable\x12*\n\x05order\x18\x33 \x01(\x0e\x32\x1b.eolymp.wellknown.Direction\x1a\xd4\x01\n\x06\x46ilter\x12*\n\x02id\x18\x01 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x30\n\x04name\x18\x02 \x03(\x0b\x32\".eolymp.wellknown.ExpressionString\x12\x38\n\ttimestamp\x18\x03 \x03(\x0b\x32%.eolymp.wellknown.ExpressionTimestamp\x12\x32\n\ncontest_id\x18\x64 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\"#\n\x08Sortable\x12\r\n\tTIMESTAMP\x10\x00\x12\x08\n\x04NAME\x10\x01\"W\n\x17ListRankingEventsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12-\n\x05items\x18\x02 \x03(\x0b\x32\x1e.eolymp.community.RankingEvent\"m\n\x17UpdateRankingPointInput\x12\x11\n\tmember_id\x18\x01 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\t\x12-\n\x05point\x18\n \x01(\x0b\x32\x1e.eolymp.community.RankingPoint\"\x1a\n\x18UpdateRankingPointOutput\"m\n\x17\x44\x65leteRankingPointInput\x12\x11\n\tmember_id\x18\x01 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\t\x12-\n\x05point\x18\n \x01(\x0b\x32\x1e.eolymp.community.RankingPoint\"\x1a\n\x18\x44\x65leteRankingPointOutput\"@\n\x19\x44\x65scribeRankingPointInput\x12\x11\n\tmember_id\x18\x01 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\t\"K\n\x1a\x44\x65scribeRankingPointOutput\x12-\n\x05point\x18\x01 \x01(\x0b\x32\x1e.eolymp.community.RankingPoint\"\xfb\x02\n\x16ListRankingPointsInput\x12\x11\n\tmember_id\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12@\n\x07\x66ilters\x18( \x01(\x0b\x32/.eolymp.community.ListRankingPointsInput.Filter\x12?\n\x04sort\x18\x32 \x01(\x0e\x32\x31.eolymp.community.ListRankingPointsInput.Sortable\x12*\n\x05order\x18\x33 \x01(\x0e\x32\x1b.eolymp.wellknown.Direction\x1a\x66\n\x06\x46ilter\x12*\n\x02id\x18\x01 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x30\n\x08\x65vent_id\x18\x02 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\"\x19\n\x08Sortable\x12\r\n\tTIMESTAMP\x10\x00\"W\n\x17ListRankingPointsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12-\n\x05items\x18\x02 \x03(\x0b\x32\x1e.eolymp.community.RankingPoint2\xef\r\n\x0eRankingService\x12\xb1\x01\n\x12\x43reateRankingEvent\x12).eolymp.community.CreateRankingEventInput\x1a*.eolymp.community.CreateRankingEventOutput\"D\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x11\"\x0f/ranking-events\x12\xbc\x01\n\x12UpdateRankingEvent\x12).eolymp.community.UpdateRankingEventInput\x1a*.eolymp.community.UpdateRankingEventOutput\"O\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x1c\"\x1a/ranking-events/{event_id}\x12\xbc\x01\n\x12\x44\x65leteRankingEvent\x12).eolymp.community.DeleteRankingEventInput\x1a*.eolymp.community.DeleteRankingEventOutput\"O\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x1c*\x1a/ranking-events/{event_id}\x12\xc1\x01\n\x14\x44\x65scribeRankingEvent\x12+.eolymp.community.DescribeRankingEventInput\x1a,.eolymp.community.DescribeRankingEventOutput\"N\x82\xe3\n\x19\x8a\xe3\n\x15\x63ommunity:member:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x1c\x12\x1a/ranking-events/{event_id}\x12\xad\x01\n\x11ListRankingEvents\x12(.eolymp.community.ListRankingEventsInput\x1a).eolymp.community.ListRankingEventsOutput\"C\x82\xe3\n\x19\x8a\xe3\n\x15\x63ommunity:member:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x11\x12\x0f/ranking-events\x12\xcf\x01\n\x12UpdateRankingPoint\x12).eolymp.community.UpdateRankingPointInput\x1a*.eolymp.community.UpdateRankingPointOutput\"b\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02/\x1a-/ranking-series/{member_id}/points/{event_id}\x12\xcf\x01\n\x12\x44\x65leteRankingPoint\x12).eolymp.community.DeleteRankingPointInput\x1a*.eolymp.community.DeleteRankingPointOutput\"b\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02/*-/ranking-series/{member_id}/points/{event_id}\x12\xd5\x01\n\x14\x44\x65scribeRankingPoint\x12+.eolymp.community.DescribeRankingPointInput\x1a,.eolymp.community.DescribeRankingPointOutput\"b\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02/\x12-/ranking-series/{member_id}/points/{event_id}\x12\xba\x01\n\x11ListRankingPoints\x12(.eolymp.community.ListRankingPointsInput\x1a).eolymp.community.ListRankingPointsOutput\"P\x82\xe3\n\x1a\x8a\xe3\n\x16\x63ommunity:member:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x1d\x12\x1b/ranking-series/{member_id}B5Z3github.com/eolymp/go-sdk/eolymp/community;communityb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.community.ranking_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z3github.com/eolymp/go-sdk/eolymp/community;community'
  _RANKINGSERVICE.methods_by_name['CreateRankingEvent']._options = None
  _RANKINGSERVICE.methods_by_name['CreateRankingEvent']._serialized_options = b'\202\343\n\032\212\343\n\026community:member:write\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\021\"\017/ranking-events'
  _RANKINGSERVICE.methods_by_name['UpdateRankingEvent']._options = None
  _RANKINGSERVICE.methods_by_name['UpdateRankingEvent']._serialized_options = b'\202\343\n\032\212\343\n\026community:member:write\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\034\"\032/ranking-events/{event_id}'
  _RANKINGSERVICE.methods_by_name['DeleteRankingEvent']._options = None
  _RANKINGSERVICE.methods_by_name['DeleteRankingEvent']._serialized_options = b'\202\343\n\032\212\343\n\026community:member:write\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\034*\032/ranking-events/{event_id}'
  _RANKINGSERVICE.methods_by_name['DescribeRankingEvent']._options = None
  _RANKINGSERVICE.methods_by_name['DescribeRankingEvent']._serialized_options = b'\202\343\n\031\212\343\n\025community:member:read\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\034\022\032/ranking-events/{event_id}'
  _RANKINGSERVICE.methods_by_name['ListRankingEvents']._options = None
  _RANKINGSERVICE.methods_by_name['ListRankingEvents']._serialized_options = b'\202\343\n\031\212\343\n\025community:member:read\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\021\022\017/ranking-events'
  _RANKINGSERVICE.methods_by_name['UpdateRankingPoint']._options = None
  _RANKINGSERVICE.methods_by_name['UpdateRankingPoint']._serialized_options = b'\202\343\n\032\212\343\n\026community:member:write\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002/\032-/ranking-series/{member_id}/points/{event_id}'
  _RANKINGSERVICE.methods_by_name['DeleteRankingPoint']._options = None
  _RANKINGSERVICE.methods_by_name['DeleteRankingPoint']._serialized_options = b'\202\343\n\032\212\343\n\026community:member:write\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002/*-/ranking-series/{member_id}/points/{event_id}'
  _RANKINGSERVICE.methods_by_name['DescribeRankingPoint']._options = None
  _RANKINGSERVICE.methods_by_name['DescribeRankingPoint']._serialized_options = b'\202\343\n\032\212\343\n\026community:member:write\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002/\022-/ranking-series/{member_id}/points/{event_id}'
  _RANKINGSERVICE.methods_by_name['ListRankingPoints']._options = None
  _RANKINGSERVICE.methods_by_name['ListRankingPoints']._serialized_options = b'\202\343\n\032\212\343\n\026community:member:write\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\035\022\033/ranking-series/{member_id}'
  _CREATERANKINGEVENTINPUT._serialized_start=304
  _CREATERANKINGEVENTINPUT._serialized_end=376
  _CREATERANKINGEVENTOUTPUT._serialized_start=378
  _CREATERANKINGEVENTOUTPUT._serialized_end=422
  _UPDATERANKINGEVENTINPUT._serialized_start=425
  _UPDATERANKINGEVENTINPUT._serialized_end=638
  _UPDATERANKINGEVENTINPUT_PATCH._serialized_start=581
  _UPDATERANKINGEVENTINPUT_PATCH._serialized_end=638
  _UPDATERANKINGEVENTOUTPUT._serialized_start=640
  _UPDATERANKINGEVENTOUTPUT._serialized_end=666
  _DELETERANKINGEVENTINPUT._serialized_start=668
  _DELETERANKINGEVENTINPUT._serialized_end=711
  _DELETERANKINGEVENTOUTPUT._serialized_start=713
  _DELETERANKINGEVENTOUTPUT._serialized_end=739
  _DESCRIBERANKINGEVENTINPUT._serialized_start=741
  _DESCRIBERANKINGEVENTINPUT._serialized_end=786
  _DESCRIBERANKINGEVENTOUTPUT._serialized_start=788
  _DESCRIBERANKINGEVENTOUTPUT._serialized_end=863
  _LISTRANKINGEVENTSINPUT._serialized_start=866
  _LISTRANKINGEVENTSINPUT._serialized_end=1347
  _LISTRANKINGEVENTSINPUT_FILTER._serialized_start=1098
  _LISTRANKINGEVENTSINPUT_FILTER._serialized_end=1310
  _LISTRANKINGEVENTSINPUT_SORTABLE._serialized_start=1312
  _LISTRANKINGEVENTSINPUT_SORTABLE._serialized_end=1347
  _LISTRANKINGEVENTSOUTPUT._serialized_start=1349
  _LISTRANKINGEVENTSOUTPUT._serialized_end=1436
  _UPDATERANKINGPOINTINPUT._serialized_start=1438
  _UPDATERANKINGPOINTINPUT._serialized_end=1547
  _UPDATERANKINGPOINTOUTPUT._serialized_start=1549
  _UPDATERANKINGPOINTOUTPUT._serialized_end=1575
  _DELETERANKINGPOINTINPUT._serialized_start=1577
  _DELETERANKINGPOINTINPUT._serialized_end=1686
  _DELETERANKINGPOINTOUTPUT._serialized_start=1688
  _DELETERANKINGPOINTOUTPUT._serialized_end=1714
  _DESCRIBERANKINGPOINTINPUT._serialized_start=1716
  _DESCRIBERANKINGPOINTINPUT._serialized_end=1780
  _DESCRIBERANKINGPOINTOUTPUT._serialized_start=1782
  _DESCRIBERANKINGPOINTOUTPUT._serialized_end=1857
  _LISTRANKINGPOINTSINPUT._serialized_start=1860
  _LISTRANKINGPOINTSINPUT._serialized_end=2239
  _LISTRANKINGPOINTSINPUT_FILTER._serialized_start=2110
  _LISTRANKINGPOINTSINPUT_FILTER._serialized_end=2212
  _LISTRANKINGPOINTSINPUT_SORTABLE._serialized_start=1312
  _LISTRANKINGPOINTSINPUT_SORTABLE._serialized_end=1337
  _LISTRANKINGPOINTSOUTPUT._serialized_start=2241
  _LISTRANKINGPOINTSOUTPUT._serialized_end=2328
  _RANKINGSERVICE._serialized_start=2331
  _RANKINGSERVICE._serialized_end=4106
# @@protoc_insertion_point(module_scope)