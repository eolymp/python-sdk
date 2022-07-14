import json
import time
import urllib.parse
import requests


class AccessToken(object):
    def __init__(self, access_token: str = "", refresh_token: str = "", expires_in: int = 0, token_type: str = ""):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.expires_in = expires_in
        self.token_type = token_type


class OAuthClient:
    def __init__(self, url: str = "https://api.eolymp.com", headers: dict = None, retry: int = 5):
        self._address = url.removesuffix("/") + "/"
        self._headers = headers if headers is not None else {}
        self._retry = retry if retry > 1 else 1

    def token(self, grant_type: str, client_id: str = "", client_secret="", username: str = "", password: str = "",
              code: str = "", code_verifier: str = "", refresh_token: str = "", scope: str = "", **kwargs):

        headers = self._headers
        headers["content-type"] = "application/x-www-form-urlencoded"

        wait = 1
        resp = requests.post(
            url=self._address + "oauth/token",
            headers=headers,
            data=urllib.parse.urlencode({
                "grant_type": grant_type,
                "scope": scope,
                "client_id": client_id,
                "client_secret": client_secret,
                "username": username,
                "password": password,
                "code": code,
                "code_verifier": code_verifier,
                "refresh_token": refresh_token,
            }),

            **kwargs
        )
        for t in range(0, self._retry):

            if resp.status_code == 429:
                time.sleep(wait)
                wait = wait + 1
                continue

            if resp.status_code == 200:
                data = json.loads(resp.content)

                return AccessToken(
                    data["access_token"] if "access_token" in data else "",
                    data["refresh_token"] if "refresh_token" in data else "",
                    data["expires_in"] if "expires_in" in data else 0,
                    data["token_type"] if "token_type" in data else "",
                )
            else:
                raise Exception("Got non-200 response: {}".format(resp.status_code) + str(resp.content))

