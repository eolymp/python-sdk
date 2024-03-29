# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/asset/asset_service.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n eolymp/asset/asset_service.proto\x12\x0c\x65olymp.asset\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\"\xc2\x02\n\x10UploadImageInput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x31\n\x04\x63rop\x18\n \x01(\x0b\x32#.eolymp.asset.UploadImageInput.Crop\x12\x31\n\x04size\x18\x0b \x01(\x0b\x32#.eolymp.asset.UploadImageInput.Size\x12\x35\n\x08variants\x18\x14 \x03(\x0b\x32#.eolymp.asset.UploadImageInput.Size\x12\x0c\n\x04\x64\x61ta\x18\x64 \x01(\x0c\x1a%\n\x04Size\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x1a@\n\x04\x43rop\x12\x0b\n\x03top\x18\x01 \x01(\r\x12\r\n\x05right\x18\x02 \x01(\r\x12\x0e\n\x06\x62ottom\x18\x03 \x01(\r\x12\x0c\n\x04left\x18\x04 \x01(\r\"&\n\x11UploadImageOutput\x12\x11\n\timage_url\x18\x01 \x01(\t\";\n\x0fUploadFileInput\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x64 \x01(\x0c\"$\n\x10UploadFileOutput\x12\x10\n\x08\x66ile_url\x18\x01 \x01(\t2\xac\x02\n\x0c\x41ssetService\x12\x8e\x01\n\x0bUploadImage\x12\x1e.eolymp.asset.UploadImageInput\x1a\x1f.eolymp.asset.UploadImageOutput\">\x82\xe3\n\x15\x8a\xe3\n\x11\x61sset:image:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x10\"\x0e/assets/images\x12\x8a\x01\n\nUploadFile\x12\x1d.eolymp.asset.UploadFileInput\x1a\x1e.eolymp.asset.UploadFileOutput\"=\x82\xe3\n\x15\x8a\xe3\n\x11\x61sset:image:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x0f\"\r/assets/filesB-Z+github.com/eolymp/go-sdk/eolymp/asset;assetb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.asset.asset_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/eolymp/go-sdk/eolymp/asset;asset'
  _ASSETSERVICE.methods_by_name['UploadImage']._options = None
  _ASSETSERVICE.methods_by_name['UploadImage']._serialized_options = b'\202\343\n\025\212\343\n\021asset:image:write\352\342\n\013\365\342\n\000\000\000@\370\342\nd\202\323\344\223\002\020\"\016/assets/images'
  _ASSETSERVICE.methods_by_name['UploadFile']._options = None
  _ASSETSERVICE.methods_by_name['UploadFile']._serialized_options = b'\202\343\n\025\212\343\n\021asset:image:write\352\342\n\013\365\342\n\000\000\000@\370\342\nd\202\323\344\223\002\017\"\r/assets/files'
  _UPLOADIMAGEINPUT._serialized_start=150
  _UPLOADIMAGEINPUT._serialized_end=472
  _UPLOADIMAGEINPUT_SIZE._serialized_start=369
  _UPLOADIMAGEINPUT_SIZE._serialized_end=406
  _UPLOADIMAGEINPUT_CROP._serialized_start=408
  _UPLOADIMAGEINPUT_CROP._serialized_end=472
  _UPLOADIMAGEOUTPUT._serialized_start=474
  _UPLOADIMAGEOUTPUT._serialized_end=512
  _UPLOADFILEINPUT._serialized_start=514
  _UPLOADFILEINPUT._serialized_end=573
  _UPLOADFILEOUTPUT._serialized_start=575
  _UPLOADFILEOUTPUT._serialized_end=611
  _ASSETSERVICE._serialized_start=614
  _ASSETSERVICE._serialized_end=914
# @@protoc_insertion_point(module_scope)
