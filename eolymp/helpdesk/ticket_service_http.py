# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

import urllib.parse
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class TicketServiceClient:
    def __init__(self, transport, url="https://api.eolymp.com"):
        self.transport = transport
        self.url = url

    def CreateTicket(self, request, **kwargs):
        path = "/helpdesk/tickets"

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.CreateTicketOutput"),
            **kwargs,
        )

    def UpdateTicket(self, request, **kwargs):
        path = "/helpdesk/tickets/"+urllib.parse.quote(request.ticket_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.ticket_id = ""

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.UpdateTicketOutput"),
            **kwargs,
        )

    def DeleteTicket(self, request, **kwargs):
        path = "/helpdesk/tickets/"+urllib.parse.quote(request.ticket_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.ticket_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.DeleteTicketOutput"),
            **kwargs,
        )

    def DescribeTicket(self, request, **kwargs):
        path = "/helpdesk/tickets/"+urllib.parse.quote(request.ticket_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.ticket_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.DescribeTicketOutput"),
            **kwargs,
        )

    def ListTickets(self, request, **kwargs):
        path = "/helpdesk/tickets"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.ListTicketsOutput"),
            **kwargs,
        )

    def ApproveTicket(self, request, **kwargs):
        path = "/helpdesk/tickets/"+urllib.parse.quote(request.ticket_id)+"/approve"

        # Cleanup URL parameters to avoid any ambiguity
        request.ticket_id = ""

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.ApproveTicketOutput"),
            **kwargs,
        )

    def RejectTicket(self, request, **kwargs):
        path = "/helpdesk/tickets/"+urllib.parse.quote(request.ticket_id)+"/reject"

        # Cleanup URL parameters to avoid any ambiguity
        request.ticket_id = ""

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.RejectTicketOutput"),
            **kwargs,
        )

    def CloseTicket(self, request, **kwargs):
        path = "/helpdesk/tickets/"+urllib.parse.quote(request.ticket_id)+"/close"

        # Cleanup URL parameters to avoid any ambiguity
        request.ticket_id = ""

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.CloseTicketOutput"),
            **kwargs,
        )

    def AddComment(self, request, **kwargs):
        path = "/helpdesk/tickets/"+urllib.parse.quote(request.ticket_id)+"/comments"

        # Cleanup URL parameters to avoid any ambiguity
        request.ticket_id = ""

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.AddCommentOutput"),
            **kwargs,
        )

    def UpdateComment(self, request, **kwargs):
        path = "/helpdesk/tickets/"+urllib.parse.quote(request.ticket_id)+"/comments/"+urllib.parse.quote(request.comment_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.ticket_id = ""
        request.comment_id = ""

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.UpdateCommentOutput"),
            **kwargs,
        )

    def DeleteComment(self, request, **kwargs):
        path = "/helpdesk/tickets/"+urllib.parse.quote(request.ticket_id)+"/comments/"+urllib.parse.quote(request.comment_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.ticket_id = ""
        request.comment_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.DeleteCommentOutput"),
            **kwargs,
        )

    def ListComments(self, request, **kwargs):
        path = "/helpdesk/tickets/"+urllib.parse.quote(request.ticket_id)+"/comments"

        # Cleanup URL parameters to avoid any ambiguity
        request.ticket_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.ListCommentsOutput"),
            **kwargs,
        )

    def DescribeComment(self, request, **kwargs):
        path = "/helpdesk/tickets/"+urllib.parse.quote(request.ticket_id)+"/comments/"+urllib.parse.quote(request.comment_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.ticket_id = ""
        request.comment_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.DescribeCommentOutput"),
            **kwargs,
        )

    def UploadAttachment(self, request, **kwargs):
        path = "/helpdesk/attachments"

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.helpdesk.UploadAttachmentOutput"),
            **kwargs,
        )

