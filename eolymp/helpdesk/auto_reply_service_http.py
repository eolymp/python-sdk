# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

import urllib.parse
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class AutoReplyServiceClient:
    def __init__(self, transport, url="https://api.eolymp.com"):
        self.transport = transport
        self.url = url

    def CreateAutoReply(self, request, **kwargs):
        path = "/helpdesk/auto-replies"

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.CreateAutoReplyOutput"),
            **kwargs,
        )

    def UpdateAutoReply(self, request, **kwargs):
        path = "/helpdesk/auto-replies/"+urllib.parse.quote(request.reply_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.reply_id = ""

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.UpdateAutoReplyOutput"),
            **kwargs,
        )

    def DeleteAutoReply(self, request, **kwargs):
        path = "/helpdesk/auto-replies/"+urllib.parse.quote(request.reply_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.reply_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.DeleteAutoReplyOutput"),
            **kwargs,
        )

    def ListAutoReplies(self, request, **kwargs):
        path = "/helpdesk/auto-replies"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.ListAutoRepliesOutput"),
            **kwargs,
        )

    def DescribeAutoReply(self, request, **kwargs):
        path = "/helpdesk/auto-replies/"+urllib.parse.quote(request.reply_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.reply_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.DescribeAutoReplyOutput"),
            **kwargs,
        )

