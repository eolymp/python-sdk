# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

import urllib.parse
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class ScoreboardServiceClient:
    def __init__(self, transport, url="https://api.eolymp.com"):
        self.transport = transport
        self.url = url

    def DescribeScoreboard(self, request, **kwargs):
        path = "/scoreboard"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.judge.DescribeScoreboardOutput"),
            **kwargs,
        )

    def ListScoreboardRows(self, request, **kwargs):
        path = "/scoreboard/rows"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.judge.ListScoreboardRowsOutput"),
            **kwargs,
        )

