# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eolymp/helpdesk/support.proto
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
from eolymp.helpdesk import auto_reply_pb2 as eolymp_dot_helpdesk_dot_auto__reply__pb2
from eolymp.helpdesk import ticket_pb2 as eolymp_dot_helpdesk_dot_ticket__pb2
from eolymp.wellknown import expression_pb2 as eolymp_dot_wellknown_dot_expression__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x65olymp/helpdesk/support.proto\x12\x0f\x65olymp.helpdesk\x1a\x1d\x65olymp/annotations/http.proto\x1a\"eolymp/annotations/ratelimit.proto\x1a\x1e\x65olymp/annotations/scope.proto\x1a eolymp/helpdesk/auto_reply.proto\x1a\x1c\x65olymp/helpdesk/ticket.proto\x1a!eolymp/wellknown/expression.proto\"M\n\x11\x43reateTicketInput\x12\'\n\x06ticket\x18\x01 \x01(\x0b\x32\x17.eolymp.helpdesk.Ticket\x12\x0f\n\x07\x63\x61ptcha\x18\x02 \x01(\t\"\'\n\x12\x43reateTicketOutput\x12\x11\n\tticket_id\x18\x01 \x01(\t\"O\n\x11UpdateTicketInput\x12\x11\n\tticket_id\x18\x01 \x01(\t\x12\'\n\x06ticket\x18\x02 \x01(\x0b\x32\x17.eolymp.helpdesk.Ticket\"\x14\n\x12UpdateTicketOutput\"&\n\x11\x44\x65leteTicketInput\x12\x11\n\tticket_id\x18\x01 \x01(\t\"\x14\n\x12\x44\x65leteTicketOutput\"8\n\x13\x44\x65scribeTicketInput\x12\x11\n\tticket_id\x18\x01 \x01(\t\x12\x0e\n\x06render\x18\x02 \x01(\x08\"?\n\x14\x44\x65scribeTicketOutput\x12\'\n\x06ticket\x18\x01 \x01(\x0b\x32\x17.eolymp.helpdesk.Ticket\"\xb2\x04\n\x10ListTicketsInput\x12\x0e\n\x06render\x18\x01 \x01(\x08\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12\x39\n\x07\x66ilters\x18( \x01(\x0b\x32(.eolymp.helpdesk.ListTicketsInput.Filter\x1a\xb4\x03\n\x06\x46ilter\x12\r\n\x05query\x18\x01 \x01(\t\x12*\n\x02id\x18\x02 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12/\n\x07user_id\x18\x03 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x34\n\nuser_email\x18\x04 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\x12\x30\n\x06status\x18\x05 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\x12.\n\x04type\x18\x06 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\x12\x39\n\ncreated_at\x18\x07 \x03(\x0b\x32%.eolymp.wellknown.ExpressionTimestamp\x12\x39\n\nupdated_at\x18\x08 \x03(\x0b\x32%.eolymp.wellknown.ExpressionTimestamp\x12\x30\n\x06locale\x18\t \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\"J\n\x11ListTicketsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12&\n\x05items\x18\x02 \x03(\x0b\x32\x17.eolymp.helpdesk.Ticket\"8\n\x12\x41pproveTicketInput\x12\x11\n\tticket_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\"\x15\n\x13\x41pproveTicketOutput\"7\n\x11RejectTicketInput\x12\x11\n\tticket_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\"\x14\n\x12RejectTicketOutput\"6\n\x10\x43loseTicketInput\x12\x11\n\tticket_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63omment\x18\x02 \x01(\t\"\x13\n\x11\x43loseTicketOutput\"V\n\x0f\x41\x64\x64\x43ommentInput\x12\x11\n\tticket_id\x18\x01 \x01(\t\x12\x30\n\x07\x63omment\x18\x02 \x01(\x0b\x32\x1f.eolymp.helpdesk.Ticket.Comment\"&\n\x10\x41\x64\x64\x43ommentOutput\x12\x12\n\ncomment_id\x18\x01 \x01(\t\"m\n\x12UpdateCommentInput\x12\x11\n\tticket_id\x18\x01 \x01(\t\x12\x12\n\ncomment_id\x18\x02 \x01(\t\x12\x30\n\x07\x63omment\x18\x03 \x01(\x0b\x32\x1f.eolymp.helpdesk.Ticket.Comment\"\x15\n\x13UpdateCommentOutput\";\n\x12\x44\x65leteCommentInput\x12\x11\n\tticket_id\x18\x01 \x01(\t\x12\x12\n\ncomment_id\x18\x02 \x01(\t\"\x15\n\x13\x44\x65leteCommentOutput\"T\n\x11ListCommentsInput\x12\x11\n\tticket_id\x18\x01 \x01(\t\x12\x0e\n\x06render\x18\x02 \x01(\x08\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\"S\n\x12ListCommentsOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12.\n\x05items\x18\x02 \x03(\x0b\x32\x1f.eolymp.helpdesk.Ticket.Comment\"M\n\x14\x44\x65scribeCommentInput\x12\x11\n\tticket_id\x18\x01 \x01(\t\x12\x12\n\ncomment_id\x18\x02 \x01(\t\x12\x0e\n\x06render\x18\x03 \x01(\x08\"I\n\x15\x44\x65scribeCommentOutput\x12\x30\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x1f.eolymp.helpdesk.Ticket.Comment\"A\n\x14\x43reateAutoReplyInput\x12)\n\x05reply\x18\x01 \x01(\x0b\x32\x1a.eolymp.helpdesk.AutoReply\")\n\x15\x43reateAutoReplyOutput\x12\x10\n\x08reply_id\x18\x01 \x01(\t\"S\n\x14UpdateAutoReplyInput\x12\x10\n\x08reply_id\x18\x01 \x01(\t\x12)\n\x05reply\x18\x02 \x01(\x0b\x32\x1a.eolymp.helpdesk.AutoReply\"\x17\n\x15UpdateAutoReplyOutput\"(\n\x14\x44\x65leteAutoReplyInput\x12\x10\n\x08reply_id\x18\x01 \x01(\t\"\x17\n\x15\x44\x65leteAutoReplyOutput\"\xfa\x01\n\x14ListAutoRepliesInput\x12\x0e\n\x06render\x18\x01 \x01(\x08\x12\x0e\n\x06offset\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12=\n\x07\x66ilters\x18( \x01(\x0b\x32,.eolymp.helpdesk.ListAutoRepliesInput.Filter\x1au\n\x06\x46ilter\x12\r\n\x05query\x18\x01 \x01(\t\x12*\n\x02id\x18\x02 \x03(\x0b\x32\x1e.eolymp.wellknown.ExpressionID\x12\x30\n\x06locale\x18\x03 \x03(\x0b\x32 .eolymp.wellknown.ExpressionEnum\"Q\n\x15ListAutoRepliesOutput\x12\r\n\x05total\x18\x01 \x01(\x05\x12)\n\x05items\x18\x02 \x03(\x0b\x32\x1a.eolymp.helpdesk.AutoReply\":\n\x16\x44\x65scribeAutoReplyInput\x12\x10\n\x08reply_id\x18\x01 \x01(\t\x12\x0e\n\x06render\x18\x02 \x01(\x08\"D\n\x17\x44\x65scribeAutoReplyOutput\x12)\n\x05reply\x18\x01 \x01(\x0b\x32\x1a.eolymp.helpdesk.AutoReply2\xcc\x19\n\x07Support\x12\x9e\x01\n\x0c\x43reateTicket\x12\".eolymp.helpdesk.CreateTicketInput\x1a#.eolymp.helpdesk.CreateTicketOutput\"E\x82\xe3\n\x19\x8a\xe3\n\x15helpdesk:ticket:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x13\"\x11/helpdesk/tickets\x12\xaa\x01\n\x0cUpdateTicket\x12\".eolymp.helpdesk.UpdateTicketInput\x1a#.eolymp.helpdesk.UpdateTicketOutput\"Q\x82\xe3\n\x19\x8a\xe3\n\x15helpdesk:ticket:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x1f\x1a\x1d/helpdesk/tickets/{ticket_id}\x12\xaa\x01\n\x0c\x44\x65leteTicket\x12\".eolymp.helpdesk.DeleteTicketInput\x1a#.eolymp.helpdesk.DeleteTicketOutput\"Q\x82\xe3\n\x19\x8a\xe3\n\x15helpdesk:ticket:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x1f*\x1d/helpdesk/tickets/{ticket_id}\x12\xaf\x01\n\x0e\x44\x65scribeTicket\x12$.eolymp.helpdesk.DescribeTicketInput\x1a%.eolymp.helpdesk.DescribeTicketOutput\"P\x82\xe3\n\x18\x8a\xe3\n\x14helpdesk:ticket:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x1f\x12\x1d/helpdesk/tickets/{ticket_id}\x12\x9a\x01\n\x0bListTickets\x12!.eolymp.helpdesk.ListTicketsInput\x1a\".eolymp.helpdesk.ListTicketsOutput\"D\x82\xe3\n\x18\x8a\xe3\n\x14helpdesk:ticket:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x13\x12\x11/helpdesk/tickets\x12\xb5\x01\n\rApproveTicket\x12#.eolymp.helpdesk.ApproveTicketInput\x1a$.eolymp.helpdesk.ApproveTicketOutput\"Y\x82\xe3\n\x19\x8a\xe3\n\x15helpdesk:ticket:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\'\"%/helpdesk/tickets/{ticket_id}/approve\x12\xb1\x01\n\x0cRejectTicket\x12\".eolymp.helpdesk.RejectTicketInput\x1a#.eolymp.helpdesk.RejectTicketOutput\"X\x82\xe3\n\x19\x8a\xe3\n\x15helpdesk:ticket:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02&\"$/helpdesk/tickets/{ticket_id}/reject\x12\xad\x01\n\x0b\x43loseTicket\x12!.eolymp.helpdesk.CloseTicketInput\x1a\".eolymp.helpdesk.CloseTicketOutput\"W\x82\xe3\n\x19\x8a\xe3\n\x15helpdesk:ticket:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02%\"#/helpdesk/tickets/{ticket_id}/close\x12\xad\x01\n\nAddComment\x12 .eolymp.helpdesk.AddCommentInput\x1a!.eolymp.helpdesk.AddCommentOutput\"Z\x82\xe3\n\x19\x8a\xe3\n\x15helpdesk:ticket:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02(\"&/helpdesk/tickets/{ticket_id}/comments\x12\xc3\x01\n\rUpdateComment\x12#.eolymp.helpdesk.UpdateCommentInput\x1a$.eolymp.helpdesk.UpdateCommentOutput\"g\x82\xe3\n\x19\x8a\xe3\n\x15helpdesk:ticket:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x35\x1a\x33/helpdesk/tickets/{ticket_id}/comments/{comment_id}\x12\xc3\x01\n\rDeleteComment\x12#.eolymp.helpdesk.DeleteCommentInput\x1a$.eolymp.helpdesk.DeleteCommentOutput\"g\x82\xe3\n\x19\x8a\xe3\n\x15helpdesk:ticket:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x35*3/helpdesk/tickets/{ticket_id}/comments/{comment_id}\x12\xb2\x01\n\x0cListComments\x12\".eolymp.helpdesk.ListCommentsInput\x1a#.eolymp.helpdesk.ListCommentsOutput\"Y\x82\xe3\n\x18\x8a\xe3\n\x14helpdesk:ticket:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02(\x12&/helpdesk/tickets/{ticket_id}/comments\x12\xc9\x01\n\x0f\x44\x65scribeComment\x12%.eolymp.helpdesk.DescribeCommentInput\x1a&.eolymp.helpdesk.DescribeCommentOutput\"g\x82\xe3\n\x19\x8a\xe3\n\x15helpdesk:ticket:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n2\x82\xd3\xe4\x93\x02\x35\x12\x33/helpdesk/tickets/{ticket_id}/comments/{comment_id}\x12\xaf\x01\n\x0f\x43reateAutoReply\x12%.eolymp.helpdesk.CreateAutoReplyInput\x1a&.eolymp.helpdesk.CreateAutoReplyOutput\"M\x82\xe3\n\x1d\x8a\xe3\n\x19helpdesk:auto-reply:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\x17\"\x15/helpdesk/autoreplies\x12\xba\x01\n\x0fUpdateAutoReply\x12%.eolymp.helpdesk.UpdateAutoReplyInput\x1a&.eolymp.helpdesk.UpdateAutoReplyOutput\"X\x82\xe3\n\x1d\x8a\xe3\n\x19helpdesk:auto-reply:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\"\x1a /helpdesk/autoreplies/{reply_id}\x12\xba\x01\n\x0f\x44\x65leteAutoReply\x12%.eolymp.helpdesk.DeleteAutoReplyInput\x1a&.eolymp.helpdesk.DeleteAutoReplyOutput\"X\x82\xe3\n\x1d\x8a\xe3\n\x19helpdesk:auto-reply:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\x00@\xf8\xe2\n\n\x82\xd3\xe4\x93\x02\"* /helpdesk/autoreplies/{reply_id}\x12\xae\x01\n\x0fListAutoReplies\x12%.eolymp.helpdesk.ListAutoRepliesInput\x1a&.eolymp.helpdesk.ListAutoRepliesOutput\"L\x82\xe3\n\x1c\x8a\xe3\n\x18helpdesk:auto-reply:read\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n\x14\x82\xd3\xe4\x93\x02\x17\x12\x15/helpdesk/autoreplies\x12\xc0\x01\n\x11\x44\x65scribeAutoReply\x12\'.eolymp.helpdesk.DescribeAutoReplyInput\x1a(.eolymp.helpdesk.DescribeAutoReplyOutput\"X\x82\xe3\n\x1d\x8a\xe3\n\x19helpdesk:auto-reply:write\xea\xe2\n\x0b\xf5\xe2\n\x00\x00\xa0@\xf8\xe2\n2\x82\xd3\xe4\x93\x02\"\x12 /helpdesk/autoreplies/{reply_id}B3Z1github.com/eolymp/go-sdk/eolymp/helpdesk;helpdeskb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'eolymp.helpdesk.support_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z1github.com/eolymp/go-sdk/eolymp/helpdesk;helpdesk'
  _SUPPORT.methods_by_name['CreateTicket']._options = None
  _SUPPORT.methods_by_name['CreateTicket']._serialized_options = b'\202\343\n\031\212\343\n\025helpdesk:ticket:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\023\"\021/helpdesk/tickets'
  _SUPPORT.methods_by_name['UpdateTicket']._options = None
  _SUPPORT.methods_by_name['UpdateTicket']._serialized_options = b'\202\343\n\031\212\343\n\025helpdesk:ticket:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\037\032\035/helpdesk/tickets/{ticket_id}'
  _SUPPORT.methods_by_name['DeleteTicket']._options = None
  _SUPPORT.methods_by_name['DeleteTicket']._serialized_options = b'\202\343\n\031\212\343\n\025helpdesk:ticket:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\037*\035/helpdesk/tickets/{ticket_id}'
  _SUPPORT.methods_by_name['DescribeTicket']._options = None
  _SUPPORT.methods_by_name['DescribeTicket']._serialized_options = b'\202\343\n\030\212\343\n\024helpdesk:ticket:read\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\037\022\035/helpdesk/tickets/{ticket_id}'
  _SUPPORT.methods_by_name['ListTickets']._options = None
  _SUPPORT.methods_by_name['ListTickets']._serialized_options = b'\202\343\n\030\212\343\n\024helpdesk:ticket:read\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\023\022\021/helpdesk/tickets'
  _SUPPORT.methods_by_name['ApproveTicket']._options = None
  _SUPPORT.methods_by_name['ApproveTicket']._serialized_options = b'\202\343\n\031\212\343\n\025helpdesk:ticket:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\'\"%/helpdesk/tickets/{ticket_id}/approve'
  _SUPPORT.methods_by_name['RejectTicket']._options = None
  _SUPPORT.methods_by_name['RejectTicket']._serialized_options = b'\202\343\n\031\212\343\n\025helpdesk:ticket:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002&\"$/helpdesk/tickets/{ticket_id}/reject'
  _SUPPORT.methods_by_name['CloseTicket']._options = None
  _SUPPORT.methods_by_name['CloseTicket']._serialized_options = b'\202\343\n\031\212\343\n\025helpdesk:ticket:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002%\"#/helpdesk/tickets/{ticket_id}/close'
  _SUPPORT.methods_by_name['AddComment']._options = None
  _SUPPORT.methods_by_name['AddComment']._serialized_options = b'\202\343\n\031\212\343\n\025helpdesk:ticket:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002(\"&/helpdesk/tickets/{ticket_id}/comments'
  _SUPPORT.methods_by_name['UpdateComment']._options = None
  _SUPPORT.methods_by_name['UpdateComment']._serialized_options = b'\202\343\n\031\212\343\n\025helpdesk:ticket:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\0025\0323/helpdesk/tickets/{ticket_id}/comments/{comment_id}'
  _SUPPORT.methods_by_name['DeleteComment']._options = None
  _SUPPORT.methods_by_name['DeleteComment']._serialized_options = b'\202\343\n\031\212\343\n\025helpdesk:ticket:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\0025*3/helpdesk/tickets/{ticket_id}/comments/{comment_id}'
  _SUPPORT.methods_by_name['ListComments']._options = None
  _SUPPORT.methods_by_name['ListComments']._serialized_options = b'\202\343\n\030\212\343\n\024helpdesk:ticket:read\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002(\022&/helpdesk/tickets/{ticket_id}/comments'
  _SUPPORT.methods_by_name['DescribeComment']._options = None
  _SUPPORT.methods_by_name['DescribeComment']._serialized_options = b'\202\343\n\031\212\343\n\025helpdesk:ticket:write\352\342\n\013\365\342\n\000\000\240@\370\342\n2\202\323\344\223\0025\0223/helpdesk/tickets/{ticket_id}/comments/{comment_id}'
  _SUPPORT.methods_by_name['CreateAutoReply']._options = None
  _SUPPORT.methods_by_name['CreateAutoReply']._serialized_options = b'\202\343\n\035\212\343\n\031helpdesk:auto-reply:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\027\"\025/helpdesk/autoreplies'
  _SUPPORT.methods_by_name['UpdateAutoReply']._options = None
  _SUPPORT.methods_by_name['UpdateAutoReply']._serialized_options = b'\202\343\n\035\212\343\n\031helpdesk:auto-reply:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\"\032 /helpdesk/autoreplies/{reply_id}'
  _SUPPORT.methods_by_name['DeleteAutoReply']._options = None
  _SUPPORT.methods_by_name['DeleteAutoReply']._serialized_options = b'\202\343\n\035\212\343\n\031helpdesk:auto-reply:write\352\342\n\013\365\342\n\000\000\000@\370\342\n\n\202\323\344\223\002\"* /helpdesk/autoreplies/{reply_id}'
  _SUPPORT.methods_by_name['ListAutoReplies']._options = None
  _SUPPORT.methods_by_name['ListAutoReplies']._serialized_options = b'\202\343\n\034\212\343\n\030helpdesk:auto-reply:read\352\342\n\013\365\342\n\000\000\240@\370\342\n\024\202\323\344\223\002\027\022\025/helpdesk/autoreplies'
  _SUPPORT.methods_by_name['DescribeAutoReply']._options = None
  _SUPPORT.methods_by_name['DescribeAutoReply']._serialized_options = b'\202\343\n\035\212\343\n\031helpdesk:auto-reply:write\352\342\n\013\365\342\n\000\000\240@\370\342\n2\202\323\344\223\002\"\022 /helpdesk/autoreplies/{reply_id}'
  _CREATETICKETINPUT._serialized_start=248
  _CREATETICKETINPUT._serialized_end=325
  _CREATETICKETOUTPUT._serialized_start=327
  _CREATETICKETOUTPUT._serialized_end=366
  _UPDATETICKETINPUT._serialized_start=368
  _UPDATETICKETINPUT._serialized_end=447
  _UPDATETICKETOUTPUT._serialized_start=449
  _UPDATETICKETOUTPUT._serialized_end=469
  _DELETETICKETINPUT._serialized_start=471
  _DELETETICKETINPUT._serialized_end=509
  _DELETETICKETOUTPUT._serialized_start=511
  _DELETETICKETOUTPUT._serialized_end=531
  _DESCRIBETICKETINPUT._serialized_start=533
  _DESCRIBETICKETINPUT._serialized_end=589
  _DESCRIBETICKETOUTPUT._serialized_start=591
  _DESCRIBETICKETOUTPUT._serialized_end=654
  _LISTTICKETSINPUT._serialized_start=657
  _LISTTICKETSINPUT._serialized_end=1219
  _LISTTICKETSINPUT_FILTER._serialized_start=783
  _LISTTICKETSINPUT_FILTER._serialized_end=1219
  _LISTTICKETSOUTPUT._serialized_start=1221
  _LISTTICKETSOUTPUT._serialized_end=1295
  _APPROVETICKETINPUT._serialized_start=1297
  _APPROVETICKETINPUT._serialized_end=1353
  _APPROVETICKETOUTPUT._serialized_start=1355
  _APPROVETICKETOUTPUT._serialized_end=1376
  _REJECTTICKETINPUT._serialized_start=1378
  _REJECTTICKETINPUT._serialized_end=1433
  _REJECTTICKETOUTPUT._serialized_start=1435
  _REJECTTICKETOUTPUT._serialized_end=1455
  _CLOSETICKETINPUT._serialized_start=1457
  _CLOSETICKETINPUT._serialized_end=1511
  _CLOSETICKETOUTPUT._serialized_start=1513
  _CLOSETICKETOUTPUT._serialized_end=1532
  _ADDCOMMENTINPUT._serialized_start=1534
  _ADDCOMMENTINPUT._serialized_end=1620
  _ADDCOMMENTOUTPUT._serialized_start=1622
  _ADDCOMMENTOUTPUT._serialized_end=1660
  _UPDATECOMMENTINPUT._serialized_start=1662
  _UPDATECOMMENTINPUT._serialized_end=1771
  _UPDATECOMMENTOUTPUT._serialized_start=1773
  _UPDATECOMMENTOUTPUT._serialized_end=1794
  _DELETECOMMENTINPUT._serialized_start=1796
  _DELETECOMMENTINPUT._serialized_end=1855
  _DELETECOMMENTOUTPUT._serialized_start=1857
  _DELETECOMMENTOUTPUT._serialized_end=1878
  _LISTCOMMENTSINPUT._serialized_start=1880
  _LISTCOMMENTSINPUT._serialized_end=1964
  _LISTCOMMENTSOUTPUT._serialized_start=1966
  _LISTCOMMENTSOUTPUT._serialized_end=2049
  _DESCRIBECOMMENTINPUT._serialized_start=2051
  _DESCRIBECOMMENTINPUT._serialized_end=2128
  _DESCRIBECOMMENTOUTPUT._serialized_start=2130
  _DESCRIBECOMMENTOUTPUT._serialized_end=2203
  _CREATEAUTOREPLYINPUT._serialized_start=2205
  _CREATEAUTOREPLYINPUT._serialized_end=2270
  _CREATEAUTOREPLYOUTPUT._serialized_start=2272
  _CREATEAUTOREPLYOUTPUT._serialized_end=2313
  _UPDATEAUTOREPLYINPUT._serialized_start=2315
  _UPDATEAUTOREPLYINPUT._serialized_end=2398
  _UPDATEAUTOREPLYOUTPUT._serialized_start=2400
  _UPDATEAUTOREPLYOUTPUT._serialized_end=2423
  _DELETEAUTOREPLYINPUT._serialized_start=2425
  _DELETEAUTOREPLYINPUT._serialized_end=2465
  _DELETEAUTOREPLYOUTPUT._serialized_start=2467
  _DELETEAUTOREPLYOUTPUT._serialized_end=2490
  _LISTAUTOREPLIESINPUT._serialized_start=2493
  _LISTAUTOREPLIESINPUT._serialized_end=2743
  _LISTAUTOREPLIESINPUT_FILTER._serialized_start=2626
  _LISTAUTOREPLIESINPUT_FILTER._serialized_end=2743
  _LISTAUTOREPLIESOUTPUT._serialized_start=2745
  _LISTAUTOREPLIESOUTPUT._serialized_end=2826
  _DESCRIBEAUTOREPLYINPUT._serialized_start=2828
  _DESCRIBEAUTOREPLYINPUT._serialized_end=2886
  _DESCRIBEAUTOREPLYOUTPUT._serialized_start=2888
  _DESCRIBEAUTOREPLYOUTPUT._serialized_end=2956
  _SUPPORT._serialized_start=2959
  _SUPPORT._serialized_end=6235
# @@protoc_insertion_point(module_scope)
