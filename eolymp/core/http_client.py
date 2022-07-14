import time
import requests

from google.protobuf import json_format


class HttpClient:
    def __init__(self, url: str = "https://api.eolymp.com", token: str = "", headers: dict = None, retry: int = 5):
        self._address = url.removesuffix("/") + "/"
        self._token = token
        self._headers = headers if headers is not None else {}
        self._retry = retry if retry > 1 else 1

    def request(self, url: str, request: object, response_obj: str, **kwargs):
        headers = self._headers
        headers["content-type"] = "application/json"

        if "space_id" in kwargs:
            headers["space-id"] = kwargs["space_id"]

        if self._token:
            headers["authorization"] = "Bearer " + self._token

        wait = 1
        for t in range(0, self._retry):
            resp = requests.post(url=self._address + url, data=json_format.MessageToJson(request), headers=headers,
                                 **kwargs)

            if resp.status_code == 429:
                time.sleep(wait)
                wait = wait + 1
                continue

            if resp.status_code == 200:
                response = response_obj()
                json_format.Parse(resp.content, response)
                return response
            else:
                raise Exception("Got non-200 response: {}".format(resp.status_code))
