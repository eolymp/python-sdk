# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

import urllib.parse
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class RecipientServiceClient:
    def __init__(self, transport, url="https://api.eolymp.com"):
        self.transport = transport
        self.url = url

    def DescribeRecipient(self, request, **kwargs):
        path = "/recipients/"+urllib.parse.quote(request.recipient_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.recipient_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.newsletter.DescribeRecipientOutput"),
            **kwargs,
        )

    def ImportRecipients(self, request, **kwargs):
        path = "/imports/recipients"

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.newsletter.ImportRecipientsOutput"),
            **kwargs,
        )

    def ListRecipients(self, request, **kwargs):
        path = "/recipients"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.newsletter.ListRecipientsOutput"),
            **kwargs,
        )

    def CreateRecipient(self, request, **kwargs):
        path = "/recipients"

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.newsletter.CreateRecipientOutput"),
            **kwargs,
        )

    def RemoveRecipient(self, request, **kwargs):
        path = "/recipients/"+urllib.parse.quote(request.recipient_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.recipient_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.newsletter.RemoveRecipientOutput"),
            **kwargs,
        )

