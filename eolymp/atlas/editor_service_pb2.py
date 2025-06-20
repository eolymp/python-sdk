# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/atlas/editor_service.proto
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
    'eolymp/atlas/editor_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.annotations import scope_pb2 as eolymp_dot_annotations_dot_scope__pb2
from eolymp.runtime import runtime_pb2 as eolymp_dot_runtime_dot_runtime__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!eolymp/atlas/editor_service.proto\x12\x0c\x65olymp.atlas\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a\x1c\x65olymp/runtime/runtime.proto\"\xaf\x02\n\x06\x45\x64itor\x12)\n\x05state\x18\x01 \x01(\x0b\x32\x1a.eolymp.atlas.Editor.State\x12.\n\x08\x66\x65\x61tures\x18\n \x03(\x0e\x32\x1c.eolymp.atlas.Editor.Feature\x12)\n\x08runtimes\x18\x0b \x03(\x0b\x32\x17.eolymp.runtime.Runtime\x1a\x41\n\x05State\x12\x0f\n\x07runtime\x18\x01 \x01(\t\x12\x13\n\x0bsource_code\x18\x02 \x01(\t\x12\x12\n\ninput_data\x18\x03 \x01(\t\"\\\n\x07\x46\x65\x61ture\x12\x13\n\x0fUNKNOWN_FEATURE\x10\x00\x12\x0e\n\nPRINT_CODE\x10\x01\x12\x0c\n\x08RUN_CODE\x10\x02\x12\x0f\n\x0bUPLOAD_CODE\x10\x03\x12\r\n\tEDIT_CODE\x10\x04\"\x15\n\x13\x44\x65scribeEditorInput\"<\n\x14\x44\x65scribeEditorOutput\x12$\n\x06\x65\x64itor\x18\x01 \x01(\x0b\x32\x14.eolymp.atlas.Editor\"\x1a\n\x18\x44\x65scribeEditorStateInput\"\x85\x01\n\x19\x44\x65scribeEditorStateOutput\x12\x0f\n\x07runtime\x18\x01 \x01(\t\x12\x13\n\x0bsource_code\x18\x02 \x01(\t\x12\x12\n\ninput_data\x18\x03 \x01(\t\x12.\n\x08\x66\x65\x61tures\x18\n \x03(\x0e\x32\x1c.eolymp.atlas.Editor.Feature\"R\n\x16UpdateEditorStateInput\x12\x0f\n\x07runtime\x18\x01 \x01(\t\x12\x13\n\x0bsource_code\x18\x02 \x01(\t\x12\x12\n\ninput_data\x18\x03 \x01(\t\"\x19\n\x17UpdateEditorStateOutput\"<\n\x14PrintEditorCodeInput\x12\x0f\n\x07runtime\x18\x01 \x01(\t\x12\x13\n\x0bsource_code\x18\x02 \x01(\t\"\x17\n\x15PrintEditorCodeOutput2\x9a\x05\n\rEditorService\x12\x94\x01\n\x0e\x44\x65scribeEditor\x12!.eolymp.atlas.DescribeEditorInput\x1a\".eolymp.atlas.DescribeEditorOutput\";\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\n\x82\xe3\n\x19\x8a\xe3\n\x15\x61tlas:submission:read\x82\xd3\xe4\x93\x02\t\x12\x07/editor\x12\xa9\x01\n\x13\x44\x65scribeEditorState\x12&.eolymp.atlas.DescribeEditorStateInput\x1a\'.eolymp.atlas.DescribeEditorStateOutput\"A\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\n\x82\xe3\n\x19\x8a\xe3\n\x15\x61tlas:submission:read\x82\xd3\xe4\x93\x02\x0f\x12\r/editor/state\x12\xa4\x01\n\x11UpdateEditorState\x12$.eolymp.atlas.UpdateEditorStateInput\x1a%.eolymp.atlas.UpdateEditorStateOutput\"B\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x02\x82\xe3\n\x1a\x8a\xe3\n\x16\x61tlas:submission:write\x82\xd3\xe4\x93\x02\x0f\"\r/editor/state\x12\x9e\x01\n\x0fPrintEditorCode\x12\".eolymp.atlas.PrintEditorCodeInput\x1a#.eolymp.atlas.PrintEditorCodeOutput\"B\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x02\x82\xe3\n\x1a\x8a\xe3\n\x16\x61tlas:submission:write\x82\xd3\xe4\x93\x02\x0f\"\r/editor/printB-Z+github.com/eolymp/go-sdk/eolymp/atlas;atlasb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.atlas.editor_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/eolymp/go-sdk/eolymp/atlas;atlas'
  _globals['_EDITORSERVICE'].methods_by_name['DescribeEditor']._loaded_options = None
  _globals['_EDITORSERVICE'].methods_by_name['DescribeEditor']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\n\202\343\n\031\212\343\n\025atlas:submission:read\202\323\344\223\002\t\022\007/editor'
  _globals['_EDITORSERVICE'].methods_by_name['DescribeEditorState']._loaded_options = None
  _globals['_EDITORSERVICE'].methods_by_name['DescribeEditorState']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\n\202\343\n\031\212\343\n\025atlas:submission:read\202\323\344\223\002\017\022\r/editor/state'
  _globals['_EDITORSERVICE'].methods_by_name['UpdateEditorState']._loaded_options = None
  _globals['_EDITORSERVICE'].methods_by_name['UpdateEditorState']._serialized_options = b'\352\342\n\013\365\342\n\000\000\200?\370\342\n\002\202\343\n\032\212\343\n\026atlas:submission:write\202\323\344\223\002\017\"\r/editor/state'
  _globals['_EDITORSERVICE'].methods_by_name['PrintEditorCode']._loaded_options = None
  _globals['_EDITORSERVICE'].methods_by_name['PrintEditorCode']._serialized_options = b'\352\342\n\013\365\342\n\000\000\200?\370\342\n\002\202\343\n\032\212\343\n\026atlas:submission:write\202\323\344\223\002\017\"\r/editor/print'
  _globals['_EDITOR']._serialized_start=181
  _globals['_EDITOR']._serialized_end=484
  _globals['_EDITOR_STATE']._serialized_start=325
  _globals['_EDITOR_STATE']._serialized_end=390
  _globals['_EDITOR_FEATURE']._serialized_start=392
  _globals['_EDITOR_FEATURE']._serialized_end=484
  _globals['_DESCRIBEEDITORINPUT']._serialized_start=486
  _globals['_DESCRIBEEDITORINPUT']._serialized_end=507
  _globals['_DESCRIBEEDITOROUTPUT']._serialized_start=509
  _globals['_DESCRIBEEDITOROUTPUT']._serialized_end=569
  _globals['_DESCRIBEEDITORSTATEINPUT']._serialized_start=571
  _globals['_DESCRIBEEDITORSTATEINPUT']._serialized_end=597
  _globals['_DESCRIBEEDITORSTATEOUTPUT']._serialized_start=600
  _globals['_DESCRIBEEDITORSTATEOUTPUT']._serialized_end=733
  _globals['_UPDATEEDITORSTATEINPUT']._serialized_start=735
  _globals['_UPDATEEDITORSTATEINPUT']._serialized_end=817
  _globals['_UPDATEEDITORSTATEOUTPUT']._serialized_start=819
  _globals['_UPDATEEDITORSTATEOUTPUT']._serialized_end=844
  _globals['_PRINTEDITORCODEINPUT']._serialized_start=846
  _globals['_PRINTEDITORCODEINPUT']._serialized_end=906
  _globals['_PRINTEDITORCODEOUTPUT']._serialized_start=908
  _globals['_PRINTEDITORCODEOUTPUT']._serialized_end=931
  _globals['_EDITORSERVICE']._serialized_start=934
  _globals['_EDITORSERVICE']._serialized_end=1600
# @@protoc_insertion_point(module_scope)
