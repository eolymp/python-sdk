# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

import urllib.parse
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class MemberServiceClient:
    def __init__(self, transport, url="https://api.eolymp.com"):
        self.transport = transport
        self.url = url

    def CreateMember(self, request, **kwargs):
        path = "/members"

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.community.CreateMemberOutput"),
            **kwargs,
        )

    def UpdateMember(self, request, **kwargs):
        path = "/members/"+urllib.parse.quote(request.member_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.member_id = ""

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.community.UpdateMemberOutput"),
            **kwargs,
        )

    def DeleteMember(self, request, **kwargs):
        path = "/members/"+urllib.parse.quote(request.member_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.member_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.community.DeleteMemberOutput"),
            **kwargs,
        )

    def RestoreMember(self, request, **kwargs):
        path = "/members/"+urllib.parse.quote(request.member_id)+"/restore"

        # Cleanup URL parameters to avoid any ambiguity
        request.member_id = ""

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.community.RestoreMemberOutput"),
            **kwargs,
        )

    def DescribeMember(self, request, **kwargs):
        path = "/members/"+urllib.parse.quote(request.member_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.member_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.community.DescribeMemberOutput"),
            **kwargs,
        )

    def ListMembers(self, request, **kwargs):
        path = "/members"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.community.ListMembersOutput"),
            **kwargs,
        )

    def AssignMember(self, request, **kwargs):
        path = "/members/"+urllib.parse.quote(request.team_id)+"/users/"+urllib.parse.quote(request.member_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.team_id = ""
        request.member_id = ""

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.community.AssignMemberOutput"),
            **kwargs,
        )

    def UnassignMember(self, request, **kwargs):
        path = "/members/"+urllib.parse.quote(request.team_id)+"/users/"+urllib.parse.quote(request.member_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.team_id = ""
        request.member_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.community.UnassignMemberOutput"),
            **kwargs,
        )
