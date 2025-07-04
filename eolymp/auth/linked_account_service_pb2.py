# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: eolymp/auth/linked_account_service.proto
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
    'eolymp/auth/linked_account_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from eolymp.annotations import http_pb2 as eolymp_dot_annotations_dot_http__pb2
from eolymp.annotations import ratelimit_pb2 as eolymp_dot_annotations_dot_ratelimit__pb2
from eolymp.auth import linked_account_pb2 as eolymp_dot_auth_dot_linked__account__pb2
from eolymp.wellknown import expression_pb2 as eolymp_dot_wellknown_dot_expression__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(eolymp/auth/linked_account_service.proto\x12\x0b\x65olymp.auth\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a eolymp/auth/linked_account.proto\x1a!eolymp/wellknown/expression.proto\"`\n\x19RequestLinkedAccountInput\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.eolymp.auth.LinkedAccount.Type\x12\x14\n\x0c\x63\x61llback_uri\x18\x02 \x01(\t\"2\n\x1aRequestLinkedAccountOutput\x12\x14\n\x0credirect_uri\x18\x01 \x01(\t\"7\n\x18\x43reateLinkedAccountInput\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\",\n\x19\x43reateLinkedAccountOutput\x12\x0f\n\x07link_id\x18\x01 \x01(\t\"+\n\x18\x44\x65leteLinkedAccountInput\x12\x0f\n\x07link_id\x18\x01 \x01(\t\"\x1b\n\x19\x44\x65leteLinkedAccountOutput\"-\n\x1a\x44\x65scribeLinkedAccountInput\x12\x0f\n\x07link_id\x18\x01 \x01(\t\"G\n\x1b\x44\x65scribeLinkedAccountOutput\x12(\n\x04link\x18\x01 \x01(\x0b\x32\x1a.eolymp.auth.LinkedAccount\"\xdb\x01\n\x17ListLinkedAccountsInput\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12<\n\x07\x66ilters\x18( \x01(\x0b\x32+.eolymp.auth.ListLinkedAccountsInput.Filter\x1a\x64\n\x06\x46ilter\x12*\n\x02id\x18\x02 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12.\n\x04type\x18\x03 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\"T\n\x18ListLinkedAccountsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12)\n\x05items\x18\x02 \x03(\x0b\x32\x1a.eolymp.auth.LinkedAccount2\x88\x06\n\x14LinkedAccountService\x12\x98\x01\n\x14RequestLinkedAccount\x12&.eolymp.auth.RequestLinkedAccountInput\x1a\'.eolymp.auth.RequestLinkedAccountOutput\"/\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x1a\"\x18/linked-accounts:request\x12\x8d\x01\n\x13\x43reateLinkedAccount\x12%.eolymp.auth.CreateLinkedAccountInput\x1a&.eolymp.auth.CreateLinkedAccountOutput\"\'\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x12\"\x10/linked-accounts\x12\x97\x01\n\x13\x44\x65leteLinkedAccount\x12%.eolymp.auth.DeleteLinkedAccountInput\x1a&.eolymp.auth.DeleteLinkedAccountOutput\"1\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x1c*\x1a/linked-accounts/{link_id}\x12\x9d\x01\n\x15\x44\x65scribeLinkedAccount\x12\'.eolymp.auth.DescribeLinkedAccountInput\x1a(.eolymp.auth.DescribeLinkedAccountOutput\"1\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x1c\x12\x1a/linked-accounts/{link_id}\x12\x8a\x01\n\x12ListLinkedAccounts\x12$.eolymp.auth.ListLinkedAccountsInput\x1a%.eolymp.auth.ListLinkedAccountsOutput\"\'\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x12\x12\x10/linked-accountsB+Z)github.com/eolymp/go-sdk/eolymp/auth;authb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.auth.linked_account_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z)github.com/eolymp/go-sdk/eolymp/auth;auth'
  _globals['_LINKEDACCOUNTSERVICE'].methods_by_name['RequestLinkedAccount']._loaded_options = None
  _globals['_LINKEDACCOUNTSERVICE'].methods_by_name['RequestLinkedAccount']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\032\"\030/linked-accounts:request'
  _globals['_LINKEDACCOUNTSERVICE'].methods_by_name['CreateLinkedAccount']._loaded_options = None
  _globals['_LINKEDACCOUNTSERVICE'].methods_by_name['CreateLinkedAccount']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\022\"\020/linked-accounts'
  _globals['_LINKEDACCOUNTSERVICE'].methods_by_name['DeleteLinkedAccount']._loaded_options = None
  _globals['_LINKEDACCOUNTSERVICE'].methods_by_name['DeleteLinkedAccount']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\034*\032/linked-accounts/{link_id}'
  _globals['_LINKEDACCOUNTSERVICE'].methods_by_name['DescribeLinkedAccount']._loaded_options = None
  _globals['_LINKEDACCOUNTSERVICE'].methods_by_name['DescribeLinkedAccount']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\034\022\032/linked-accounts/{link_id}'
  _globals['_LINKEDACCOUNTSERVICE'].methods_by_name['ListLinkedAccounts']._loaded_options = None
  _globals['_LINKEDACCOUNTSERVICE'].methods_by_name['ListLinkedAccounts']._serialized_options = b'\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\022\022\020/linked-accounts'
  _globals['_REQUESTLINKEDACCOUNTINPUT']._serialized_start=193
  _globals['_REQUESTLINKEDACCOUNTINPUT']._serialized_end=289
  _globals['_REQUESTLINKEDACCOUNTOUTPUT']._serialized_start=291
  _globals['_REQUESTLINKEDACCOUNTOUTPUT']._serialized_end=341
  _globals['_CREATELINKEDACCOUNTINPUT']._serialized_start=343
  _globals['_CREATELINKEDACCOUNTINPUT']._serialized_end=398
  _globals['_CREATELINKEDACCOUNTOUTPUT']._serialized_start=400
  _globals['_CREATELINKEDACCOUNTOUTPUT']._serialized_end=444
  _globals['_DELETELINKEDACCOUNTINPUT']._serialized_start=446
  _globals['_DELETELINKEDACCOUNTINPUT']._serialized_end=489
  _globals['_DELETELINKEDACCOUNTOUTPUT']._serialized_start=491
  _globals['_DELETELINKEDACCOUNTOUTPUT']._serialized_end=518
  _globals['_DESCRIBELINKEDACCOUNTINPUT']._serialized_start=520
  _globals['_DESCRIBELINKEDACCOUNTINPUT']._serialized_end=565
  _globals['_DESCRIBELINKEDACCOUNTOUTPUT']._serialized_start=567
  _globals['_DESCRIBELINKEDACCOUNTOUTPUT']._serialized_end=638
  _globals['_LISTLINKEDACCOUNTSINPUT']._serialized_start=641
  _globals['_LISTLINKEDACCOUNTSINPUT']._serialized_end=860
  _globals['_LISTLINKEDACCOUNTSINPUT_FILTER']._serialized_start=760
  _globals['_LISTLINKEDACCOUNTSINPUT_FILTER']._serialized_end=860
  _globals['_LISTLINKEDACCOUNTSOUTPUT']._serialized_start=862
  _globals['_LISTLINKEDACCOUNTSOUTPUT']._serialized_end=946
  _globals['_LINKEDACCOUNTSERVICE']._serialized_start=949
  _globals['_LINKEDACCOUNTSERVICE']._serialized_end=1725
# @@protoc_insertion_point(module_scope)
