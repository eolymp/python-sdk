# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

import urllib.parse
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class PostServiceClient:
    def __init__(self, transport, url="https://api.eolymp.com"):
        self.transport = transport
        self.url = url

    def DescribePost(self, request, **kwargs):
        path = "/posts/"+urllib.parse.quote(request.post_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.post_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.discussion.DescribePostOutput"),
            **kwargs,
        )

    def ListPosts(self, request, **kwargs):
        path = "/posts"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.discussion.ListPostsOutput"),
            **kwargs,
        )

    def CreatePost(self, request, **kwargs):
        path = "/posts"

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.discussion.CreatePostOutput"),
            **kwargs,
        )

    def UpdatePost(self, request, **kwargs):
        path = "/posts/"+urllib.parse.quote(request.post_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.post_id = ""

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.discussion.UpdatePostOutput"),
            **kwargs,
        )

    def DeletePost(self, request, **kwargs):
        path = "/posts/"+urllib.parse.quote(request.post_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.post_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.discussion.DeletePostOutput"),
            **kwargs,
        )

    def VotePost(self, request, **kwargs):
        path = "/posts/"+urllib.parse.quote(request.post_id)+"/vote"

        # Cleanup URL parameters to avoid any ambiguity
        request.post_id = ""

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.discussion.VotePostOutput"),
            **kwargs,
        )
