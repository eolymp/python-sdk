# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

import urllib.parse
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class PostTypeServiceClient:
    def __init__(self, transport, url="https://api.eolymp.com"):
        self.transport = transport
        self.url = url

    def DescribePostType(self, request, **kwargs):
        path = "/post-types/"+urllib.parse.quote(request.type_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.type_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.discussion.DescribePostTypeOutput"),
            **kwargs,
        )

    def ListPostTypes(self, request, **kwargs):
        path = "/post-types"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.discussion.ListPostTypesOutput"),
            **kwargs,
        )

    def CreatePostType(self, request, **kwargs):
        path = "/post-types"

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.discussion.CreatePostTypeOutput"),
            **kwargs,
        )

    def UpdatePostType(self, request, **kwargs):
        path = "/post-types/"+urllib.parse.quote(request.type_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.type_id = ""

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.discussion.UpdatePostTypeOutput"),
            **kwargs,
        )

    def DeletePostType(self, request, **kwargs):
        path = "/post-types/"+urllib.parse.quote(request.type_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.type_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.discussion.DeletePostTypeOutput"),
            **kwargs,
        )
