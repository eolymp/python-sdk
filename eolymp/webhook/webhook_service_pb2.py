# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/webhook/webhook_service.proto
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
from eolymp.webhook import webhook_pb2 as eolymp_dot_webhook_dot_webhook__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$eolymp/webhook/webhook_service.proto\x12\x0e\x65olymp.webhook\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a\x1c\x65olymp/webhook/webhook.proto\">\n\x12\x43reateWebhookInput\x12(\n\x07webhook\x18\x01 \x01(\x0b\x32\x17.eolymp.webhook.Webhook\")\n\x13\x43reateWebhookOutput\x12\x12\n\nwebhook_id\x18\x01 \x01(\t\"\x80\x01\n\x12UpdateWebhookInput\x12,\n\x05patch\x18\x01 \x03(\x0e\x32\x1d.eolymp.webhook.Webhook.Patch\x12\x12\n\nwebhook_id\x18\x02 \x01(\t\x12(\n\x07webhook\x18\x03 \x01(\x0b\x32\x17.eolymp.webhook.Webhook\"\x15\n\x13UpdateWebhookOutput\"(\n\x12\x44\x65leteWebhookInput\x12\x12\n\nwebhook_id\x18\x01 \x01(\t\"\x15\n\x13\x44\x65leteWebhookOutput\"*\n\x14\x44\x65scribeWebhookInput\x12\x12\n\nwebhook_id\x18\x01 \x01(\t\"A\n\x15\x44\x65scribeWebhookOutput\x12(\n\x07webhook\x18\x01 \x01(\x0b\x32\x17.eolymp.webhook.Webhook\"1\n\x11ListWebhooksInput\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12\x0e\n\x06offset\x18\n \x01(\x05\"K\n\x12ListWebhooksOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12&\n\x05items\x18\x02 \x03(\x0b\x32\x17.eolymp.webhook.Webhook\"&\n\x10TestWebhookInput\x12\x12\n\nwebhook_id\x18\x01 \x01(\t\"5\n\x11TestWebhookOutput\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x10\n\x08response\x18\x02 \x01(\t2\xe0\x07\n\x0eWebhookService\x12\x97\x01\n\rCreateWebhook\x12\".eolymp.webhook.CreateWebhookInput\x1a#.eolymp.webhook.CreateWebhookOutput\"=\x82\xe3\n\x19\x8a\xe3\n\x15webhook:webhook:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x0b\"\t/webhooks\x12\xa4\x01\n\rUpdateWebhook\x12\".eolymp.webhook.UpdateWebhookInput\x1a#.eolymp.webhook.UpdateWebhookOutput\"J\x82\xe3\n\x19\x8a\xe3\n\x15webhook:webhook:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x18\"\x16/webhooks/{webhook_id}\x12\xa4\x01\n\rDeleteWebhook\x12\".eolymp.webhook.DeleteWebhookInput\x1a#.eolymp.webhook.DeleteWebhookOutput\"J\x82\xe3\n\x19\x8a\xe3\n\x15webhook:webhook:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x18*\x16/webhooks/{webhook_id}\x12\xa9\x01\n\x0f\x44\x65scribeWebhook\x12$.eolymp.webhook.DescribeWebhookInput\x1a%.eolymp.webhook.DescribeWebhookOutput\"I\x82\xe3\n\x18\x8a\xe3\n\x14webhook:webhook:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x18\x12\x16/webhooks/{webhook_id}\x12\x93\x01\n\x0cListWebhooks\x12!.eolymp.webhook.ListWebhooksInput\x1a\".eolymp.webhook.ListWebhooksOutput\"<\x82\xe3\n\x18\x8a\xe3\n\x14webhook:webhook:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x0b\x12\t/webhooks\x12\xa3\x01\n\x0bTestWebhook\x12 .eolymp.webhook.TestWebhookInput\x1a!.eolymp.webhook.TestWebhookOutput\"O\x82\xe3\n\x19\x8a\xe3\n\x15webhook:webhook:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x1d\"\x1b/webhooks/{webhook_id}/testB1Z/github.com/eolymp/go-sdk/eolymp/webhook;webhookb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.webhook.webhook_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z/github.com/eolymp/go-sdk/eolymp/webhook;webhook'
  _WEBHOOKSERVICE.methods_by_name['CreateWebhook']._options = None
  _WEBHOOKSERVICE.methods_by_name['CreateWebhook']._serialized_options = b'\202\343\n\031\212\343\n\025webhook:webhook:write\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\013\"\t/webhooks'
  _WEBHOOKSERVICE.methods_by_name['UpdateWebhook']._options = None
  _WEBHOOKSERVICE.methods_by_name['UpdateWebhook']._serialized_options = b'\202\343\n\031\212\343\n\025webhook:webhook:write\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\030\"\026/webhooks/{webhook_id}'
  _WEBHOOKSERVICE.methods_by_name['DeleteWebhook']._options = None
  _WEBHOOKSERVICE.methods_by_name['DeleteWebhook']._serialized_options = b'\202\343\n\031\212\343\n\025webhook:webhook:write\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\030*\026/webhooks/{webhook_id}'
  _WEBHOOKSERVICE.methods_by_name['DescribeWebhook']._options = None
  _WEBHOOKSERVICE.methods_by_name['DescribeWebhook']._serialized_options = b'\202\343\n\030\212\343\n\024webhook:webhook:read\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\030\022\026/webhooks/{webhook_id}'
  _WEBHOOKSERVICE.methods_by_name['ListWebhooks']._options = None
  _WEBHOOKSERVICE.methods_by_name['ListWebhooks']._serialized_options = b'\202\343\n\030\212\343\n\024webhook:webhook:read\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\013\022\t/webhooks'
  _WEBHOOKSERVICE.methods_by_name['TestWebhook']._options = None
  _WEBHOOKSERVICE.methods_by_name['TestWebhook']._serialized_options = b'\202\343\n\031\212\343\n\025webhook:webhook:write\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\035\"\033/webhooks/{webhook_id}/test'
  _CREATEWEBHOOKINPUT._serialized_start=185
  _CREATEWEBHOOKINPUT._serialized_end=247
  _CREATEWEBHOOKOUTPUT._serialized_start=249
  _CREATEWEBHOOKOUTPUT._serialized_end=290
  _UPDATEWEBHOOKINPUT._serialized_start=293
  _UPDATEWEBHOOKINPUT._serialized_end=421
  _UPDATEWEBHOOKOUTPUT._serialized_start=423
  _UPDATEWEBHOOKOUTPUT._serialized_end=444
  _DELETEWEBHOOKINPUT._serialized_start=446
  _DELETEWEBHOOKINPUT._serialized_end=486
  _DELETEWEBHOOKOUTPUT._serialized_start=488
  _DELETEWEBHOOKOUTPUT._serialized_end=509
  _DESCRIBEWEBHOOKINPUT._serialized_start=511
  _DESCRIBEWEBHOOKINPUT._serialized_end=553
  _DESCRIBEWEBHOOKOUTPUT._serialized_start=555
  _DESCRIBEWEBHOOKOUTPUT._serialized_end=620
  _LISTWEBHOOKSINPUT._serialized_start=622
  _LISTWEBHOOKSINPUT._serialized_end=671
  _LISTWEBHOOKSOUTPUT._serialized_start=673
  _LISTWEBHOOKSOUTPUT._serialized_end=748
  _TESTWEBHOOKINPUT._serialized_start=750
  _TESTWEBHOOKINPUT._serialized_end=788
  _TESTWEBHOOKOUTPUT._serialized_start=790
  _TESTWEBHOOKOUTPUT._serialized_end=843
  _WEBHOOKSERVICE._serialized_start=846
  _WEBHOOKSERVICE._serialized_end=1838
# @@protoc_insertion_point(module_scope)