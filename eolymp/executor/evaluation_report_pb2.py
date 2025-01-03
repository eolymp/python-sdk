# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/executor/evaluation_report.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.executor import stats_pb2 as eolymp_dot_executor_dot_stats__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'eolymp/executor/evaluation_report.proto\x12\x0f\x65olymp.executor\x1a\x1b\x65olymp/executor/stats.proto\"\xba\t\n\x10\x45valuationReport\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x11\n\treference\x18\x02 \x01(\t\x12\x0e\n\x06origin\x18\x03 \x01(\t\x12\r\n\x05\x61gent\x18\x04 \x01(\t\x12\x11\n\tsignature\x18\x32 \x01(\t\x12\x0f\n\x07version\x18\x64 \x01(\r\x12\x34\n\x04type\x18\n \x01(\x0e\x32&.eolymp.executor.EvaluationReport.Type\x12\x38\n\x06status\x18\x0b \x01(\x0e\x32(.eolymp.executor.EvaluationReport.Status\x12\x15\n\rerror_message\x18\x14 \x01(\t\x12\x33\n\x04runs\x18( \x03(\x0b\x32%.eolymp.executor.EvaluationReport.Run\x1a\xb1\x05\n\x03Run\x12\x11\n\treference\x18\x01 \x01(\t\x12<\n\x06status\x18\x02 \x01(\x0e\x32,.eolymp.executor.EvaluationReport.Run.Status\x12\r\n\x05score\x18P \x01(\x02\x12\x0c\n\x04\x63ost\x18Q \x01(\x02\x12\x17\n\x0fwall_time_usage\x18\x33 \x01(\r\x12\x17\n\x0fwall_time_limit\x18= \x01(\r\x12\x16\n\x0e\x63pu_time_usage\x18\x34 \x01(\r\x12\x16\n\x0e\x63pu_time_limit\x18> \x01(\r\x12\x14\n\x0cmemory_usage\x18\x35 \x01(\x04\x12\x14\n\x0cmemory_limit\x18? \x01(\x04\x12\x11\n\tinput_url\x18\n \x01(\t\x12\x12\n\noutput_url\x18\x0b \x01(\t\x12\x12\n\nanswer_url\x18\x0c \x01(\t\x12+\n\x0b\x64\x65\x62ug_stats\x18Z \x01(\x0b\x32\x16.eolymp.executor.Stats\x12-\n\rchecker_stats\x18# \x01(\x0b\x32\x16.eolymp.executor.Stats\x12\x30\n\x10interactor_stats\x18- \x01(\x0b\x32\x16.eolymp.executor.Stats\"\xe4\x01\n\x06Status\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\r\n\tEXECUTING\x10\x02\x12\x0b\n\x07TIMEOUT\x10\x03\x12\x11\n\rCPU_EXHAUSTED\x10\x04\x12\x13\n\x0fMEMORY_OVERFLOW\x10\x05\x12\x11\n\rRUNTIME_ERROR\x10\x06\x12\x0c\n\x08\x45XECUTED\x10\x07\x12\x0c\n\x08\x41\x43\x43\x45PTED\x10\x08\x12\x10\n\x0cWRONG_ANSWER\x10\t\x12\x18\n\x14VERIFICATION_FAILURE\x10\n\x12\x0b\n\x07SKIPPED\x10\x0b\x12\x17\n\x13INTERACTION_FAILURE\x10\x0c\"\x81\x01\n\x06Status\x12\x12\n\x0eUNKNOWN_STATUS\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x10\n\x0cPROVISIONING\x10\x02\x12\x10\n\x0cINITIALIZING\x10\x03\x12\r\n\tEXECUTING\x10\x04\x12\x0c\n\x08\x43OMPLETE\x10\x05\x12\t\n\x05\x45RROR\x10\x06\x12\n\n\x06\x46\x41ILED\x10\x07\"K\n\x04Type\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x0f\n\x0bTYPE_UPDATE\x10\x01\x12\x0e\n\nTYPE_ERROR\x10\x02\x12\x10\n\x0cTYPE_FAILURE\x10\x03\x42\x33Z1github.com/eolymp/go-sdk/eolymp/executor;executorb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.executor.evaluation_report_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/eolymp/go-sdk/eolymp/executor;executor'
  _globals['_EVALUATIONREPORT']._serialized_start=90
  _globals['_EVALUATIONREPORT']._serialized_end=1300
  _globals['_EVALUATIONREPORT_RUN']._serialized_start=402
  _globals['_EVALUATIONREPORT_RUN']._serialized_end=1091
  _globals['_EVALUATIONREPORT_RUN_STATUS']._serialized_start=863
  _globals['_EVALUATIONREPORT_RUN_STATUS']._serialized_end=1091
  _globals['_EVALUATIONREPORT_STATUS']._serialized_start=1094
  _globals['_EVALUATIONREPORT_STATUS']._serialized_end=1223
  _globals['_EVALUATIONREPORT_TYPE']._serialized_start=1225
  _globals['_EVALUATIONREPORT_TYPE']._serialized_end=1300
# @@protoc_insertion_point(module_scope)
