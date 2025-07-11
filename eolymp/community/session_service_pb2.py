# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/community/session_service.proto
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
    'eolymp/community/session_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.annotations import scope_pb2 as eolymp_dot_annotations_dot_scope__pb2
from eolymp.community import session_pb2 as eolymp_dot_community_dot_session__pb2
from eolymp.wellknown import expression_pb2 as eolymp_dot_wellknown_dot_expression__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&eolymp/community/session_service.proto\x12\x10\x65olymp.community\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a\x1e\x65olymp/community/session.proto\x1a!eolymp/wellknown/expression.proto\"*\n\x14\x44\x65scribeSessionInput\x12\x12\n\nsession_id\x18\x01 \x01(\t\"C\n\x15\x44\x65scribeSessionOutput\x12*\n\x07session\x18\x01 \x01(\x0b\x32\x19.eolymp.community.Session\"\xd6\x02\n\x11ListSessionsInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12;\n\x07\x66ilters\x18( \x01(\x0b\x32*.eolymp.community.ListSessionsInput.Filter\x1a\xe5\x01\n\x06\x46ilter\x12*\n\x02id\x18\x01 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x34\n\nip_address\x18\x02 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\x12<\n\rfirst_seen_at\x18\x05 \x03(\x0b\x32%.eolymp.wellknown.ExpressionTimestamp\x12;\n\x0clast_seen_at\x18\x06 \x03(\x0b\x32%.eolymp.wellknown.ExpressionTimestamp\"M\n\x12ListSessionsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12(\n\x05items\x18\x02 \x03(\x0b\x32\x19.eolymp.community.Session\"+\n\x15TerminateSessionInput\x12\x12\n\nsession_id\x18\x01 \x01(\t\"\x18\n\x16TerminateSessionOutput\"/\n\x19TerminateAllSessionsInput\x12\x12\n\nsession_id\x18\x01 \x01(\t\"H\n\x1aTerminateAllSessionsOutput\x12*\n\x07session\x18\x01 \x01(\x0b\x32\x19.eolymp.community.Session2\xdb\x05\n\x0eSessionService\x12\xae\x01\n\x0f\x44\x65scribeSession\x12&.eolymp.community.DescribeSessionInput\x1a\'.eolymp.community.DescribeSessionOutput\"J\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xe3\n\x19\x8a\xe3\n\x15\x63ommunity:member:read\x82\xd3\xe4\x93\x02\x18\x12\x16/sessions/{session_id}\x12\x98\x01\n\x0cListSessions\x12#.eolymp.community.ListSessionsInput\x1a$.eolymp.community.ListSessionsOutput\"=\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xe3\n\x19\x8a\xe3\n\x15\x63ommunity:member:read\x82\xd3\xe4\x93\x02\x0b\x12\t/sessions\x12\xbb\x01\n\x10TerminateSession\x12\'.eolymp.community.TerminateSessionInput\x1a(.eolymp.community.TerminateSessionOutput\"T\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xe3\n\x19\x8a\xe3\n\x15\x63ommunity:member:read\x82\xd3\xe4\x93\x02\"\" /sessions/{session_id}/terminate\x12\xbe\x01\n\x14TerminateAllSessions\x12+.eolymp.community.TerminateAllSessionsInput\x1a,.eolymp.community.TerminateAllSessionsOutput\"K\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xe3\n\x19\x8a\xe3\n\x15\x63ommunity:member:read\x82\xd3\xe4\x93\x02\x19\"\x17/sessions:terminate-allB5Z3github.com/eolymp/go-sdk/eolymp/community;communityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.community.session_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z3github.com/eolymp/go-sdk/eolymp/community;community'
  _globals['_SESSIONSERVICE'].methods_by_name['DescribeSession']._loaded_options = None
  _globals['_SESSIONSERVICE'].methods_by_name['DescribeSession']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\343\n\031\212\343\n\025community:member:read\202\323\344\223\002\030\022\026/sessions/{session_id}'
  _globals['_SESSIONSERVICE'].methods_by_name['ListSessions']._loaded_options = None
  _globals['_SESSIONSERVICE'].methods_by_name['ListSessions']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\343\n\031\212\343\n\025community:member:read\202\323\344\223\002\013\022\t/sessions'
  _globals['_SESSIONSERVICE'].methods_by_name['TerminateSession']._loaded_options = None
  _globals['_SESSIONSERVICE'].methods_by_name['TerminateSession']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\343\n\031\212\343\n\025community:member:read\202\323\344\223\002\"\" /sessions/{session_id}/terminate'
  _globals['_SESSIONSERVICE'].methods_by_name['TerminateAllSessions']._loaded_options = None
  _globals['_SESSIONSERVICE'].methods_by_name['TerminateAllSessions']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\343\n\031\212\343\n\025community:member:read\202\323\344\223\002\031\"\027/sessions:terminate-all'
  _globals['_DESCRIBESESSIONINPUT']._serialized_start=226
  _globals['_DESCRIBESESSIONINPUT']._serialized_end=268
  _globals['_DESCRIBESESSIONOUTPUT']._serialized_start=270
  _globals['_DESCRIBESESSIONOUTPUT']._serialized_end=337
  _globals['_LISTSESSIONSINPUT']._serialized_start=340
  _globals['_LISTSESSIONSINPUT']._serialized_end=682
  _globals['_LISTSESSIONSINPUT_FILTER']._serialized_start=453
  _globals['_LISTSESSIONSINPUT_FILTER']._serialized_end=682
  _globals['_LISTSESSIONSOUTPUT']._serialized_start=684
  _globals['_LISTSESSIONSOUTPUT']._serialized_end=761
  _globals['_TERMINATESESSIONINPUT']._serialized_start=763
  _globals['_TERMINATESESSIONINPUT']._serialized_end=806
  _globals['_TERMINATESESSIONOUTPUT']._serialized_start=808
  _globals['_TERMINATESESSIONOUTPUT']._serialized_end=832
  _globals['_TERMINATEALLSESSIONSINPUT']._serialized_start=834
  _globals['_TERMINATEALLSESSIONSINPUT']._serialized_end=881
  _globals['_TERMINATEALLSESSIONSOUTPUT']._serialized_start=883
  _globals['_TERMINATEALLSESSIONSOUTPUT']._serialized_end=955
  _globals['_SESSIONSERVICE']._serialized_start=958
  _globals['_SESSIONSERVICE']._serialized_end=1689
# @@protoc_insertion_point(module_scope)
