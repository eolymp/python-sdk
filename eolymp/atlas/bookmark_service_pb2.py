# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/atlas/bookmark_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#eolymp/atlas/bookmark_service.proto\x12\x0c\x65olymp.atlas\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\"8\n\x10SetBookmarkInput\x12\x12\n\nproblem_id\x18\x01 \x01(\t\x12\x10\n\x08\x62ookmark\x18\x02 \x01(\x08\"\x13\n\x11SetBookmarkOutput\"&\n\x10GetBookmarkInput\x12\x12\n\nproblem_id\x18\x01 \x01(\t\"%\n\x11GetBookmarkOutput\x12\x10\n\x08\x62ookmark\x18\x01 \x01(\x08\x32\xf5\x01\n\x0f\x42ookmarkService\x12p\n\x0bGetBookmark\x12\x1e.eolymp.atlas.GetBookmarkInput\x1a\x1f.eolymp.atlas.GetBookmarkOutput\" \xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xc8\x41\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x0b\x12\t/bookmark\x12p\n\x0bSetBookmark\x12\x1e.eolymp.atlas.SetBookmarkInput\x1a\x1f.eolymp.atlas.SetBookmarkOutput\" \xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x0b\"\t/bookmarkB-Z+github.com/eolymp/go-sdk/eolymp/atlas;atlasb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.atlas.bookmark_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/eolymp/go-sdk/eolymp/atlas;atlas'
  _BOOKMARKSERVICE.methods_by_name['GetBookmark']._options = None
  _BOOKMARKSERVICE.methods_by_name['GetBookmark']._serialized_options = b'\352\342\n\013\365\342\n\000\000\310A\370\342\nd\202\323\344\223\002\013\022\t/bookmark'
  _BOOKMARKSERVICE.methods_by_name['SetBookmark']._options = None
  _BOOKMARKSERVICE.methods_by_name['SetBookmark']._serialized_options = b'\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\013\"\t/bookmark'
  _SETBOOKMARKINPUT._serialized_start=120
  _SETBOOKMARKINPUT._serialized_end=176
  _SETBOOKMARKOUTPUT._serialized_start=178
  _SETBOOKMARKOUTPUT._serialized_end=197
  _GETBOOKMARKINPUT._serialized_start=199
  _GETBOOKMARKINPUT._serialized_end=237
  _GETBOOKMARKOUTPUT._serialized_start=239
  _GETBOOKMARKOUTPUT._serialized_end=276
  _BOOKMARKSERVICE._serialized_start=279
  _BOOKMARKSERVICE._serialized_end=524
# @@protoc_insertion_point(module_scope)