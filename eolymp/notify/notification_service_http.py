# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

import urllib.parse
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class NotificationServiceClient:
    def __init__(self, transport, url="https://api.eolymp.com"):
        self.transport = transport
        self.url = url

    def DescribeNotification(self, request, **kwargs):
        path = "/notifications/"+urllib.parse.quote(request.notification_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.notification_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.notify.DescribeNotificationOutput"),
            **kwargs,
        )

    def ReadNotification(self, request, **kwargs):
        path = "/notifications/"+urllib.parse.quote(request.notification_id)+"/read"

        # Cleanup URL parameters to avoid any ambiguity
        request.notification_id = ""

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.notify.ReadNotificationOutput"),
            **kwargs,
        )

    def DeleteNotification(self, request, **kwargs):
        path = "/notifications/"+urllib.parse.quote(request.notification_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.notification_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.notify.DeleteNotificationOutput"),
            **kwargs,
        )

    def ListNotifications(self, request, **kwargs):
        path = "/notifications"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.notify.ListNotificationsOutput"),
            **kwargs,
        )

    def DescribeNotificationConfig(self, request, **kwargs):
        path = "/configs/notifications"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.notify.DescribeNotificationConfigOutput"),
            **kwargs,
        )

    def UpdateNotificationConfig(self, request, **kwargs):
        path = "/configs/notifications"

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.notify.UpdateNotificationConfigOutput"),
            **kwargs,
        )
