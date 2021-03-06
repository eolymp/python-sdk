# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class UniverseClient:
    def __init__(self, transport):
        self.transport = transport

    def CreateSpace(self, request, **kwargs):
        return self.transport.request(
            url="eolymp.universe.Universe/CreateSpace",
            request=request,
            response_obj=_sym_db.GetSymbol("eolymp.universe.CreateSpaceOutput"),
            **kwargs,
        )

    def UpdateSpace(self, request, **kwargs):
        return self.transport.request(
            url="eolymp.universe.Universe/UpdateSpace",
            request=request,
            response_obj=_sym_db.GetSymbol("eolymp.universe.UpdateSpaceOutput"),
            **kwargs,
        )

    def DeleteSpace(self, request, **kwargs):
        return self.transport.request(
            url="eolymp.universe.Universe/DeleteSpace",
            request=request,
            response_obj=_sym_db.GetSymbol("eolymp.universe.DeleteSpaceOutput"),
            **kwargs,
        )

    def LookupSpace(self, request, **kwargs):
        return self.transport.request(
            url="eolymp.universe.Universe/LookupSpace",
            request=request,
            response_obj=_sym_db.GetSymbol("eolymp.universe.LookupSpaceOutput"),
            **kwargs,
        )

    def DescribeSpace(self, request, **kwargs):
        return self.transport.request(
            url="eolymp.universe.Universe/DescribeSpace",
            request=request,
            response_obj=_sym_db.GetSymbol("eolymp.universe.DescribeSpaceOutput"),
            **kwargs,
        )

    def DescribeQuota(self, request, **kwargs):
        return self.transport.request(
            url="eolymp.universe.Universe/DescribeQuota",
            request=request,
            response_obj=_sym_db.GetSymbol("eolymp.universe.DescribeQuotaOutput"),
            **kwargs,
        )

    def ListSpaces(self, request, **kwargs):
        return self.transport.request(
            url="eolymp.universe.Universe/ListSpaces",
            request=request,
            response_obj=_sym_db.GetSymbol("eolymp.universe.ListSpacesOutput"),
            **kwargs,
        )

    def GrantPermission(self, request, **kwargs):
        return self.transport.request(
            url="eolymp.universe.Universe/GrantPermission",
            request=request,
            response_obj=_sym_db.GetSymbol("eolymp.universe.GrantPermissionOutput"),
            **kwargs,
        )

    def RevokePermission(self, request, **kwargs):
        return self.transport.request(
            url="eolymp.universe.Universe/RevokePermission",
            request=request,
            response_obj=_sym_db.GetSymbol("eolymp.universe.RevokePermissionOutput"),
            **kwargs,
        )

    def DescribePermission(self, request, **kwargs):
        return self.transport.request(
            url="eolymp.universe.Universe/DescribePermission",
            request=request,
            response_obj=_sym_db.GetSymbol("eolymp.universe.DescribePermissionOutput"),
            **kwargs,
        )

    def IntrospectPermission(self, request, **kwargs):
        return self.transport.request(
            url="eolymp.universe.Universe/IntrospectPermission",
            request=request,
            response_obj=_sym_db.GetSymbol("eolymp.universe.IntrospectPermissionOutput"),
            **kwargs,
        )

    def ListPermissions(self, request, **kwargs):
        return self.transport.request(
            url="eolymp.universe.Universe/ListPermissions",
            request=request,
            response_obj=_sym_db.GetSymbol("eolymp.universe.ListPermissionsOutput"),
            **kwargs,
        )

