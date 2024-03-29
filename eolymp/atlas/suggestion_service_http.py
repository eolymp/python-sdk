# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

import urllib.parse
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class SuggestionServiceClient:
    def __init__(self, transport, url="https://api.eolymp.com"):
        self.transport = transport
        self.url = url

    def CreateSuggestion(self, request, **kwargs):
        path = "/suggestions"

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.CreateSuggestionOutput"),
            **kwargs,
        )

    def UpdateSuggestion(self, request, **kwargs):
        path = "/suggestions/"+urllib.parse.quote(request.suggestion_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.suggestion_id = ""

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.UpdateSuggestionOutput"),
            **kwargs,
        )

    def ReviewSuggestion(self, request, **kwargs):
        path = "/suggestions/"+urllib.parse.quote(request.suggestion_id)+"/review"

        # Cleanup URL parameters to avoid any ambiguity
        request.suggestion_id = ""

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.ReviewSuggestionOutput"),
            **kwargs,
        )

    def ResubmitSuggestion(self, request, **kwargs):
        path = "/suggestions/"+urllib.parse.quote(request.suggestion_id)+"/resubmit"

        # Cleanup URL parameters to avoid any ambiguity
        request.suggestion_id = ""

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.ResubmitSuggestionOutput"),
            **kwargs,
        )

    def DeleteSuggestion(self, request, **kwargs):
        path = "/suggestions/"+urllib.parse.quote(request.suggestion_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.suggestion_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.DeleteSuggestionOutput"),
            **kwargs,
        )

    def ListSuggestions(self, request, **kwargs):
        path = "/suggestions"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.ListSuggestionsOutput"),
            **kwargs,
        )

    def DescribeSuggestion(self, request, **kwargs):
        path = "/suggestions/"+urllib.parse.quote(request.suggestion_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.suggestion_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.DescribeSuggestionOutput"),
            **kwargs,
        )

