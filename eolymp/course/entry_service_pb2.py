# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/course/entry_service.proto
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
from eolymp.course import entry_pb2 as eolymp_dot_course_dot_entry__pb2
from eolymp.wellknown import direction_pb2 as eolymp_dot_wellknown_dot_direction__pb2
from eolymp.wellknown import expression_pb2 as eolymp_dot_wellknown_dot_expression__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!eolymp/course/entry_service.proto\x12\reolymp.course\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a\x19\x65olymp/course/entry.proto\x1a eolymp/wellknown/direction.proto\x1a!eolymp/wellknown/expression.proto\"7\n\x10\x43reateEntryInput\x12#\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x14.eolymp.course.Entry\"%\n\x11\x43reateEntryOutput\x12\x10\n\x08\x65ntry_id\x18\x01 \x01(\t\"\xa0\x02\n\x10UpdateEntryInput\x12\x34\n\x05patch\x18\x01 \x03(\x0e\x32%.eolymp.course.UpdateEntryInput.Patch\x12\x10\n\x08\x65ntry_id\x18\x02 \x01(\t\x12#\n\x05\x65ntry\x18\x03 \x01(\x0b\x32\x14.eolymp.course.Entry\"\x9e\x01\n\x05Patch\x12\x07\n\x03\x41LL\x10\x00\x12\t\n\x05TITLE\x10\x01\x12\t\n\x05\x44RAFT\x10\x02\x12\x0f\n\x0b\x43ONTENT_ALL\x10\x03\x12\x11\n\rSECTION_IMAGE\x10\n\x12\x17\n\x13SECTION_DESCRIPTION\x10\x0b\x12\x13\n\x0fVIDEO_IMAGE_URL\x10\x14\x12\x13\n\x0fVIDEO_VIDEO_URL\x10\x15\x12\x0f\n\x0bPROBLEM_URL\x10\x1e\"\x13\n\x11UpdateEntryOutput\"3\n\x10RenameEntryInput\x12\x10\n\x08\x65ntry_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\"\x13\n\x11RenameEntryOutput\"D\n\x0eMoveEntryInput\x12\x10\n\x08\x65ntry_id\x18\x01 \x01(\t\x12\x11\n\tparent_id\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\r\"\x11\n\x0fMoveEntryOutput\"$\n\x10\x44\x65leteEntryInput\x12\x10\n\x08\x65ntry_id\x18\x01 \x01(\t\"\x13\n\x11\x44\x65leteEntryOutput\"6\n\x12\x44\x65scribeEntryInput\x12\x10\n\x08\x65ntry_id\x18\x01 \x01(\t\x12\x0e\n\x06render\x18\x02 \x01(\x08\":\n\x13\x44\x65scribeEntryOutput\x12#\n\x05\x65ntry\x18\x01 \x01(\x0b\x32\x14.eolymp.course.Entry\"\xd3\x03\n\x10ListEntriesInput\x12\x0e\n\x06render\x18\x01 \x01(\x08\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12\x37\n\x07\x66ilters\x18( \x01(\x0b\x32&.eolymp.course.ListEntriesInput.Filter\x12\x36\n\x04sort\x18\x32 \x01(\x0e\x32(.eolymp.course.ListEntriesInput.Sortable\x12*\n\x05order\x18\x33 \x01(\x0e\x32\x1b.eolymp.wellknown.Direction\x1a\xda\x01\n\x06\x46ilter\x12\r\n\x05query\x18\x01 \x01(\t\x12*\n\x02id\x18\n \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x31\n\tparent_id\x18\x0b \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12/\n\x05\x64raft\x18\x0c \x03(\x0b\x32 .eolymp.wellknown.ExpressionBool\x12\x31\n\x05title\x18\r \x03(\x0b\x32\".eolymp.wellknown.ExpressionString\"\x17\n\x08Sortable\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\"G\n\x11ListEntriesOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12#\n\x05items\x18\x02 \x03(\x0b\x32\x14.eolymp.course.Entry\"A\n\x10\x44\x65scribeTOCInput\x12\x0f\n\x07root_id\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\r\x12\r\n\x05\x64raft\x18\x03 \x01(\x08\"8\n\x11\x44\x65scribeTOCOutput\x12#\n\x05items\x18\x02 \x03(\x0b\x32\x14.eolymp.course.Entry\"$\n\x10ListParentsInput\x12\x10\n\x08\x65ntry_id\x18\x01 \x01(\t\"8\n\x11ListParentsOutput\x12#\n\x05items\x18\x02 \x03(\x0b\x32\x14.eolymp.course.Entry\")\n\x15\x44\x65scribeProgressInput\x12\x10\n\x08\x65ntry_id\x18\x01 \x01(\t\"*\n\x16\x44\x65scribeProgressOutput\x12\x10\n\x08progress\x18\x01 \x01(\x02\"9\n\x13ReportProgressInput\x12\x10\n\x08\x65ntry_id\x18\x01 \x01(\t\x12\x10\n\x08progress\x18\x02 \x01(\x02\"\x16\n\x14ReportProgressOutput2\xc2\r\n\x0c\x45ntryService\x12\x8c\x01\n\x0b\x43reateEntry\x12\x1f.eolymp.course.CreateEntryInput\x1a .eolymp.course.CreateEntryOutput\":\x82\xe3\n\x17\x8a\xe3\n\x13\x63ourse:course:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\n\"\x08/entries\x12\x97\x01\n\x0bUpdateEntry\x12\x1f.eolymp.course.UpdateEntryInput\x1a .eolymp.course.UpdateEntryOutput\"E\x82\xe3\n\x17\x8a\xe3\n\x13\x63ourse:course:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x80?\xf8\xe2\n\x05\x82\xd3\xe4\x93\x02\x15\x1a\x13/entries/{entry_id}\x12\x9d\x01\n\x0bRenameEntry\x12\x1f.eolymp.course.RenameEntryInput\x1a .eolymp.course.RenameEntryOutput\"K\x82\xe3\n\x17\x8a\xe3\n\x13\x63ourse:course:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x1b\x1a\x19/entries/{entry_id}/title\x12\x9a\x01\n\tMoveEntry\x12\x1d.eolymp.course.MoveEntryInput\x1a\x1e.eolymp.course.MoveEntryOutput\"N\x82\xe3\n\x17\x8a\xe3\n\x13\x63ourse:course:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x1e\x1a\x1c/entries/{entry_id}/position\x12\x97\x01\n\x0b\x44\x65leteEntry\x12\x1f.eolymp.course.DeleteEntryInput\x1a .eolymp.course.DeleteEntryOutput\"E\x82\xe3\n\x17\x8a\xe3\n\x13\x63ourse:course:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x15*\x13/entries/{entry_id}\x12\x9c\x01\n\rDescribeEntry\x12!.eolymp.course.DescribeEntryInput\x1a\".eolymp.course.DescribeEntryOutput\"D\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0\x41\xf8\xe2\nd\x82\xd3\xe4\x93\x02\x15\x12\x13/entries/{entry_id}\x12\x8b\x01\n\x0bListEntries\x12\x1f.eolymp.course.ListEntriesInput\x1a .eolymp.course.ListEntriesOutput\"9\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\n\x12\x08/entries\x12\x87\x01\n\x0b\x44\x65scribeTOC\x12\x1f.eolymp.course.DescribeTOCInput\x1a .eolymp.course.DescribeTOCOutput\"5\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x06\x12\x04/toc\x12\x9e\x01\n\x0bListParents\x12\x1f.eolymp.course.ListParentsInput\x1a .eolymp.course.ListParentsOutput\"L\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x1d\x12\x1b/entries/{entry_id}/parents\x12\xae\x01\n\x10\x44\x65scribeProgress\x12$.eolymp.course.DescribeProgressInput\x1a%.eolymp.course.DescribeProgressOutput\"M\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x1e\x12\x1c/entries/{entry_id}/progress\x12\xa8\x01\n\x0eReportProgress\x12\".eolymp.course.ReportProgressInput\x1a#.eolymp.course.ReportProgressOutput\"M\x82\xe3\n\x16\x8a\xe3\n\x12\x63ourse:course:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x1e\x1a\x1c/entries/{entry_id}/progressB/Z-github.com/eolymp/go-sdk/eolymp/course;courseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.course.entry_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/eolymp/go-sdk/eolymp/course;course'
  _ENTRYSERVICE.methods_by_name['CreateEntry']._options = None
  _ENTRYSERVICE.methods_by_name['CreateEntry']._serialized_options = b'\202\343\n\027\212\343\n\023course:course:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\n\"\010/entries'
  _ENTRYSERVICE.methods_by_name['UpdateEntry']._options = None
  _ENTRYSERVICE.methods_by_name['UpdateEntry']._serialized_options = b'\202\343\n\027\212\343\n\023course:course:write\352\342\n\013\365\342\n\000\000\200?\370\342\n\005\202\323\344\223\002\025\032\023/entries/{entry_id}'
  _ENTRYSERVICE.methods_by_name['RenameEntry']._options = None
  _ENTRYSERVICE.methods_by_name['RenameEntry']._serialized_options = b'\202\343\n\027\212\343\n\023course:course:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\033\032\031/entries/{entry_id}/title'
  _ENTRYSERVICE.methods_by_name['MoveEntry']._options = None
  _ENTRYSERVICE.methods_by_name['MoveEntry']._serialized_options = b'\202\343\n\027\212\343\n\023course:course:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\036\032\034/entries/{entry_id}/position'
  _ENTRYSERVICE.methods_by_name['DeleteEntry']._options = None
  _ENTRYSERVICE.methods_by_name['DeleteEntry']._serialized_options = b'\202\343\n\027\212\343\n\023course:course:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\025*\023/entries/{entry_id}'
  _ENTRYSERVICE.methods_by_name['DescribeEntry']._options = None
  _ENTRYSERVICE.methods_by_name['DescribeEntry']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\240A\370\342\nd\202\323\344\223\002\025\022\023/entries/{entry_id}'
  _ENTRYSERVICE.methods_by_name['ListEntries']._options = None
  _ENTRYSERVICE.methods_by_name['ListEntries']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\n\022\010/entries'
  _ENTRYSERVICE.methods_by_name['DescribeTOC']._options = None
  _ENTRYSERVICE.methods_by_name['DescribeTOC']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\240@\370\342\n\n\202\323\344\223\002\006\022\004/toc'
  _ENTRYSERVICE.methods_by_name['ListParents']._options = None
  _ENTRYSERVICE.methods_by_name['ListParents']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\240@\370\342\n\n\202\323\344\223\002\035\022\033/entries/{entry_id}/parents'
  _ENTRYSERVICE.methods_by_name['DescribeProgress']._options = None
  _ENTRYSERVICE.methods_by_name['DescribeProgress']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\240@\370\342\n\n\202\323\344\223\002\036\022\034/entries/{entry_id}/progress'
  _ENTRYSERVICE.methods_by_name['ReportProgress']._options = None
  _ENTRYSERVICE.methods_by_name['ReportProgress']._serialized_options = b'\202\343\n\026\212\343\n\022course:course:read\352\342\n\013\365\342\n\000\000\240@\370\342\n\n\202\323\344\223\002\036\032\034/entries/{entry_id}/progress'
  _CREATEENTRYINPUT._serialized_start=247
  _CREATEENTRYINPUT._serialized_end=302
  _CREATEENTRYOUTPUT._serialized_start=304
  _CREATEENTRYOUTPUT._serialized_end=341
  _UPDATEENTRYINPUT._serialized_start=344
  _UPDATEENTRYINPUT._serialized_end=632
  _UPDATEENTRYINPUT_PATCH._serialized_start=474
  _UPDATEENTRYINPUT_PATCH._serialized_end=632
  _UPDATEENTRYOUTPUT._serialized_start=634
  _UPDATEENTRYOUTPUT._serialized_end=653
  _RENAMEENTRYINPUT._serialized_start=655
  _RENAMEENTRYINPUT._serialized_end=706
  _RENAMEENTRYOUTPUT._serialized_start=708
  _RENAMEENTRYOUTPUT._serialized_end=727
  _MOVEENTRYINPUT._serialized_start=729
  _MOVEENTRYINPUT._serialized_end=797
  _MOVEENTRYOUTPUT._serialized_start=799
  _MOVEENTRYOUTPUT._serialized_end=816
  _DELETEENTRYINPUT._serialized_start=818
  _DELETEENTRYINPUT._serialized_end=854
  _DELETEENTRYOUTPUT._serialized_start=856
  _DELETEENTRYOUTPUT._serialized_end=875
  _DESCRIBEENTRYINPUT._serialized_start=877
  _DESCRIBEENTRYINPUT._serialized_end=931
  _DESCRIBEENTRYOUTPUT._serialized_start=933
  _DESCRIBEENTRYOUTPUT._serialized_end=991
  _LISTENTRIESINPUT._serialized_start=994
  _LISTENTRIESINPUT._serialized_end=1461
  _LISTENTRIESINPUT_FILTER._serialized_start=1218
  _LISTENTRIESINPUT_FILTER._serialized_end=1436
  _LISTENTRIESINPUT_SORTABLE._serialized_start=1438
  _LISTENTRIESINPUT_SORTABLE._serialized_end=1461
  _LISTENTRIESOUTPUT._serialized_start=1463
  _LISTENTRIESOUTPUT._serialized_end=1534
  _DESCRIBETOCINPUT._serialized_start=1536
  _DESCRIBETOCINPUT._serialized_end=1601
  _DESCRIBETOCOUTPUT._serialized_start=1603
  _DESCRIBETOCOUTPUT._serialized_end=1659
  _LISTPARENTSINPUT._serialized_start=1661
  _LISTPARENTSINPUT._serialized_end=1697
  _LISTPARENTSOUTPUT._serialized_start=1699
  _LISTPARENTSOUTPUT._serialized_end=1755
  _DESCRIBEPROGRESSINPUT._serialized_start=1757
  _DESCRIBEPROGRESSINPUT._serialized_end=1798
  _DESCRIBEPROGRESSOUTPUT._serialized_start=1800
  _DESCRIBEPROGRESSOUTPUT._serialized_end=1842
  _REPORTPROGRESSINPUT._serialized_start=1844
  _REPORTPROGRESSINPUT._serialized_end=1901
  _REPORTPROGRESSOUTPUT._serialized_start=1903
  _REPORTPROGRESSOUTPUT._serialized_end=1925
  _ENTRYSERVICE._serialized_start=1928
  _ENTRYSERVICE._serialized_end=3658
# @@protoc_insertion_point(module_scope)
