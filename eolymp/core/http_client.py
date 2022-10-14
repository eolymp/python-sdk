import time
import urllib.parse

import requests

from google.protobuf import json_format


class HttpClient:
    def __init__(self, token: str = "", headers: dict = None, retry: int = 5):
        self._token = token
        self._headers = headers if headers is not None else {}
        self._retry = retry if retry > 1 else 1

    def request(self, url: str, method: str, request_data: object, response_symbol: str, **kwargs):
        headers = self._headers
        headers["content-type"] = "application/json"

        if self._token:
            headers["authorization"] = "Bearer " + self._token

        wait = 1
        for t in range(0, self._retry):
            data = json_format.MessageToJson(request_data)
            if method == "GET":
                query = ("?q=" + urllib.parse.quote(data)) if data != "{}" else ""
                resp = requests.request(url=url+query, method=method, headers=headers, **kwargs)
            else:
                resp = requests.request(url=url, method=method, data=data, headers=headers, **kwargs)

            if resp.status_code == 429:
                time.sleep(wait)
                wait = wait + 1
                continue

            if resp.status_code == 200:
                response = response_symbol()
                json_format.Parse(resp.content, response, ignore_unknown_fields=True)
                return response
            else:
                raise Exception("Got non-200 response: {}".format(resp.status_code))
