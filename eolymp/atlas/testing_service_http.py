# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler. DO NOT EDIT!
# See https://github.com/eolymp/contracts/tree/main/cmd/protoc-gen-python-esdk for more details.
"""Generated protocol buffer code."""

import urllib.parse
from google.protobuf import symbol_database as _symbol_database

_sym_db = _symbol_database.Default()


class TestingServiceClient:
    def __init__(self, transport, url="https://api.eolymp.com"):
        self.transport = transport
        self.url = url

    def UpdateChecker(self, request, **kwargs):
        path = "/verifier"

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.UpdateVerifierOutput"),
            **kwargs,
        )

    def DescribeChecker(self, request, **kwargs):
        path = "/verifier"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.DescribeVerifierOutput"),
            **kwargs,
        )

    def UpdateInteractor(self, request, **kwargs):
        path = "/interactor"

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.UpdateInteractorOutput"),
            **kwargs,
        )

    def DescribeInteractor(self, request, **kwargs):
        path = "/interactor"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.DescribeInteractorOutput"),
            **kwargs,
        )

    def CreateTestset(self, request, **kwargs):
        path = "/testsets"

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.CreateTestsetOutput"),
            **kwargs,
        )

    def UpdateTestset(self, request, **kwargs):
        path = "/testsets/"+urllib.parse.quote(request.testset_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.testset_id = ""

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.UpdateTestsetOutput"),
            **kwargs,
        )

    def DeleteTestset(self, request, **kwargs):
        path = "/testsets/"+urllib.parse.quote(request.testset_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.testset_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.DeleteTestsetOutput"),
            **kwargs,
        )

    def DescribeTestset(self, request, **kwargs):
        path = "/testsets/"+urllib.parse.quote(request.testset_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.testset_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.DescribeTestsetOutput"),
            **kwargs,
        )

    def ListTestsets(self, request, **kwargs):
        path = "/testsets"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.ListTestsetsOutput"),
            **kwargs,
        )

    def CreateTest(self, request, **kwargs):
        path = "/testsets/"+urllib.parse.quote(request.testset_id)+"/tests"

        # Cleanup URL parameters to avoid any ambiguity
        request.testset_id = ""

        return self.transport.request(
            method="POST",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.CreateTestOutput"),
            **kwargs,
        )

    def UpdateTest(self, request, **kwargs):
        path = "/testsets/"+urllib.parse.quote(request.testset_id)+"/tests/"+urllib.parse.quote(request.test_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.testset_id = ""
        request.test_id = ""

        return self.transport.request(
            method="PUT",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.UpdateTestOutput"),
            **kwargs,
        )

    def DeleteTest(self, request, **kwargs):
        path = "/testsets/"+urllib.parse.quote(request.testset_id)+"/tests/"+urllib.parse.quote(request.test_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.testset_id = ""
        request.test_id = ""

        return self.transport.request(
            method="DELETE",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.DeleteTestOutput"),
            **kwargs,
        )

    def DescribeTest(self, request, **kwargs):
        path = "/testsets/"+urllib.parse.quote(request.testset_id)+"/tests/"+urllib.parse.quote(request.test_id)

        # Cleanup URL parameters to avoid any ambiguity
        request.testset_id = ""
        request.test_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.DescribeTestOutput"),
            **kwargs,
        )

    def ListTests(self, request, **kwargs):
        path = "/testsets/"+urllib.parse.quote(request.testset_id)+"/tests"

        # Cleanup URL parameters to avoid any ambiguity
        request.testset_id = ""

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.ListTestsOutput"),
            **kwargs,
        )

    def ListExamples(self, request, **kwargs):
        path = "/examples"

        return self.transport.request(
            method="GET",
            url=self.url+path,
            request_data=request,
            response_symbol=_sym_db.GetSymbol("eolymp.atlas.ListExamplesOutput"),
            **kwargs,
        )
