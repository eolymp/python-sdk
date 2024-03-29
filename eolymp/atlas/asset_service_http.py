# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

import urllib.parse
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class AssetServiceClient:
    def __init__(self, transport, url="https://api.eolymp.com"):
        self.transport = transport
        self.url = url

    def UploadFile(self, request, **kwargs):
        path = "/data/files"

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.UploadFileOutput"),
            **kwargs,
        )

    def StartMultipartUpload(self, request, **kwargs):
        path = "/data/uploads"

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.StartMultipartUploadOutput"),
            **kwargs,
        )

    def UploadPart(self, request, **kwargs):
        path = "/data/uploads/"+urllib.parse.quote(request.upload_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.upload_id = ""

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.UploadPartOutput"),
            **kwargs,
        )

    def CompleteMultipartUpload(self, request, **kwargs):
        path = "/data/uploads/"+urllib.parse.quote(request.upload_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.upload_id = ""

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.CompleteMultipartUploadOutput"),
            **kwargs,
        )

