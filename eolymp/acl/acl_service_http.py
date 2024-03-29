# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

import urllib.parse
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class AclServiceClient:
    def __init__(self, transport, url="https://api.eolymp.com"):
        self.transport = transport
        self.url = url

    def GrantPermission(self, request, **kwargs):
        path = "/acl/"+urllib.parse.quote(request.user_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.user_id = ""

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.acl.GrantPermissionOutput"),
            **kwargs,
        )

    def RevokePermission(self, request, **kwargs):
        path = "/acl/"+urllib.parse.quote(request.user_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.user_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.acl.RevokePermissionOutput"),
            **kwargs,
        )

    def DescribePermission(self, request, **kwargs):
        path = "/acl/"+urllib.parse.quote(request.user_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.user_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.acl.DescribePermissionOutput"),
            **kwargs,
        )

    def ListPermissions(self, request, **kwargs):
        path = "/acl"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.acl.ListPermissionsOutput"),
            **kwargs,
        )

    def IntrospectPermission(self, request, **kwargs):
        path = "/whoami"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.acl.IntrospectPermissionOutput"),
            **kwargs,
        )

