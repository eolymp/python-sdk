# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

import urllib.parse
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class AchievementServiceClient:
    def __init__(self, transport, url="https://api.eolymp.com"):
        self.transport = transport
        self.url = url

    def AssignAchievement(self, request, **kwargs):
        path = "/achievements/"+urllib.parse.quote(request.achievement_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.achievement_id = ""

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.community.AssignAchievementOutput"),
            **kwargs,
        )

    def UnassignAchievement(self, request, **kwargs):
        path = "/achievements/"+urllib.parse.quote(request.achievement_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.achievement_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.community.UnassignAchievementOutput"),
            **kwargs,
        )

    def ListAchievements(self, request, **kwargs):
        path = "/achievements"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.community.ListAchievementsOutput"),
            **kwargs,
        )
